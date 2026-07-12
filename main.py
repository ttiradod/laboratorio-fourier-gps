from lector_csv import buscar_archivos_csv, cargar_csv
from graficas import dibujar_velocidad, dibujar_espectro


archivos_csv = buscar_archivos_csv()

if len(archivos_csv) == 0:
    print("No he encontrado archivos CSV.")
    quit()


print("Archivos CSV encontrados:")

for numero, archivo in enumerate(archivos_csv, start=1):
    print(numero, "-", archivo)


opcion = int(input("Elige el número del archivo que quieres analizar: "))

archivo_elegido = archivos_csv[opcion - 1]

datos = cargar_csv(archivo_elegido)


tiempo = datos["esp_ms"] / 1000

tiempo = tiempo - tiempo.iloc[0]

velocidad = datos["speed_2d_mps"]


dibujar_velocidad(
    tiempo,
    velocidad,
    "Velocidad GPS"
)


# FASE 2: SELECCIONAR TRAMO

from tramos import pedir_tramo, recortar_tramo, ajustar_tramo_por_umbral

inicio, fin = pedir_tramo()

tiempo_tramo, velocidad_tramo = recortar_tramo(
    tiempo,
    velocidad,
    inicio,
    fin
)

tiempo_tramo, velocidad_tramo = ajustar_tramo_por_umbral(
    tiempo_tramo,
    velocidad_tramo,
    umbral=0.5
)

dibujar_velocidad(
    tiempo_tramo,
    velocidad_tramo,
    "Tramo ajustado"
)

# FASE 2.5: Ver los numeros reales que hay detrás de la gráfica >> verdatos.py

from verdatos import mostrar_info_tramo, mostrar_primeras_muestras, guardar_valores_tramo

mostrar_info_tramo(tiempo_tramo, velocidad_tramo)

mostrar_primeras_muestras(
    tiempo_tramo,
    velocidad_tramo,
    cantidad=20
)

# FASE 3: PREPARAR LA SEÑAL PARA FOURIER
 

# Fase 3.1  quitar media

from preprocesado import quitar_media, quitar_tendencia, aplicar_ventana_hanning

velocidad_sin_media, media_velocidad = quitar_media(velocidad_tramo)

print()
print("FASE 3: QUITAR LA MEDIA")
print("-----------------------")
print("Media de velocidad:", media_velocidad, "m/s")

dibujar_velocidad(
    tiempo_tramo,
    velocidad_sin_media,
    "Velocidad sin media"
)


guardar_valores_tramo(
    "valores_tramo.txt",
    tiempo_tramo,
    velocidad_tramo,
    velocidad_sin_media
)

# Fase 3.2 quitar tendencia lenta

velocidad_sin_tendencia, tendencia = quitar_tendencia(
    tiempo_tramo,
    velocidad_sin_media
)

dibujar_velocidad(
    tiempo_tramo,
    velocidad_sin_tendencia,
    "Velocidad sin tendencia lenta"
)


# Fase 3.3 aplicar ventana Hanning

senal_preparada, ventana = aplicar_ventana_hanning(
    velocidad_sin_tendencia
)

dibujar_velocidad(
    tiempo_tramo,
    senal_preparada,
    "Señal preparada con ventana Hanning"
)


# FASE 4: calcular la frecuencia de muestreo real

# Fourier necesita saber cada cuánto tiempo están separadas las muestras.
from muestreo import calcular_frecuencia_muestreo

frecuencia_muestreo, dt_medio = calcular_frecuencia_muestreo(tiempo_tramo)

print()
print("FASE 4: FRECUENCIA DE MUESTREO")
print("------------------------------")
print("Tiempo medio entre muestras:", dt_medio, "s")
print("Frecuencia de muestreo:", frecuencia_muestreo, "Hz")

# FASE 5: FOURIER GLOBAL

from fourier import calcular_espectro_fourier, buscar_frecuencia_dominante

# FASE 5.1: CALCULAR FOURIER Y DIBUJAR EL ESPECTRO --> ¿Qué frecuencias aparecen dentro de mi señal preparada?


frecuencias, magnitudes = calcular_espectro_fourier(
    senal_preparada,
    frecuencia_muestreo
)

dibujar_espectro(
    frecuencias,
    magnitudes,
    "Espectro de frecuencias"
)

# FASE 5.2: BUSCAR FRECUENCIA DOMINANTE --> Dentro del rango lógico de pasos, ¿qué frecuencia tiene la mayor magnitud?

frecuencia_dominante, magnitud_dominante = buscar_frecuencia_dominante(
    frecuencias,
    magnitudes,
    frecuencia_min=0.7,
    frecuencia_max=2.5
)

print()
print("FASE 5.2: FRECUENCIA DOMINANTE")
print("------------------------------")
print("Frecuencia dominante:", frecuencia_dominante, "Hz")
print("Magnitud dominante:", magnitud_dominante)


# FASE 6: CONVERTIR FRECUENCIA DOMINANTE A PASOS/MIN

from cadencia import frecuencia_a_cadencia_minuto

cadencia_pasos_min = frecuencia_a_cadencia_minuto(
    frecuencia_dominante
)

print()
print("FASE 6: CADENCIA ESTIMADA")
print("-------------------------")
print("Cadencia estimada:", cadencia_pasos_min, "pasos/min")