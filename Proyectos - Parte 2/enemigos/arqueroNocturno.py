from enemigo import * 

class ArqueroNocturno(Enemigo):
    def __init__(self, nombre="Arquero Nocturno",vida=80, ataque=45, defensa=20, inteligencia=42, agilidad=23, fuerza=5 ):
        super().__init__(nombre,vida, ataque, defensa, inteligencia, agilidad, fuerza)
        self.armas = {"Flecha sileciosa": 65,"Arco de la Penumbra":75}
        self.armas_esquivables = [] 

    def puede_esquivar(self, arma_seleccionada):
        return self.armas_esquivables is None or arma_seleccionada in self.armas_esquivables
        
        
    def calcular_danio_enemigo(self):
        danio_comun =  super().calcular_danio_enemigo()
        return self.agilidad + self.inteligencia + danio_comun; 