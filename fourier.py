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


# Buscamos la frecuencia dominante dentro de un rango lógico.
# No buscamos el máximo de todo el espectro porque cerca de 0 Hz pueden aparecer cambios muy lentos de la señal que no representan pasos.
# Para caminar usamos, por ejemplo, un rango entre 0.7 Hz y 2.5 Hz.
# La frecuencia con mayor magnitud dentro de ese rango será la frecuencia dominante.

def buscar_frecuencia_dominante(frecuencias, magnitudes, frecuencia_min, frecuencia_max):
    zona_interes = (frecuencias >= frecuencia_min) & (frecuencias <= frecuencia_max)
    # Crea una máscara: de todas las frecuencias del espectro, se queda solo con las que están entre: frecuencia_min y frecuencia_max
    frecuencias_zona = frecuencias[zona_interes]
    magnitudes_zona = magnitudes[zona_interes]

    indice_maximo = np.argmax(magnitudes_zona) # ¿Dónde está el pico más alto dentro de la zona de pasos?

    frecuencia_dominante = frecuencias_zona[indice_maximo]
    magnitud_dominante = magnitudes_zona[indice_maximo]
    # la frecuencia ganadora y la magnitud de esa frecuencia

    return frecuencia_dominante, magnitud_dominante