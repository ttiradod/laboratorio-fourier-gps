def crear_ventanas(tiempo, senal, duracion_ventana, salto_ventana):
    ventanas = []

    inicio = 0

    tiempo_final = tiempo.iloc[-1]

    while inicio + duracion_ventana <= tiempo_final:
        fin = inicio + duracion_ventana

        mascara = (tiempo >= inicio) & (tiempo <= fin)

        tiempo_ventana = tiempo[mascara].reset_index(drop=True)
        senal_ventana = senal[mascara].reset_index(drop=True)

        if len(tiempo_ventana) > 0:
            tiempo_central = inicio + duracion_ventana / 2

            ventanas.append({
                "inicio": inicio,
                "fin": fin,
                "tiempo_central": tiempo_central,
                "tiempo": tiempo_ventana,
                "senal": senal_ventana
            })

        inicio = inicio + salto_ventana

    return ventanas