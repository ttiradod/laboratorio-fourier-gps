import glob
import pandas as pd


def buscar_archivos_csv():
    archivos = glob.glob("*.csv")
    return archivos


def cargar_csv(nombre_archivo):
    datos = pd.read_csv(nombre_archivo)
    return datos