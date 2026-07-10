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