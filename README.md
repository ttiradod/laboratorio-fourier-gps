# Laboratorio Fourier GPS

Este proyecto es un mini laboratorio en Python para estudiar si las pequeñas oscilaciones de velocidad registradas por un GPS a 10 Hz pueden utilizarse para estimar la cadencia de pasos en un tramo.

La idea principal es tratar la velocidad GPS como una señal discreta en el tiempo y aplicar análisis de Fourier mediante DFT/FFT para buscar la frecuencia dominante de la oscilación.



CSV GPS --> velocidad GPS --> selección de tramo --> quitar media --> quitar tendencia lenta --> ventana Hanning --> calcular frecuencia de muestreo --> FFT --> frecuencia dominante --> cadencia en pasos/min --> pasos estimados del tramo


## Aclaración importante

Este análisis calcula una frecuencia dominante del tramo completo. Por tanto, la cadencia obtenida representa una estimación global o media dominante del tramo analizado.

No representa todavía una cadencia instantánea segundo a segundo.


## Validación con Garmin

Se realizó una validación inicial comparando el algoritmo con dos pruebas registradas con Garmin.

La documentación completa está disponible en:

[Validación inicial con Garmin](docs/validacion_garmin.md)

## Fourier por ventanas

La segunda fase del proyecto aplica Fourier en ventanas temporales para estudiar cómo cambia la cadencia estimada a lo largo del tramo.

Esta fase permite detectar zonas donde la frecuencia dominante es estable y zonas donde la señal GPS no representa bien la cadencia.

La documentación completa está disponible en:

[Fourier por ventanas](docs/fourier_por_ventanas.md)

