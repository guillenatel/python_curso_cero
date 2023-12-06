from libro import *
from biblioteca import *

#--------------Sistema Bibliotecas--------------------

opcion_principal = 0
opcion_biblioteca_accion = 0
biblioteca_nacional = biblioteca();
biblioteca_ateneo = biblioteca();
biblioteca_seleccionada = None


def mostrar_menu (): 
    menu_principal = """
-------Menú Principal------- 
1 - Seleccionar biblioteca.
2 - Crear nueva biblioteca desde JSON.
3 - Salir.
"""
    print(menu_principal); 
    
def mostrar_menu_biblioteca (): 
    biblioteca_menu = """ 
-------Menú de Biblioteca-------
1 - Agregar libro.
2 - Eliminar libro.
3 - Mostrar libros disponibles.
4 - Guardar biblioteca en JSON.
5 - Volver al Menú Principal.
"""
    print(biblioteca_menu);



while opcion_principal != 3:
    mostrar_menu();

    try:
        opcion_principal = int(input("Ingrese una opción: "))
    except ValueError:
        print("Por favor, ingrese un número entero.")
        continue

    if opcion_principal == 1:
        # Seleccionar Biblioteca
        print("\nSeleccione una biblioteca:")
        print("1 - Biblioteca Nacional")
        print("2 - Biblioteca Ateneo")

        try:
            opcion_biblioteca = int(input("Ingrese una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero.")
            continue

        if opcion_biblioteca == 1:
            biblioteca_seleccionada = biblioteca_nacional
            print("Biblioteca Nacional seleccionada.")
        elif opcion_biblioteca == 2:
            biblioteca_seleccionada = biblioteca_ateneo
            print("Biblioteca Ateneo seleccionada.")
        else:
            print("Opción no válida. Volviendo al Menú Principal.")

        while opcion_biblioteca_accion != 5:
            mostrar_menu_biblioteca()

            try:
                opcion_biblioteca_accion = int(input("Ingrese una opción: "))
            except ValueError:
                print("Por favor, ingrese un número entero.")
                continue

            if opcion_biblioteca_accion == 1:
                # Agregar Libro
                nuevo_libro = libro(
                    input("Ingrese el título: "),
                    input("Ingrese el autor: "),
                    input("Ingrese el año de publicación: "),
                    int(input("Ingrese la cantidad de unidades del libro: "))
                )
                biblioteca_seleccionada.agregar_libro(nuevo_libro);

            elif opcion_biblioteca_accion == 2:
                # Eliminar Libro
                titulo = input("Ingrese el título del libro a eliminar: ")
                biblioteca_seleccionada.eliminar_libro(titulo);

            elif opcion_biblioteca_accion == 3:
                # Mostrar Libros Disponibles
                biblioteca_seleccionada.libros_disponibles();

            elif opcion_biblioteca_accion == 4:
                # Guardar Biblioteca en JSON
                archivo_json = input("Ingrese el nombre del archivo JSON: ")
                biblioteca_seleccionada.guardar_en_json(archivo_json)

            elif opcion_biblioteca_accion == 5:
                print("Volviendo al Menú Principal")

            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 5.");

    elif opcion_principal == 2:
        # Crear Nueva Biblioteca desde JSON
        pass

    elif opcion_principal == 3:
        print("Saliendo del programa.")

    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")