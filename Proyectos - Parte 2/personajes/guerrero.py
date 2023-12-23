from personaje import * 

class Guerrero(Personaje): 
    def __init__(self,nombre="Guerrero", vida=100, ataque=15, defensa=20, inteligencia=10, agilidad=25, fuerza=60):
        super().__init__(nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza)
        self.armas = {"Espada":35, "Hacha":50}
    
    
    def calcular_danio(self, arma_seleccionada):
        danio_comun = super().calcular_danio(arma_seleccionada)
        #Guerrero: (influye su fuerza + su ataque base + ataque del arma)
        return self.fuerza + danio_comun            
            



