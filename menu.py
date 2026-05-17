import config
import gestor_expedientes
import validaciones

def imprimir_cabecera():
    print("\n" + "="*50)
    print(f" GESTIÓN DE EXPEDIENTES ACADÉMICOS ({config.CURSO_ACTUAL}) ".center(50, "="))
    print("="*50)

def solicitar_id(mensaje="Introduce el ID del alumno: "):
    # Bucle infinito hasta que el usuario introduzca un ID con formato correcto
    while True:
        id_str = input(mensaje)
        valido, resultado = validaciones.validar_id(id_str)
        if valido:
            return resultado
        print(f"Error: {resultado}")

def solicitar_texto(mensaje="Introduce el valor: "):
    while True:
        texto = input(mensaje)
        valido, resultado = validaciones.validar_nombre_o_apellidos(texto)
        if valido:
            return resultado
        print(f"Error: {resultado}")

def solicitar_notas():
    notas = {}
    print(f"\n--- Calificaciones para {config.CURSO_ACTUAL} ---")
    print("Deja en blanco si el alumno no está matriculado o no tiene nota aún.")
    for asig in config.ASIGNATURAS_VALIDAS:
        while True:
            nota_str = input(f"Nota para '{asig}': ").strip()
            if not nota_str:
                break # Salta la asignatura actual sin registrar nota
            valido, resultado = validaciones.validar_nota(nota_str)
            if valido:
                notas[asig] = resultado
                break
            print(f"Error: {resultado}")
    return notas

def mostrar_expediente(exp):
    print("\n" + "-"*30)
    print(f"ID: {exp['id']}")
    print(f"Nombre: {exp['nombre']}")
    print(f"Apellidos: {exp['apellidos']}")
    print(f"Curso: {exp['curso']}")
    if exp['notas']:
        print("Calificaciones:")
        for asig, nota in exp['notas'].items():
            print(f"  - {asig}: {nota}")
    else:
        print("Calificaciones: Sin notas registradas.")
    print("-"*30)

def opcion_crear():
    print("\n--- Crear Nuevo Expediente ---")
    nuevo_id = solicitar_id("ID del nuevo expediente: ")
    nombre = solicitar_texto("Nombre del alumno: ")
    apellidos = solicitar_texto("Apellidos del alumno: ")
    
    curso = config.CURSO_ACTUAL
    notas = solicitar_notas()
    
    datos = {
        "id": nuevo_id,
        "nombre": nombre,
        "apellidos": apellidos,
        "curso": curso,
        "notas": notas
    }
    
    try:
        exito, msg = gestor_expedientes.crear_expediente(datos)
        if exito:
            print(f"\n[OK] {msg}")
        else:
            print(f"\n[ERROR] No se pudo crear: {msg}")
    except Exception as e:
        print(f"\n[ERROR DEL SISTEMA] {e}")

def opcion_listar():
    print("\n--- Listado de Expedientes ---")
    try:
        expedientes = gestor_expedientes.leer_expedientes()
        if not expedientes:
            print("No hay expedientes registrados.")
            return
        
        for exp in expedientes:
            mostrar_expediente(exp)
    except Exception as e:
        print(f"\n[ERROR] Al leer los expedientes: {e}")

def opcion_buscar():
    print("\n--- Buscar Expediente ---")
    id_buscar = solicitar_id("ID del expediente a buscar: ")
    try:
        exp = gestor_expedientes.buscar_expediente(id_buscar)
        if exp:
            mostrar_expediente(exp)
        else:
            print("\n[INFO] Expediente no encontrado.")
    except Exception as e:
        print(f"\n[ERROR] Al buscar el expediente: {e}")

def opcion_actualizar():
    print("\n--- Actualizar Expediente ---")
    id_actualizar = solicitar_id("ID del expediente a actualizar: ")
    try:
        exp_actual = gestor_expedientes.buscar_expediente(id_actualizar)
        if not exp_actual:
            print("\n[INFO] Expediente no encontrado.")
            return
            
        print("\nExpediente actual:")
        mostrar_expediente(exp_actual)
        
        print("\nIntroduce los nuevos datos (deja en blanco para mantener el valor actual)")
        nuevo_nombre = input(f"Nombre [{exp_actual['nombre']}]: ").strip()
        if not nuevo_nombre:
            nuevo_nombre = exp_actual['nombre']
        else:
            nuevo_nombre = validaciones.limpiar_texto(nuevo_nombre)
            
        nuevos_apellidos = input(f"Apellidos [{exp_actual['apellidos']}]: ").strip()
        if not nuevos_apellidos:
            nuevos_apellidos = exp_actual['apellidos']
        else:
            nuevos_apellidos = validaciones.limpiar_texto(nuevos_apellidos)
            
        print("\n¿Deseas actualizar las notas? (s/n)")
        actualizar_n = input("Opción: ").strip().lower()
        
        nuevas_notas = exp_actual['notas']
        if actualizar_n == 's':
            nuevas_notas = solicitar_notas()
            
        datos_actualizados = {
            "id": id_actualizar,
            "nombre": nuevo_nombre,
            "apellidos": nuevos_apellidos,
            "curso": config.CURSO_ACTUAL,
            "notas": nuevas_notas
        }
        
        exito, msg = gestor_expedientes.actualizar_expediente(id_actualizar, datos_actualizados)
        if exito:
            print(f"\n[OK] {msg}")
        else:
            print(f"\n[ERROR] No se pudo actualizar: {msg}")
            
    except Exception as e:
        print(f"\n[ERROR] Al actualizar el expediente: {e}")

def opcion_eliminar():
    print("\n--- Eliminar Expediente ---")
    id_eliminar = solicitar_id("ID del expediente a eliminar: ")
    confirmacion = input(f"¿Estás seguro de eliminar el expediente con ID {id_eliminar}? (s/n): ").lower()
    
    if confirmacion == 's':
        try:
            exito, msg = gestor_expedientes.eliminar_expediente(id_eliminar)
            if exito:
                print(f"\n[OK] {msg}")
            else:
                print(f"\n[ERROR] No se pudo eliminar: {msg}")
        except Exception as e:
            print(f"\n[ERROR] Al eliminar el expediente: {e}")
    else:
        print("\nOperación cancelada.")

def mostrar_menu():
    # Bucle principal que mantiene la aplicación abierta hasta pulsar la opción de salida
    while True:
        imprimir_cabecera()
        print("1. Crear nuevo expediente")
        print("2. Listar todos los expedientes")
        print("3. Buscar un expediente")
        print("4. Actualizar un expediente")
        print("5. Eliminar un expediente")
        print("6. Salir")
        
        opcion = input("\nSelecciona una opción (1-6): ").strip()
        
        if opcion == '1':
            opcion_crear()
        elif opcion == '2':
            opcion_listar()
        elif opcion == '3':
            opcion_buscar()
        elif opcion == '4':
            opcion_actualizar()
        elif opcion == '5':
            opcion_eliminar()
        elif opcion == '6':
            print("\n¡Gracias por usar el sistema! Hasta pronto.")
            break
        else:
            print("\n[INFO] Opción no válida. Por favor, selecciona un número del 1 al 6.")