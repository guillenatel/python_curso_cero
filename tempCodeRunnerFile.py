import threading
import time

def hola(bandera): 
    while not bandera.is_set():
        print("Ejecucion en segundo plano ...", end="\r"); 
        time.sleep(3) #durante tres segundos.
        
bandera = threading.Event()
hilo = threading.Thread(target=hola,args=(bandera, )); 


hilo.start(); 

while True: 
    print("\n"); 
    entrada = input(" PRESIONE UNA TECLA PARA DETENER LA EJECUCIÓN"); 
    if entrada:
        bandera.set(); 
        hilo.join();  
        break; 