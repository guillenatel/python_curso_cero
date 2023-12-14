import threading; 
import time; 


class Tamagotchi: 
    def __init__(self,nombre):
        self.nombre = nombre;
        self.nivel_energia = 100;
        self.nivel_hambre = 0;
        self.nivel_felicidad = 50; 
        self.humor = "indiferente"
        self.esta_vivo = True;
        
    def mostrar_estado(self): 
        print (f"Tamagotchi: \n-Nombre: {self.nombre} \n-Nivel de energia:{self.nivel_energia}  \n-Nivel de hambre:{self.nivel_hambre} \n-Humor:{self.humor}"); 
    
    def alimentar(self):
        self.nivel_hambre -= 10;
        self.nivel_energia -= 15;  
        if(self.nivel_hambre <= 0): 
            self.nivel_hambre = 0;
        print(f"{self.nombre} ha sido alimentado. Los nuevos niveles son: \n-Nivel de hambre: {self.nivel_hambre} \n-Nivel de energía: {self.nivel_energia}"); 
    
    def jugar(self): 
        self.nivel_felicidad += 20; 
        self.nivel_energia  -= 18; 
        self.nivel_hambre += 10; 
        print(f"{self.nombre} ha jugado. Los nuevos niveles son: \n-Nivel de hambre: {self.nivel_hambre} \n-Nivel de energía: {self.nivel_energia} \n-Nivel de felicidad: {self.nivel_felicidad}"); 
        self.verificar_estado();
    
    def dormir(self): 
        self.nivel_hambre += 5;  
        self.nivel_energia += 40;  
        print (f"{self.nombre} ha dormido. Los nuevos niveles son: \n-Nivel de hambre: {self.nivel_hambre} \n-Nivel de energía: {self.nivel_energia}");
        self.verificar_estado(); 
        
    def verificar_estado(self): 
        if (self.nivel_energia <=0): 
            self.esta_vivo = False;
            print(f"{self.nombre} ha muerto.Lo sentimos mucho, que descanse en paz."); 
        elif(self.nivel_hambre >= 20): 
            self.nivel_energia -= 20; 
            self.nivel_felicidad -= 30; 
            print(f"{self.nombre} esta hambriento.Se pierden puntos de energía y felicidad."); 
            if(self.nivel_energia <=0):
                self.esta_vivo = False; 
                print(f"{self.nombre} ha muerto de hambre.Lo sentimos mucho, que descanse en paz."); 
        elif(self.nivel_felicidad <= 0): 
            self.esta_vivo = False;
            print(f"{self.nombre} ha muerto por falta de felicidad.Lo sentimos mucho, que descanse en paz."); 
            
    def tiempoOcio(self, bandera): 
        while not bandera.is_set() and self.esta_vivo == True:
            self.nivel_energia -= 15; 
            self.nivel_felicidad -=20; 
            self.nivel_hambre += 15; 
            time.sleep(3); 
    




