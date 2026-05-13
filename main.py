import utilidades_archivos
import menu

def main():
    """
    Punto de entrada principal de la aplicación.
    Inicializa el entorno y lanza el menú.
    """
    # Inicializar el entorno (carpetas y archivos si no existen)
    utilidades_archivos.inicializar_entorno()
    
    # Iniciar el menú principal interactivo
    try:
        menu.mostrar_menu()
    except KeyboardInterrupt:
        print("\n\nSaliendo del programa de forma segura...")
    except Exception as e:
        utilidades_archivos.registrar_error(f"Error fatal inesperado: {e}")
        print("\nSe ha producido un error fatal. Revisa los logs para más detalles.")

if __name__ == "__main__":
    main()