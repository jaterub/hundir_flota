from clases import JuegoHundirFlota
import numpy as np
import random
import logging


logging.basicConfig(level=logging.DEBUG)

logging.info('VERSION BETA!! Puedes cambiar los ajustes de la demo!!')


# instancia demo

Hundir_flota = JuegoHundirFlota(10, 4, [1, 2, 3, 4])


# iniciar juego
Hundir_flota.jugar()
