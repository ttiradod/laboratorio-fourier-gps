import numpy as np


def quitar_media(senal):
    media = senal.mean()
    senal_sin_media = senal - media

    return senal_sin_media, media


# Quitar la "tendencia lenta"
# Tendencia lenta = cambio progresivo de la velocidad a lo largo del tramo.
# La quitamos para que Fourier se centre en las oscilaciones rápidas producidas por los pasos, no en cambios lentos de velocidad.


# Python calcula una recta que resume la subida/bajada general
# se la resta a la señal y queda una señal más limpia para Fourier
def quitar_tendencia(tiempo, senal):
    coeficientes = np.polyfit(tiempo, senal, 1) # Encuentra la recta que mejor resume la evolución general de esta señal.

    tendencia = np.polyval(coeficientes, tiempo) # crea los valores de esa recta en cada instante de tiempo.

    senal_sin_tendencia = senal - tendencia # resta esa recta a la señal.

    return senal_sin_tendencia, tendencia