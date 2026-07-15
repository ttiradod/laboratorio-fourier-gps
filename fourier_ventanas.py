from preprocesado import aplicar_ventana_hanning
from fourier import calcular_espectro_fourier, buscar_frecuencia_dominante
from cadencia import frecuencia_a_cadencia_minuto


def analizar_ventanas_fourier(
    ventanas,
    frecuencia_muestreo,
    frecuencia_min,
    frecuencia_max
):
    resultados = []

    for ventana in ventanas:
        senal_ventana = ventana["senal"]

        senal_preparada, ventana_hanning = aplicar_ventana_hanning(
            senal_ventana
        )

        frecuencias, magnitudes = calcular_espectro_fourier(
            senal_preparada,
            frecuencia_muestreo
        )

        frecuencia_dominante, magnitud_dominante = buscar_frecuencia_dominante(
            frecuencias,
            magnitudes,
            frecuencia_min,
            frecuencia_max
        )

        cadencia = frecuencia_a_cadencia_minuto(
            frecuencia_dominante
        )

        resultados.append({
            "inicio": ventana["inicio"],
            "fin": ventana["fin"],
            "tiempo_central": ventana["tiempo_central"],
            "frecuencia_dominante": frecuencia_dominante,
            "magnitud_dominante": magnitud_dominante,
            "cadencia": cadencia
        })

    return resultados