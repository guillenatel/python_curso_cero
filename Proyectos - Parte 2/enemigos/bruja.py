from enemigo import Enemigo
from random import random, choice


class Bruja(Enemigo):
    def __init__(self, nombre="Bruja Malevola", vida=80, ataque=45, defensa=20, inteligencia=42, agilidad=35, fuerza=5):
        super().__init__(nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza)
        self.armas = {"Volar": 65,"Hechizo":15}
        self.puede_volar = True
        self.armas_esquivables = ["Lanzar fuego"]

    def esquivar_lanzamiento_de_fuego(self, arma_seleccionada):
        # Si puede volar y el arma seleccionada es "Lanzar fuego", decide si esquiva
        if self.puede_volar and arma_seleccionada == "Lanzar fuego":
            esquiva = choice([True, False])
            if esquiva:
                print(f"{self.nombre} esquiva el lanzamiento de fuego y no recibe daño.")
                return True  # Retorna True indicando que se esquivó el ataque
            
        return False  # Retorna False indicando que no se esquivó el ataque

    def ataqueDelEnemigo(self, objetivo, arma_seleccionada=None):
        # Calcular ataque de la bruja
        danio_infligido = max(0, self.calcular_danio_enemigo() - objetivo.defensa)

        # Si puede volar, intenta esquivar el lanzamiento de fuego
        esquiva_fuego = self.esquivar_lanzamiento_de_fuego(arma_seleccionada)

        if not esquiva_fuego:
            # Si no puede volar o decide no esquivar el fuego, aplica el daño normal
            objetivo.vida -= danio_infligido
            print(f"{self.nombre} ataca a {objetivo.nombre} y causa {danio_infligido} de daño.")

