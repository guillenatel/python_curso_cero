class Personaje:
    def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.inteligencia = inteligencia
        self.agilidad = agilidad
        self.fuerza = fuerza
        self.armas = {} 

    def atacar(self, arma_seleccionada, enemigo):
        
        if arma_seleccionada in self.armas:
            
            danio_total = self.calcular_danio(arma_seleccionada)

            # Para calcular el daño infligido, se tiene en cuenta la defensa del enemigo
            danio_infligido = max(0, danio_total - enemigo.defensa)

            if arma_seleccionada != "Lanzar fuego":
                print(f"{self.nombre} ataca con {arma_seleccionada} y causa {danio_infligido} de daño a {enemigo.nombre}.")
                enemigo.vida -= danio_infligido

            if enemigo.vida <= 0:
                print(f"{enemigo.nombre} ha sido derrotado.")
            return danio_infligido
        else:
            print("Arma no válida.")
            return 0

    def calcular_danio(self, arma_seleccionada):
        # Calcular el daño según cada personaje
        return self.ataque + self.armas.get(arma_seleccionada, 0)

