from enemigo import * 

class SombraSilenciosa(Enemigo): 
    def __init__(self, nombre="Sombra Silenciosa",vida=100, ataque=30, defensa=45, inteligencia=5, agilidad=65, fuerza=25):
        super().__init__(nombre,vida, ataque, defensa, inteligencia, agilidad, fuerza)
        self.armas = {"Daga de las Sombras": 45,"Arco  venenoso":35}
        self.armas_esquivables = []  

    def puede_esquivar(self, arma_seleccionada):
        return self.armas_esquivables is None or arma_seleccionada in self.armas_esquivables
        
    def calcular_danio_enemigo(self):
        danio_comun =  super().calcular_danio_enemigo()
        return self.agilidad + danio_comun; 