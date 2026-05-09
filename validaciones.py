def limpiar_texto(texto):
    """
    Elimina caracteres conflictivos (punto y coma, dos puntos) y espacios al inicio/final.
    """
    if not isinstance(texto, str):
        return str(texto)
    return texto.replace(";", "").replace(":", "").strip()