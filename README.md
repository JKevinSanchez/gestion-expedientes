# Sistema de Gestión de Expedientes Académicos (ASIR)
Este proyecto es una aplicación de consola desarrollada en Python diseñada para la gestión integral de expedientes de alumnos. Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre un sistema de persistencia basado en ficheros de texto plano.
##  Características principales

* **Persistencia en Ficheros**
    * Los datos se almacenan de forma estructurada en un archivo `.txt`.
* **Escritura Atómica**
    * Implementa un sistema de guardado mediante archivos temporales.
    * Evita la corrupción de datos en caso de fallo del sistema.
* **Validación Estricta**
    * Control total sobre la entrada de datos:
        * IDs únicos y enteros positivos.
        * Rangos de notas estrictos de 0 a 10.
        * Limpieza automática de caracteres conflictivos (como `;` o `:`).
* **Generador de Datos**
    * Incluye un script para poblar el sistema de forma automática.
    * Genera un entorno de prueba inicial con 50 registros.
* **Sistema de Logs**
    * Registro analítico de errores técnicos.
    * Incluye marcas de fecha y hora para facilitar el mantenimiento.

---

##  Estructura del Proyecto

El código se organiza de forma modular para separar la lógica de negocio de la interfaz de usuario:

* **`main.py`** – *Descripción:* Punto de entrada principal de la aplicación.
    * *Función:* Inicializa el entorno físico de carpetas y lanza el bucle del menú.
* **`menu.py`** – *Descripción:* Interfaz de usuario basada en consola de comandos.
    * *Función:* Captura las opciones del terminal, gestiona las respuestas visuales y controla las interrupciones del teclado.
* **`gestor_expedientes.py`** – *Descripción:* Núcleo principal de la lógica del negocio.
    * *Función:* Procesa las operaciones CRUD y maneja los algoritmos de lectura/escritura atómica en los archivos.
* **`validaciones.py`** – *Descripción:* Módulo de seguridad perimetral de datos.
    * *Función:* Contiene las funciones de comprobación de tipos, rangos de notas y desinfección de strings.
* **`utilidades_archivos.py`** – *Descripción:* Infraestructura interna del sistema.
    * *Función:* Gestión de directorios (creación de carpetas de datos/logs) y volcado del historial de errores.
* **`generador_datos.py`** – *Descripción:* Utilidad de desarrollo independiente.
    * *Función:* Script diseñado para generar expedientes aleatorios de prueba y guardarlos directamente en `expedientes.txt`.
* **`config.py`** – *Descripción:* Archivo global de configuración.
    * *Función:* Define constantes esenciales, rutas físicas de guardado y asignaturas válidas del curso.