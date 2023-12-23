from personaje import Personaje
import random

class Enemigo(Personaje):
    def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza):
        super().__init__(nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza)
        self.armas = {}

    def ataqueDelEnemigo(self, objetivo, arma_seleccionada=None):
        # Seleccionar un arma al azar
        arma_seleccionada = random.choice(list(self.armas.keys()))
        
        # Verificar si el arma seleccionada puede esquivarse
        if self.puede_esquivar(arma_seleccionada):
            print(f"{self.nombre} esquiva el ataque y no recibe daño.")
            return

        # Calcular ataque del enemigo
        danio_infligido = max(0, self.calcular_danio_enemigo() - objetivo.defensa)

        # Aplicar daño al objetivo
        objetivo.vida -= danio_infligido
        print(f"{self.nombre} ataca a {objetivo.nombre} y causa {danio_infligido} de daño.")

    def puede_esquivar(self, arma_seleccionada):
        # Verificar si el enemigo puede esquivar el arma seleccionada
        return arma_seleccionada in self.armas_esquivables

    def calcular_danio_enemigo(self):
        # Calcula el daño que realiza el enemigo
        return self.ataque



    