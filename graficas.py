import matplotlib.pyplot as plt
import numpy as np


def dibujar_velocidad(tiempo, velocidad, titulo):
    plt.figure(figsize=(15, 8))

    plt.plot(tiempo, velocidad)

    plt.xticks(
        np.arange(0, tiempo.max() + 1, 20)
    )

    plt.xlabel("Tiempo (s)")
    plt.ylabel("Velocidad (m/s)")
    plt.title(titulo)
    plt.grid(True)

    plt.show()

def dibujar_espectro(frecuencias, magnitudes, titulo):
    plt.figure(figsize=(15, 8))

    plt.plot(frecuencias, magnitudes)

    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud")
    plt.title(titulo)
    plt.grid(True)

    plt.xlim(0, 4) # frecuencias razonables para pasos

    plt.show()