class tamagotchi: 
    def __init__(self,nombre,nivel_energia,nivel_hambre,nivel_felicidad,humor,esta_vivo):
        self.nombre = nombre
        self.nivel_energia = nivel_energia
        self.nivel_hambre = nivel_hambre
        self.nivel_felicidad = nivel_felicidad 
        self.humor = humor
        self.esta_vivo = esta_vivo
        
    def mostrar_estado(self): 
        print (f"Tamagotchi: \n-Nombre: {self.nombre} \n-Nivel de energia:{self.nivel_energia}  \n-Nivel de hambre:{self.nivel_hambre} \n-Humor:{self.humor}"); 
    
    def alimentar(self): 
        self.nivel_hambre = self.nivel_hambre - 10; 
        self.nivel_energia = self.nivel_energia - 15; 
        print(f"Luego de alimentarlo sus niveles de hambre y energía cambiaron, los nuevos niveles son: \n-Nivel de hambre: {self.nivel_hambre} \n-Nivel de energía: {self.nivel_energia}"); 
    
    def jugar(self): 
        self.nivel_felicidad = self.nivel_felicidad + 20; 
        self.nivel_energia = self.nivel_energia - 18; 
        self.nivel_hambre = self.nivel_hambre + 10; 
        print(f"Luego de jugar sus niveles de hambre, energía y felicidad cambiaron, los nuevos niveles son: \n-Nivel de hambre: {self.nivel_hambre} \n-Nivel de energía: {self.nivel_energia} \n-Nivel de felicidad: {self.nivel_felicidad}"); 
    
    def dormir(self): 
        self.nivel_hambre = self.nivel_hambre + 5; 
        self.nivel_energia = self.nivel_energia + 40; 
        self.verificar_estado(); 
        
    def verificar_estado(self): 
        pass




