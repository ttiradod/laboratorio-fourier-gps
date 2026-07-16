import plotly.graph_objects as go


def dibujar_cadencia_interactiva(
    resultados_ventanas,
    archivo_salida="cadencia_ventanas.html"
):
    tiempos = []
    cadencias = []
    textos_hover = []

    for resultado in resultados_ventanas:
        tiempos.append(resultado["tiempo_central"])
        cadencias.append(resultado["cadencia"])

        texto = (
            "Ventana: "
            + str(resultado["inicio"])
            + " - "
            + str(resultado["fin"])
            + " s"
            + "<br>Tiempo central: "
            + str(round(resultado["tiempo_central"], 2))
            + " s"
            + "<br>Cadencia: "
            + str(round(resultado["cadencia"], 2))
            + " pasos/min"
            + "<br>Frecuencia dominante: "
            + str(round(resultado["frecuencia_dominante"], 4))
            + " Hz"
            + "<br>Magnitud: "
            + str(round(resultado["magnitud_dominante"], 4))
        )

        textos_hover.append(texto)

    figura = go.Figure()

    figura.add_trace(
        go.Scatter(
            x=tiempos,
            y=cadencias,
            mode="lines+markers",
            text=textos_hover,
            hovertemplate="%{text}<extra></extra>"
        )
    )

    figura.update_layout(
        title="Cadencia estimada por ventanas",
        xaxis_title="Tiempo central de la ventana (s)",
        yaxis_title="Cadencia estimada (pasos/min)",
        hovermode="closest"
    )

    figura.write_html(
        archivo_salida,
        auto_open=True
    )

    print()
    print("Gráfica interactiva creada:", archivo_salida)