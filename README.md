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

---

##  Instalación y Uso

1. **Clonar el repositorio**
    * Puedes descargar el código del proyecto ejecutando en tu terminal:
    ```bash
    git clone [https://github.com/JKevinSanchez/gestion-expedientes.git](https://github.com/JKevinSanchez/gestion-expedientes.git)
    cd gestion-expedientes
    ```
2. **Preparar el entorno operativo**
    * El sistema automatizado de *bootstrap* creará los directorios necesarios al iniciar:
        * `data/` (Para el almacenamiento del archivo maestro).
        * `logs/` (Para el registro técnico de excepciones).
3. **Generar datos de prueba (Opcional)**
    * Si deseas poblar la base de datos con registros simulados de forma masiva:
    ```bash
    python generador_datos.py
    ```
4. **Lanzar la aplicación**
    * Para iniciar el bucle interactivo del menú de consola:
    ```bash
    python main.py
    ```

---

##  Formato de los Datos

La persistencia de la información en el fichero plano `data/expedientes.txt` sigue un protocolo estricto de doble delimitación por subniveles:

* **Sintaxis de la línea:**
    * `ID;Nombre;Apellidos;Curso;Asignatura1:Nota1,Asignatura2:Nota2`
* **Ejemplo de registro real:**
    * `1;Alejandro;Garcia;1º ASIR;Programacion:8.5,Redes:7.0`

---

##  Autores

El desarrollo de los diferentes componentes de la aplicación se organizó de forma equitativa entre los integrantes de 1º ASIR:

* **Jacques Kevin Sánchez Guerra**
    
* **Fred Farit Bendezu Hernández**
    
* **Mario López Sánchez**
   