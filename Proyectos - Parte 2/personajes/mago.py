from personaje import * 

class Mago(Personaje): 
    def __init__(self, nombre="Mago",vida=70, ataque=20, defensa=15, inteligencia=15, agilidad=30, fuerza=60 ):
        super().__init__(nombre,vida, ataque, defensa, inteligencia, agilidad, fuerza )
        self.armas = {"Varita magica":42, "Lanzar fuego":25};
        
    def calcular_danio(self, arma_seleccionada):
        danio_comun = super().calcular_danio(arma_seleccionada)
        #Mago : (influye su inteligencia + su ataque base + ataque del arma)
        return self.inteligencia +  danio_comun    