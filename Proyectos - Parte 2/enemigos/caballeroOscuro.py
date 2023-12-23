from enemigo import * 

class CaballeroOscuro(Enemigo): 
    def __init__(self, nombre="Caballero Oscuro",vida=80, ataque=45, defensa=50, inteligencia=15, agilidad=15, fuerza=45 ):
        super().__init__(nombre,vida, ataque, defensa, inteligencia, agilidad, fuerza)
        self.armas = {"Espada Pesada": 45,"Escudo":35}
        self.armas_esquivables = []  

    def puede_esquivar(self, arma_seleccionada):
        return self.armas_esquivables is None or arma_seleccionada in self.armas_esquivables
        
    
    def calcular_danio_enemigo(self):
        danio_comun =  super().calcular_danio_enemigo()
        return self.fuerza + danio_comun; 