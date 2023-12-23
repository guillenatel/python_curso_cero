from personaje import * 

class Arquero(Personaje): 
    def __init__(self, nombre="Arquero", vida=90, ataque=18, defensa=8, inteligencia=20, agilidad=55, fuerza=10):
        super().__init__(nombre,vida, ataque, defensa, inteligencia, agilidad, fuerza)
        self.armas = {"Flecha comun":25, "Flecha con veneno":45} 
        
    def actualizar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def calcular_danio(self, arma_seleccionada):
        danio_comun = super().calcular_danio(arma_seleccionada)
        #Arquero : (influye su agilidad + su ataque base + ataque del arma)
        return self.agilidad +  danio_comun    