import os
import shutil
import config
from utilidades_archivos import registrar_error

def _parsear_linea(linea):
    """
    Convierte una línea de texto del archivo en un diccionario.
    Formato esperado: ID;Nombre;Apellidos;Curso;Asig1:Nota1,Asig2:Nota2
    """
    try:
        partes = linea.strip().split(";")
        if len(partes) < 5:
            # Si no hay calificaciones, la longitud puede ser 4
            if len(partes) == 4:
                partes.append("")
            else:
                raise ValueError("Formato de línea incorrecto.")
        
        id_str, nombre, apellidos, curso, notas_str = partes
        
        notas = {}
        if notas_str:
            pares_notas = notas_str.split(",")
            for par in pares_notas:
                if ":" in par:
                    asignatura, nota = par.split(":")
                    notas[asignatura] = float(nota)
                    
        return {
            "id": int(id_str),
            "nombre": nombre,
            "apellidos": apellidos,
            "curso": curso,
            "notas": notas
        }
    except Exception as e:
        registrar_error(f"Error al parsear la línea '{linea}': {e}")
        return None

def _formatear_diccionario(datos):
    """
    Convierte un diccionario de expediente a una cadena de texto para el archivo.
    """
    notas_str = ",".join([f"{asig}:{nota}" for asig, nota in datos["notas"].items()])
    return f"{datos['id']};{datos['nombre']};{datos['apellidos']};{datos['curso']};{notas_str}\n"

def crear_expediente(datos):
    """
    Añade un nuevo expediente al final del archivo.
    """
    try:
        # Verificar si el ID ya existe
        existentes = leer_expedientes()
        if any(exp["id"] == datos["id"] for exp in existentes if exp):
            return False, "Ya existe un expediente con este ID."
            
        linea = _formatear_diccionario(datos)
        with open(config.ARCHIVO_EXPEDIENTES, 'a', encoding='utf-8') as f:
            f.write(linea)
        return True, "Expediente creado con éxito."
    except Exception as e:
        registrar_error(f"Error al crear expediente: {e}")
        raise

def leer_expedientes():
    """
    Lee todos los expedientes del archivo y devuelve una lista de diccionarios.
    """
    expedientes = []
    try:
        with open(config.ARCHIVO_EXPEDIENTES, 'r', encoding='utf-8') as f:
            for linea in f:
                if linea.strip():
                    exp_dict = _parsear_linea(linea)
                    if exp_dict:
                        expedientes.append(exp_dict)
        return expedientes
    except Exception as e:
        registrar_error(f"Error al leer expedientes: {e}")
        raise

def buscar_expediente(id_expediente):
    """
    Busca un expediente por su ID y lo devuelve.
    """
    try:
        expedientes = leer_expedientes()
        for exp in expedientes:
            if exp["id"] == id_expediente:
                return exp
        return None
    except Exception as e:
        registrar_error(f"Error al buscar expediente {id_expediente}: {e}")
        raise

def actualizar_expediente(id_expediente, nuevos_datos):
    """
    Actualiza un expediente existente sobrescribiendo el archivo de forma segura.
    """
    try:
        expedientes = leer_expedientes()
        actualizado = False
        
        for i, exp in enumerate(expedientes):
            if exp["id"] == id_expediente:
                expedientes[i] = nuevos_datos
                actualizado = True
                break
                
        if not actualizado:
            return False, "Expediente no encontrado."
            
        _reescribir_archivo(expedientes)
        return True, "Expediente actualizado con éxito."
    except Exception as e:
        registrar_error(f"Error al actualizar expediente {id_expediente}: {e}")
        raise

def eliminar_expediente(id_expediente):
    """
    Elimina un expediente filtrándolo de la lista y reescribiendo el archivo.
    """
    try:
        expedientes = leer_expedientes()
        len_original = len(expedientes)
        expedientes_filtrados = [exp for exp in expedientes if exp["id"] != id_expediente]
        
        if len(expedientes) == len(expedientes_filtrados):
            return False, "Expediente no encontrado."
            
        _reescribir_archivo(expedientes_filtrados)
        return True, "Expediente eliminado con éxito."
    except Exception as e:
        registrar_error(f"Error al eliminar expediente {id_expediente}: {e}")
        raise

def _reescribir_archivo(expedientes):
    """
    Reescribe el archivo completo usando un archivo temporal para mayor seguridad.
    """
    archivo_temp = config.ARCHIVO_EXPEDIENTES + ".tmp"
    with open(archivo_temp, 'w', encoding='utf-8') as f:
        for exp in expedientes:
            f.write(_formatear_diccionario(exp))
            
    # Reemplazar atómicamente el original con el temporal
    shutil.move(archivo_temp, config.ARCHIVO_EXPEDIENTES)