import numpy as np
import random


class Tablero:
    """
    Clase que representa el tablero de juego en el juego de hundir la flota.
    """

    def __init__(self, tamaño):
        """
        Constructor de la clase Tablero.

        Args:
            tamaño (int): El tamaño del tablero de juego.

        Returns:
            None

        Raises:
            None
        """

        self.tamaño = tamaño
        self.tablero = np.full((tamaño, tamaño), " ")

    def crear_tablero(self):
        print("  " + " ".join(str(i) for i in range(self.tamaño)))
        for i in range(self.tamaño):
            print(f"{i} {' '.join(self.tablero[i])}")
        return self.tablero


class Barco:
    """
    Clase que representa un barco en el juego de hundir la flota.
    """

    def __init__(self, eslora, tamaño_tablero):
        """
        Constructor de la clase Barco.

        Args:
            eslora (int): La longitud del barco.
            tamaño_tablero (int): El tamaño del tablero de juego.

        Returns:
            None

        Raises:
            None
        """
        self.eslora = eslora
        self.tamaño_tablero = tamaño_tablero
        self.coordenadas = self.crear_barco_random()

    def crear_barco_random(self):
        """Crea las coordenadas de un barco de eslora dada en una posición aleatoria en el tablero.

        Args:
        - eslora (int): longitud del barco.
        - tamaño_tablero (int): tamaño del tablero de juego.

        Returns:
        - coordenadas (List[Tuple[int, int]]): lista de coordenadas que representan la posición del barco en el tablero.
        """
        orientacion = random.choice(["H", "V"])
        if orientacion == "H":
            fila = random.randint(0, self.tamaño_tablero-1)
            columna = random.randint(0, self.tamaño_tablero-self.eslora)
            coordenadas = [(fila, columna+i) for i in range(self.eslora)]
        else:
            fila = random.randint(0, self.tamaño_tablero-self.eslora)
            columna = random.randint(0, self.tamaño_tablero-1)
            coordenadas = [(fila+i, columna) for i in range(self.eslora)]
        return coordenadas

    def colocar_barco(self, coordenadas, tablero):
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


class JuegoHundirFlota:
    """
    Clase que representa el juego Hundir la Flota.
    """

    barcos = []

    def __init__(self, tamaño_tablero, num_barcos, eslora_barcos):
        """
        Constructor de la clase JuegoHundirFlota.

        Args:
            tamaño_tablero (int): El tamaño del tablero de juego.
            num_barcos (int): El número de barcos a colocar en el tablero.
            eslora_barcos (List[int]): Una lista que contiene las esloras de los barcos a colocar.

        Returns:
            None

        Raises:
            None
        """

        self.tamaño_tablero = tamaño_tablero
        self.num_barcos = num_barcos
        self.eslora_barcos = eslora_barcos
        self.barcos = []

    def crear_tablero(self, tamaño_tablero):
        """
        Crea y muestra el tablero en la consola.

        Args:
            tamaño_tablero (int): El tamaño del tablero de juego.

        Returns:
            tablero (np.ndarray): La matriz que representa el tablero.

        Raises:
            None
        """
        self.tamaño_tablero = tamaño_tablero
        self.tablero = np.full((tamaño_tablero, tamaño_tablero), " ")

        print("  " + " ".join(str(i) for i in range(self.tamaño_tablero)))
        for i in range(self.tamaño_tablero):
            print(f"{i} {' '.join(self.tablero[i])}")
        return self.tablero

    def crear_barco_random(self, eslora, tamaño_tablero):
        """
        Crea las coordenadas de un barco de eslora dada en una posición aleatoria en el tablero.

        Args:
        - eslora (int): longitud del barco.
        - tamaño_tablero (int): tamaño del tablero de juego.

        Returns:
        - coordenadas (List[Tuple[int, int]]): lista de coordenadas que representan la posición del barco en el tablero.
        """

        orientacion = np.random.choice(['horizontal', 'vertical'])
        if orientacion == 'horizontal':
            fila = np.random.randint(0, self.tamaño_tablero)
            columna = np.random.randint(0, self.tamaño_tablero - eslora + 1)
            return [(fila, columna+i) for i in range(eslora)]
        else:
            fila = np.random.randint(0, self.tamaño_tablero - eslora + 1)
            columna = np.random.randint(0, self.tamaño_tablero)
            return [(fila+i, columna) for i in range(eslora)]

    def colocar_barco(self, barco, tablero):
        '''
        Coloca el barco en el tablero.

        Args:
        - coordenadas: Una lista de tuplas.
        - tablero: Array que representa el tablero.

        Returns:
        - El tablero actualizado con el barco.
        '''
        for fila, columna in barco:
            tablero[fila][columna] = 'O'
        return tablero

    def disparar(self, casilla, tablero):
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
            for barco in self.barcos:
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

    def jugar(self):
        """
        Inicializa el juego Hundir la flota

        Args:
            tamaño_tablero (int): The size of the game board.
            num_barcos (int): The number of ships to place on the board.
            eslora_barcos (List[int]): A list of the lengths of each ship to be placed on the board.

        Returns:
            None

        Raises:
            None

        """
        print("¡Bienvenido a Hundir la Flota!")

        # Crear tablero vacío
        print("Creando tablero...")
        self.tablero = self.crear_tablero(self.tamaño_tablero)

        # Crear los barcos aleatorios
        print("Desplegando barcos...")
        for eslora in self.eslora_barcos:
            barco = self.crear_barco_random(eslora, self.tamaño_tablero)
            # Comprobar que el barco no se superpone con otros ya creados
            while any(np.array(self.tablero)[[c[0] for c in barco], [c[1] for c in barco]] == "X"):
                barco = self.crear_barco_random(eslora, self.tamaño_tablero)
            self.barcos.append(barco)
            # Colocar barco en el tablero
            self.tablero = self.colocar_barco(barco, self.tablero)

        # Dispara doordenadas en la demo
        print("¡A jugar!")
        num_barcos_hundidos = 0

        while 'O' in self.tablero:
            coordenadas = tuple(
                map(int, input("Dispara en formato fila, columna (ejemplo: 2,5): ").split(",")))
            self.tablero = self.disparar(coordenadas, self.tablero)

            # Verificar si se hundió un barco
            for barco in self.barcos:
                if all(self.tablero[fila][columna] == "X" for fila, columna in barco):
                    num_barcos_hundidos += 1
                    print(
                        f"Hundiste un barco ({num_barcos_hundidos}/{self.num_barcos})!")

            # Mostrar el tablero actualizado
            print("  " + " ".join(str(i) for i in range(self.tamaño_tablero)))
            for i in range(self.tamaño_tablero):
                print(f"{i} {' '.join(self.tablero[i])}")

        print("¡Ganaste!")
