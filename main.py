from lector_csv import buscar_archivos_csv, cargar_csv
from graficas import dibujar_velocidad


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