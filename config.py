import os

# Configuración del curso
CURSO_ACTUAL = "1º ASIR"

# Asignaturas válidas para el curso
ASIGNATURAS_VALIDAS = [
    "Implementacion de sistemas",
    "Bases de datos",
    "Programacion",
    "Redes",
    "Hardware",
    "IPPE",
    "Lenguaje de Marcas"
]

# Rutas de archivos y carpetas
DIRECTORIO_DATOS = "data"
DIRECTORIO_LOGS = "logs"

ARCHIVO_EXPEDIENTES = os.path.join(DIRECTORIO_DATOS, "expedientes.txt")
ARCHIVO_LOGS = os.path.join(DIRECTORIO_LOGS, "errores.log")