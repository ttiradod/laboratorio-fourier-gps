def mostrar_info_tramo(tiempo_tramo, velocidad_tramo):
    print()
    print("INFORMACIÓN DEL TRAMO AJUSTADO")
    print("------------------------------")
    print("Número de muestras:", len(tiempo_tramo))
    print("Tiempo inicial del tramo:", tiempo_tramo.iloc[0], "s")
    print("Tiempo final del tramo:", tiempo_tramo.iloc[-1], "s")
    print("Duración del tramo:", tiempo_tramo.iloc[-1] - tiempo_tramo.iloc[0], "s")
    print("Primera velocidad:", velocidad_tramo.iloc[0], "m/s")
    print("Última velocidad:", velocidad_tramo.iloc[-1], "m/s")
    print("Velocidad media del tramo:", velocidad_tramo.mean(), "m/s")


def mostrar_primeras_muestras(tiempo_tramo, velocidad_tramo, cantidad=20):
    print()
    print("PRIMERAS VELOCIDADES DEL TRAMO")
    print("------------------------------")

    for i in range(cantidad):
        print(
            i,
            "tiempo:", round(tiempo_tramo.iloc[i], 3), "s",
            "velocidad:", velocidad_tramo.iloc[i], "m/s"
        )


def guardar_valores_tramo(nombre_archivo, tiempo_tramo, velocidad_tramo, velocidad_sin_media):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("indice,tiempo_s,velocidad_mps,velocidad_sin_media\n")

        for i in range(len(tiempo_tramo)):
            archivo.write(
                f"{i},{tiempo_tramo.iloc[i]},{velocidad_tramo.iloc[i]},{velocidad_sin_media.iloc[i]}\n"
            )

    print()
    print("Archivo", nombre_archivo, "creado.")