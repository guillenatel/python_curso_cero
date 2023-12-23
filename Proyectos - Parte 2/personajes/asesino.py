from personaje import * 

class Asesino(Personaje): 
    def __init__(self, nombre="Asesino", vida=85, ataque=20, defensa=5, inteligencia=65, agilidad=35, fuerza=15):
        super().__init__(nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza)
        self.armas = {"Cuchillo":45, "Arma de fuego":35};
        
    def actualizar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    
    def calcular_danio(self, arma_seleccionada):
        danio_comun = super().calcular_danio(arma_seleccionada)
        #Asesino : (influye su agilidad e inteligencia + su ataque base + ataque del arma)
        return self.agilidad + self.inteligencia +  danio_comun    