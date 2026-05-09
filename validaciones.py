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

def validar_nota(nota_str):
    """
    Valida que la nota sea un número entre 0 y 10.
    """
    try:
        nota_num = float(nota_str)
        if 0 <= nota_num <= 10:
            return True, round(nota_num, 2)
        else:
            return False, "La nota debe estar entre 0 y 10."
    except ValueError:
        return False, "La nota debe ser un número válido (ej. 8.5)."