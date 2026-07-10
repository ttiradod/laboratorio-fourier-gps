def pedir_tramo():
    inicio = float(input("Introduce el segundo inicial del tramo: "))
    fin = float(input("Introduce el segundo final del tramo: "))

    return inicio, fin


def recortar_tramo(tiempo, senal, inicio, fin):
    mascara = (tiempo >= inicio) & (tiempo <= fin)

    tiempo_tramo = tiempo[mascara].reset_index(drop=True)
    senal_tramo = senal[mascara].reset_index(drop=True)

    tiempo_tramo = tiempo_tramo - tiempo_tramo.iloc[0]

    return tiempo_tramo, senal_tramo


def ajustar_tramo_por_umbral(tiempo, senal, umbral=0.5, min_muestras=10):
    """
    Dentro de un tramo ya recortado, busca los segmentos donde
    la señal está por encima de un umbral.

    Si hay varios segmentos, se queda con el más largo.
    """

    en_movimiento = senal > umbral

    segmentos = []
    inicio_segmento = None

    for i in range(len(en_movimiento)):

        if en_movimiento.iloc[i] and inicio_segmento is None:
            inicio_segmento = i

        if (
            (not en_movimiento.iloc[i] or i == len(en_movimiento) - 1)
            and inicio_segmento is not None
        ):

            if en_movimiento.iloc[i] and i == len(en_movimiento) - 1:
                fin_segmento = i
            else:
                fin_segmento = i - 1

            longitud = fin_segmento - inicio_segmento + 1

            if longitud >= min_muestras:
                segmentos.append(
                    (inicio_segmento, fin_segmento)
                )

            inicio_segmento = None

    if len(segmentos) == 0:
        print("No se ha encontrado un tramo claro de movimiento.")
        return tiempo, senal

    segmento_mas_largo = max(
        segmentos,
        key=lambda segmento: segmento[1] - segmento[0]
    )

    inicio, fin = segmento_mas_largo

    tiempo_ajustado = tiempo.iloc[inicio:fin + 1].reset_index(drop=True)
    senal_ajustada = senal.iloc[inicio:fin + 1].reset_index(drop=True)

    tiempo_ajustado = tiempo_ajustado - tiempo_ajustado.iloc[0]

    return tiempo_ajustado, senal_ajustada