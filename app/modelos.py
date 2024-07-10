from enum import Enum, auto

class TipoEntrada(Enum):
    BEBE = auto()
    NIÑO = auto()
    ADULTO = auto()
    JUBILADO = auto()


class Entrada:
    def __init__(self, edad: int):
        
        self.__validate_edad(edad)
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

    def __validate_edad(self, edad):
        if edad < 0:
            raise ValueError("La edad no debe ser un número negativo")
        if edad > 99:
            raise ValueError("La edad no debe ser mayor a 99")

class GrupoEntrada:
    def __init__(self):
        self.total = 0
        self.num_entradas = 0
        self.tipos_entrada = {
            TipoEntrada.BEBE: 0,
            TipoEntrada.NIÑO: 0,
            TipoEntrada.ADULTO: 0,
            TipoEntrada.JUBILADO: 0
        }

    def agregar_entrada(self, edad: int):
                
        nueva_entrada = Entrada(edad)
        self.total += nueva_entrada.precio
        self.num_entradas += 1
        self.tipos_entrada[nueva_entrada.tipo] += 1

    def cant_entradas_tipo(self, tipo: TipoEntrada):
        return self.tipos_entrada[tipo]
