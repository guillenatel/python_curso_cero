
tablero = [ "-","-","-",
            "-","-","-",
            "-","-","-"
]

ganador = None; 

def controloGanador():
    global ganador; 
    controlHorizontal(); 
    controlvertical(); 
    controlDiagonal(); 
    
    
def controlHorizontal(): 
    global ganador; 
    
    if tablero[0] == tablero[1] == tablero[2] != "-": 
        ganador = tablero[0]; #colocamos la posicion 0 pero puede ser 1 o 2. 
    elif tablero[3] == tablero[4] == tablero[5] != "-": 
        ganador = tablero[3];
    elif tablero[6] == tablero[7] == tablero[8] != "-": 
        ganador = tablero[6];

def controlvertical():
    global ganador; 
    
    if tablero[0] == tablero[3] == tablero[6] != "-": 
        ganador = tablero[0]; 
    elif tablero[1] == tablero[4] == tablero[7] != "-": 
        ganador = tablero[1];
    elif tablero[2] == tablero[5] == tablero[8] != "-": 
        ganador = tablero[2]; 


def controlDiagonal(): 
    global ganador; 
    
    if tablero[0] == tablero[4] == tablero[8] != "-": 
        ganador = tablero[0];  
    elif tablero[2] == tablero[4] == tablero[6] != "-": 
        ganador = tablero[2];



def jugada(valor): 
    
    while True: 
        
        posicion = int(input("Ingrese una posicion del 1 al 9: ")); 
        posicion = posicion - 1; #restamos una posicion ya que se debe tener en cuenta que para recorrer la lista es de 0 a 8
        
        #verificamos si la posicion esta ocupada o no
        if(tablero[posicion]== "-"): 
            #asignamos el valor a la posicion ingresada
            tablero[posicion] = valor;
            break; 
        else: 
            print("Esta posición ya esta ocupada"); 
            
    ver_tablero();

def ver_tablero (): 
    print();
    print(tablero[0] + " | " + tablero[1] + " | " + tablero[2] + "        1 | 2 | 3"); 
    print(tablero[3] + " | " + tablero[4] + " | " + tablero[5] + "        4 | 5 | 6"); 
    print(tablero[6] + " | " + tablero[7] + " | " + tablero[8] + "        7 | 8 | 9"); 
    print();


def jugar(): 
    global ganador; 
    print("Comienza el juego!"); 
    ver_tablero(); 
    
    #range cantidad de vueltas posibles 
    for i in range(5):
        print("Turno del jugador 1 - X")
        valor = "X"
        jugada(valor)
        controloGanador()

        if ganador == "X":
            print("Felicitaciones jugador 1!! Has GANADO el TA-TE-TI")
            break
        elif i < 4:
            print("Turno del jugador 2 - O")
            valor = "O"
            jugada(valor)
            controloGanador()

            if ganador == "O":
                print("Felicitaciones jugador 2!! Has GANADO el TA-TE-TI")
                break
        else:
            print("Empataron el TA-TE-TI")

jugar(); 
