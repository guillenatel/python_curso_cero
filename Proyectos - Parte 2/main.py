from random import *
from personaje import *
from personajes import Guerrero, Mago, Arquero, Asesino
from enemigo import *
from enemigos import Bruja, ArqueroNocturno, CaballeroOscuro, SombraSilenciosa


def determinar_turno(jugadores, enemigos):
    todos_personajes = jugadores + enemigos
    orden_turno = sorted(todos_personajes, key=lambda personaje: personaje.agilidad, reverse=True)
    return orden_turno


def mostrar_opciones_armas(jugador):
    print(f"\nOpciones de armas para {jugador.nombre}:")
    for i, arma in enumerate(jugador.armas.keys(), start=1):
        print(f"{i}. {arma}")
    while True:
        try:
            seleccion = int(input("Seleccione el número de su arma: "))
            if 1 <= seleccion <= len(jugador.armas):
                return list(jugador.armas.keys())[seleccion - 1]
            else:
                print("Número no válido. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Intente nuevamente.")


def seleccionar_clase():
    print("\nSeleccione su clase:")
    print("1. Guerrero")
    print("2. Mago")
    print("3. Arquero")
    print("4. Asesino")

    while True:
        try:
            seleccion = int(input("Ingrese el número de su clase: "))
            if 1 <= seleccion <= 4:
                return seleccion
            else:
                print("Número no válido. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Intente nuevamente.")


def juego():
    # Crear instancias de jugador y enemigos
    clase_seleccionada = seleccionar_clase()

    if clase_seleccionada == 1:
        jugador = Guerrero()
        enemigo = CaballeroOscuro()
    elif clase_seleccionada == 2:
        jugador = Mago()
        enemigo = Bruja()
    elif clase_seleccionada == 3:
        jugador = Arquero()
        enemigo = ArqueroNocturno()
    elif clase_seleccionada == 4:
        jugador = Asesino()
        enemigo = SombraSilenciosa()

    jugadores = [jugador]
    enemigos = [enemigo]

    puntuacion_jugador = 0
    puntuacion_enemigo = 0

    for encuentro in range(4):
        print(f"\n----- Encuentro {encuentro + 1} -----")

        # Reiniciamos la vida de ambos personajes para el próximo encuentro
        jugador.vida = 100
        enemigo.vida = 100

        # Definir arma_seleccionada fuera del bucle
        arma_seleccionada = None

        while True:
            orden_turno = determinar_turno(jugadores, enemigos)

            for personaje in orden_turno:
                if personaje in jugadores:
                    print(f"\nTurno de {personaje.nombre} (Jugador)")
                    print(f"Vida de {personaje.nombre}: {personaje.vida}")
                    if personaje.vida <= 0:
                        print("¡HAS MUERTO! Tu personaje ha quedado sin vida.")
                        puntuacion_enemigo += 1  # Incrementa la puntuación del enemigo
                        break  # Termina el encuentro si el jugador ha perdido
                    # Asignar el valor de arma_seleccionada dentro del bucle
                    arma_seleccionada = mostrar_opciones_armas(personaje)
                    danio_infligido = personaje.atacar(arma_seleccionada, enemigo)
                    if enemigo.vida <= 0 and danio_infligido > 0:
                        puntuacion_jugador += 1
                        print(f"{jugador.nombre} ha derrotado a {enemigo.nombre}. ¡Punto para {jugador.nombre}!")
                        break  # Termina el encuentro si el jugador mata al enemigo
                else:
                    # Aquí, pasamos el arma seleccionada (que puede ser usada para decidir si la bruja esquiva o no)
                    personaje.ataqueDelEnemigo(jugador, arma_seleccionada)

                    if jugador.vida <= 0:
                        print("¡HAS MUERT0! Tu personaje ha quedado sin vida.")
                        puntuacion_enemigo += 1  # Incrementa la puntuación del enemigo
                        break  # Termina el encuentro si el jugador ha perdido

            if jugador.vida <= 0 or enemigo.vida <= 0:
                break  # Si uno de los personajes ha perdido, termina el encuentro

        print(f"\n----- Fin del Encuentro {encuentro + 1} -----")
        print(f"Puntuación actual:")
        print(f"{jugador.nombre}: {puntuacion_jugador} puntos")
        print(f"{enemigo.nombre}: {puntuacion_enemigo} puntos")

    print("\n----- Fin de los Encuentros -----")
    print(f"Puntuación final:")
    print(f"{jugador.nombre}: {puntuacion_jugador} puntos")
    print(f"{enemigo.nombre}: {puntuacion_enemigo} puntos")

    if puntuacion_jugador > puntuacion_enemigo:
        print(f"\n¡Felicidades! Has ganado la partida.")
    elif puntuacion_enemigo > puntuacion_jugador:
        print(f"\n¡Lo siento! Has perdido la partida.")
    else:
        print(f"\n¡Es un empate!")


if __name__ == "__main__":
    juego()






# lógica implementada en el juego:

# Inicio del juego:
# El jugador elige una clase al principio del juego (Guerrero, Mago, Arquero, Asesino).
# Según la elección del jugador, se instancia un objeto de la clase correspondiente con estadísticas base.

#Encuentros:
#Hay un total de 4 encuentros en el juego (for encuentro in range(4)).
#En cada encuentro, se reinician las vidas de ambos jugadores (jugador y enemigo) para empezar con 100 de vida.
#Se determina el orden de turno entre jugadores y enemigos según la agilidad de cada personaje.

#Turnos:
#En cada turno, un personaje (jugador o enemigo) realiza acciones.
#Si el personaje es un jugador, se muestra la información sobre su turno y se le permite elegir un arma.
#El jugador ataca al enemigo con el arma seleccionada. Si el enemigo queda sin vida, el jugador gana el encuentro y se rompe el bucle del encuentro. 
#Si el jugador queda sin vida, se rompe el bucle del encuentro, y se muestra que el jugador ha perdido.

# Fin del encuentro:
#Se muestra la puntuación actual después de cada encuentro.
#Se acumulan los puntos de los encuentros ganados por el jugador y el enemigo.

#Fin del juego:
#Después de los 4 encuentros, se muestra la puntuación final.
#Si la puntuación del jugador es mayor que la del enemigo, el jugador gana la partida.
#Si la puntuación del enemigo es mayor que la del jugador, el jugador pierde la partida.
#Si ambos tienen la misma puntuación, es un empate.

#La lógica del juego se basa en las interacciones entre los jugadores y los enemigos durante los encuentros. 
#La victoria o derrota en cada encuentro se determina por la cantidad de puntos acumulados. 
#Las estadísticas base de los personajes, como la agilidad, ataque, defensa, etc., influyen en las posibilidades de éxito durante los combates.
#Además, se han implementado mecánicas específicas para ciertos personajes, como la capacidad de la bruja para esquivar ciertos ataques.


