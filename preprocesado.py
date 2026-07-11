def quitar_media(senal):
    media = senal.mean()
    senal_sin_media = senal - media

    return senal_sin_media, media