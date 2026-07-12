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