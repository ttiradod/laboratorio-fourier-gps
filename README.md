# Laboratorio Fourier GPS

Este proyecto es un mini laboratorio en Python para estudiar si las pequeñas oscilaciones de velocidad registradas por un GPS a 10 Hz pueden utilizarse para estimar la cadencia de pasos en un tramo.

La idea principal es tratar la velocidad GPS como una señal discreta en el tiempo y aplicar análisis de Fourier mediante DFT/FFT para buscar la frecuencia dominante de la oscilación.



CSV GPS
↓
velocidad GPS
↓
selección de tramo
↓
quitar media
↓
quitar tendencia lenta
↓
ventana Hanning
↓
calcular frecuencia de muestreo
↓
FFT
↓
frecuencia dominante
↓
cadencia en pasos/min
↓
pasos estimados del tramo


## Aclaración importante

Este análisis calcula una frecuencia dominante del tramo completo. Por tanto, la cadencia obtenida representa una estimación global o media dominante del tramo analizado.

No representa todavía una cadencia instantánea segundo a segundo.


