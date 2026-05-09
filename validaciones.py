def limpiar_texto(texto):
    """
    Elimina caracteres conflictivos (punto y coma, dos puntos) y espacios al inicio/final.
    """
    if not isinstance(texto, str):
        return str(texto)
    return texto.replace(";", "").replace(":", "").strip()

def validar_id(id_str):
    """
    Valida que el ID sea un número entero positivo.
    """
    try:
        id_num = int(id_str)
        if id_num <= 0:
            return False, "El ID debe ser un número entero positivo."
        return True, id_num
    except ValueError:
        return False, "El ID debe ser un número válido."
