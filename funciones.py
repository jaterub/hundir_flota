
import numpy as np
import random


def crear_tablero(tamaño):
    '''
    Crea un tablero vacío de tamaño especificado.

    Args:
    tamaño (int): Tamaño del tablero.

    Returns:
    numpy.ndarray: Un arreglo numpy de tamaño (tamaño, tamaño) lleno de cadenas vacías.'''

    # Guarda el tablero en su variable
    tablero = np.full((tamaño, tamaño), " ")
    # Imprime str concatenado del rango del argumento
    print("  " + " ".join(str(i) for i in range(tamaño)))

    # Muesta de indices de las filas tablero
    for i in range(tamaño):
        print(f"{i} {' '.join(tablero[i])}")
    return tablero


def crear_barco_random(eslora, tamaño_tablero):
    """Crea las coordenadas de un barco de eslora dada en una posición aleatoria en el tablero.

    Args:
    - eslora (int): longitud del barco.
    - tamaño_tablero (int): tamaño del tablero de juego.

    Returns:
    - coordenadas (List[Tuple[int, int]]): lista de coordenadas que representan la posición del barco en el tablero.
    """

    # Orienta el barco 'Horizontal' o 'Vertical'
    orientacion = random.choice(["H", "V"])
    if orientacion == "H":
        # Obtiene el valor axis = 0
        fila = random.randint(0, tamaño_tablero-1)
        # Obtiene el valor axis = 1
        columna = random.randint(0, tamaño_tablero-eslora)
        # Genera la primera posicion y la orienta a la derecha en el eje axis = 1
        coordenadas = [(fila, columna+i) for i in range(eslora)]
    else:
        fila = random.randint(0, tamaño_tablero-eslora)
        columna = random.randint(0, tamaño_tablero-1)
        coordenadas = [(fila+i, columna) for i in range(eslora)]
    return coordenadas


def colocar_barco(coordenadas, tablero):
    '''
    Coloca el barco en el tablero.

    Args:
    - coordenadas: Una lista de tuplas.
    - tablero: Array que representa el tablero.

    Returns:
    - El tablero actualizado con el barco.
    '''
    for fila, columna in coordenadas:
        tablero[fila, columna] = "O"
    return tablero


def disparar(casilla, tablero):
    '''
    Realiza un disparo en la casilla indicada del tablero y actualiza su estado.

    Args:
        casilla: Tupla que indica las coordenadas del disparo en el formato (fila, columna).
        tablero: Matriz de NumPy que representa el tablero del juego.

    Returns:
        La matriz de NumPy actualizada que representa el tablero después del disparo.

    '''
    fila, columna = casilla
    if tablero[fila, columna] == "O":
        print("Tocado!")
        tablero[fila, columna] = "X"
        for barco in barcos:
            if all(tablero[fila][columna] == "X" for fila, columna in barco):
                print("Barco hundido!")
                for fila, columna in barco:
                    tablero[fila][columna] = "H"
    elif tablero[fila, columna] == " ":
        print("Agua!")
        tablero[fila, columna] = "·"
    else:
        print("Ya habías disparado ahí!")
    return tablero


# barcos = []

def juego_inicializacion(tamaño_tablero, num_barcos, eslora_barcos):
    print("¡Bienvenido a Hundir la Flota!")

    # Crear tablero vacío
    print("Creando tablero...")
    tablero = crear_tablero(tamaño_tablero)

    # Crear los barcos aleatorios
    print("Demo...Desplegando barcos")
    for eslora in eslora_barcos:
        barco = crear_barco_random(eslora, tamaño_tablero)
        # Comprobar que el barco no se superpone con otros ya creados
        while any(np.array(tablero)[[c[0] for c in barco], [c[1] for c in barco]] == "X"):
            barco = crear_barco_random(eslora, tamaño_tablero)
        barcos.append(barco)
        # Colocar barco en el tablero
        tablero = colocar_barco(barco, tablero)

    # Juego
    print("¡A jugar!")
    num_barcos_hundidos = 0

    while 'O' in tablero:
        coordenadas = tuple(
            map(int, input("Dispara en formato fila, columna (ejemplo: 2,5): ").split(",")))
        tablero = disparar(coordenadas, tablero)

        # Verificar si se hundió un barco
        for barco in barcos:
            if all(tablero[fila][columna] == "X" for fila, columna in barco):
                num_barcos_hundidos += 1
                print(
                    f"Hundiste un barco ({num_barcos_hundidos}/{num_barcos})!")

        # Mostrar el tablero actualizado
        print("  " + " ".join(str(i) for i in range(tamaño_tablero)))
        for i in range(tamaño_tablero):
            print(f"{i} {' '.join(tablero[i])}")

    print("¡Ganaste!")
