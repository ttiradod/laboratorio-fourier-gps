# Convertimos una frecuencia en Hz a cadencia por minuto.
#
# Hz significa repeticiones por segundo.
# Ejemplo: Si Fourier nos dice que la frecuencia dominante es 1.46 Hz, eso significa que la señal se repite unas 1.46 veces cada segundo.
#
# Para pasar de repeticiones/segundo a repeticiones/minuto, multiplicamos por 60.
#
# En este laboratorio interpretamos esas repeticiones como pasos, por eso el resultado será pasos por minuto.

def frecuencia_a_cadencia_minuto(frecuencia_hz):
    cadencia_minuto = frecuencia_hz * 60

    return cadencia_minuto



# Estimamos cuántas repeticiones se han producido en todo el tramo.
#
# Si la frecuencia dominante está en Hz, significa repeticiones por segundo.
# Por ejemplo: 1.46 Hz = 1.46 repeticiones cada segundo.
#
# Si multiplicamos esa frecuencia por la duración del tramo en segundos, obtenemos una estimación del número total de repeticiones.
#
# En este laboratorio interpretamos esas repeticiones como pasos.

# !!!! Importante: esto estima los pasos del tramo completo, no los pasos exactos segundo a segundo.

def estimar_repeticiones_tramo(frecuencia_hz, duracion_segundos):
    repeticiones_estimadas = frecuencia_hz * duracion_segundos

    return repeticiones_estimadas