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