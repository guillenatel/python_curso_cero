from tamagotchiEjer1 import *

# ------------Ejercicio Tamagotchi------------

primer_tamagotchi = Tamagotchi(input(f"Ingrese el nombre de su tamagotchi: "));  

def menu (): 
    menu_tamagotchi = """
--------Menú principal--------
1 - Alimentar.
2 - Juagr.
3 - Dormir.
4 - Mostrar estado actual.
5 - Salir.
"""
    print(menu_tamagotchi); 
    
opcion = 0; 
bandera = threading.Event(); 
hilo = threading.Thread(target=primer_tamagotchi.tiempoOcio,args=(bandera, )); 
hilo.start(); 

while opcion != 5: 
    menu (); 
    
    try:
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("Por favor, ingrese un número entero.")
        continue
    
    if  opcion == 1: 
        primer_tamagotchi.alimentar();  
    elif opcion == 2: 
        primer_tamagotchi.jugar();  
    elif opcion == 3: 
        primer_tamagotchi.dormir();  
    elif opcion == 4: 
        primer_tamagotchi.mostrar_estado();  
    elif opcion == 5:
        bandera.set(); 
        hilo.join(); 
        print("Saliendo del programa."); 
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")


