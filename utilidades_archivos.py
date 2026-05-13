import os
import datetime
import config

def inicializar_entorno():

    # Crear directorios si no existen y archivos necesarios
    try:
        if not os.path.exists(config.DIRECTORIO_DATOS):
            os.makedirs(config.DIRECTORIO_DATOS)

        if not os.path.exists(config.DIRECTORIO_LOGS):
            os.makedirs(config.DIRECTORIO_LOGS)

        if not os.path.exists(config.DIRECTORIO_RESPALDOS):
            os.makedirs(config.DIRECTORIO_RESPALDOS)
        with open(config.ARCHIVO_EXPEDIENTES, 'w', encoding='utf-8') as f:
            pass # Crea el archivo vacío

        if not os.path.exists(config.ARCHIVO_LOGS):
            with open(config.ARCHIVO_LOGS, 'w', encoding='utf-8') as f:
                pass # Crea el archivo vacío

    except Exception as e:
        print(f"Error crítico al inicializar el entorno: {e}")

def registrar_error(mensaje_error):
    # Registra un error en el archivo de logs con la fecha y hora actual
    try:
        with open(config.ARCHIVO_LOGS, 'a', encoding='utf-8') as f:
            fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{fecha_actual}] ERROR: {mensaje_error}\n")
    except Exception as e:
        print(f"Error al intentar registrar el log: {e}")
        