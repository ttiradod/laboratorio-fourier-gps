import numpy as np


# Calculamos el espectro de frecuencias de la señal.
# La señal ya debe venir preparada: sin media, sin tendencia lenta y con ventana Hanning aplicada.
#
# Fourier compara nuestra señal con muchas ondas de distintas frecuencias.

# El resultado nos dice qué frecuencias están más presentes en la señal.

def calcular_espectro_fourier(senal, frecuencia_muestreo):
    numero_muestras = len(senal) # Guarda cuántos datos tiene la señal

    transformada = np.fft.rfft(senal) # Esto calcula la transformada y devuelve la información de frecuencia

    frecuencias = np.fft.rfftfreq(
        numero_muestras,
        d=1 / frecuencia_muestreo
    ) # Esto crea el eje X del espectro

    magnitudes = np.abs(transformada) # puntuación de cada frecuencia

    return frecuencias, magnitudes