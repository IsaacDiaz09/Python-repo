# Constantes para evitar la modificacion de su valor
from enum import Enum
from math import pi
from math import e


# Pasa que sea una enumeracion debe heredar de Enum del modulo enum
class Numeros(Enum):
    """
    Constantes de los numeros euler y pi
    """
    NUM_E = e
    NUM_PI = pi
