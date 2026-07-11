import numpy as np


# Calculamos la frecuencia de muestreo real.
# Aunque el GPS esté configurado a 10 Hz, es mejor comprobarlo usando los tiempos reales.
# Primero calculamos cuánto tiempo pasa entre una muestra y la siguiente.
# Después hacemos fs = 1 / dt, porque si una muestra llega cada 0.1 s, entonces recibimos 10 muestras por segundo.
# 
# Esta fs será necesaria para que Fourier pueda convertir el resultado a Hz.

def calcular_frecuencia_muestreo(tiempo):
    diferencias_tiempo = np.diff(tiempo) # Calcula la diferencia entre cada tiempo y el siguiente.

    dt_medio = np.median(diferencias_tiempo) # Calcula el tiempo típico entre muestras.

    frecuencia_muestreo = 1 / dt_medio

    return frecuencia_muestreo, dt_medio