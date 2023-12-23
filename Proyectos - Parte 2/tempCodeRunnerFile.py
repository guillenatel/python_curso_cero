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
