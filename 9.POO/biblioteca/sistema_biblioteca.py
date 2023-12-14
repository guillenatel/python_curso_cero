from libro import *
from biblioteca import *

#--------------Sistema Bibliotecas--------------------

def mostrar_menu_princial (): 
    menu_principal = """
-------Menú Principal------- 
1 - Seleccionar biblioteca.
2 - Crear nueva biblioteca desde JSON.
3 - Salir.
"""
    print(menu_principal); 


def mostrar_menu_biblioteca (bibliotecas): 
    print("-------Bibliotecas disponibles-------")
    for i, biblioteca in enumerate(bibliotecas, start=1):
        print(f"{i}- {biblioteca.nombre}"); 
    print(f"{len(bibliotecas) + 1}. Volver al menú principal"); 


def mostrar_menu_acciones (): 
    acciones_menu = """ 
-------Menú de Acciones-------
1 - Mostrar libros.
2 - Prestar libro.
3 - Devolver libro.
4 - Agregar libro. 
5 - Eliminar libro.
6 - Guardar biblioteca en JSON.
7 - Volver al menú de bibliotecas.
"""
    print(acciones_menu);

# Crear bibliotecas y agregar al menos una al inicio
bibliotecas = [Biblioteca("Biblioteca Ateneo")]

while True: 
    mostrar_menu_princial(); 
    op_principal = input ("Selecciones una opción: ");
    
    if (op_principal == "1"): 
        mostrar_menu_biblioteca(bibliotecas);
        op_biblioteca = input("Seleccione una biblioteca o vuelva al menú principal: "); 
        
        if(op_biblioteca.isdigit() and 1 <= int(op_biblioteca) <= len(bibliotecas)): 
            biblioteca_actual = bibliotecas[int(op_biblioteca) - 1]; 
            
            while True: 
                mostrar_menu_acciones(); 
                op_acciones = input("Seleccione una acción: ");
                
                if (op_acciones == "1"):
                    biblioteca_actual.mostrar_libros(); 
                elif(op_acciones == "2"): 
                    titulo = input("Ingrese el título del libro que desea prestar: ")
                    biblioteca_actual.prestar_libro(titulo); 
                elif(op_acciones == "3"):
                    titulo = input("Ingrese el título del libro que desea devolver: ")     
                    biblioteca_actual.devolver_libro(titulo); 
                elif(op_acciones == "4"):
                    nuevo_libro = Libro(
                        input("Ingrese el título: "),
                        input("Ingrese el autor: "),
                        input("Ingrese el año de publicación: "),
                        int(input("Ingrese la cantidad de unidades del libro: "))
                    ); 
                    biblioteca_actual.agregar_libro(nuevo_libro); 
                elif(op_acciones == "5"):
                    titulo = input("Ingrese el título del libro que desea eliminar: ")
                    biblioteca_actual.eliminar_libro(titulo); 
                elif(op_acciones == "6"):
                    nom_archivo = input("Ingrese el nombre del archivo JSON para guardar la biblioteca: "); 
                    nom_archivo_result = nom_archivo if nom_archivo.endswith(".json") else nom_archivo + ".json"; 
                    biblioteca_actual.guardar_en_json(nom_archivo_result); 
                elif(op_acciones == "7"):
                    break; 
                else: 
                    print("Opción no válida. Intente de nuevo."); 
                
        elif op_biblioteca.isdigit() and int(op_biblioteca) == len(bibliotecas) + 1:
                continue
        else:
            print("Opción no válida. Intente de nuevo.")
    
    elif (op_principal == "2"): 
        nom_archivo = input("Ingrese el nombre del archivo JSON para cargar la biblioteca: ");
        nom_archivo_result = nom_archivo if nom_archivo.endswith(".json") else nom_archivo + ".json"; 
        nueva_biblioteca = Biblioteca.cargar_desde_json(nom_archivo_result);
        bibliotecas.append(nueva_biblioteca);
        print(f"Biblioteca '{nueva_biblioteca.nombre}' agregada a las bibliotecas disponibles.");
        
    elif op_principal == '3':
        break

    else:
        print("Opción no válida. Intente de nuevo.")
        