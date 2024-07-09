from enum import Enum, auto

class TipoEntrada(Enum):
    BEBE = auto()
    NIÑO = auto()
    ADULTO = auto()
    JUBILADO = auto()


class Entrada:
    def __init__(self, edad: int):

        if edad < 0:
            raise ValueError("Edad no puede ser menor a 0")
        
        elif edad <= 2:
            self.tipo = TipoEntrada.BEBE
            self.precio = 0
        elif edad < 13:
            self.tipo = TipoEntrada.NIÑO
            self.precio = 14
        elif edad < 65:
            self.tipo = TipoEntrada.ADULTO
            self.precio = 23
        else:
            self.tipo = TipoEntrada.JUBILADO
            self.precio = 18

class GrupoEntrada:
    def __init__(self):
        self.total = 0
        self.num_entradas = 0
        

    def agregar_entrada(self, edad: int):
                
        entrada = Entrada(edad)
        self.total += entrada.precio
        self.num_entradas += 1