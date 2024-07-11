from enum import Enum, auto

class TipoEntrada(Enum):
    BEBE = 0
    NIÑO = 14
    ADULTO = 23
    JUBILADO = 18


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
        #self.tipos_entrada = {
            #TipoEntrada.BEBE: {"CANT": 0, "PRECIO": 0},
            #TipoEntrada.NIÑO: {"CANT": 0, "PRECIO": 14},
            #TipoEntrada.ADULTO: {"CANT": 0, "PRECIO": 23},
            #TipoEntrada.JUBILADO: {"CANT": 0, "PRECIO": 18}
        #}    
    
    
        self.tipos_entrada = {}

        for tipo in TipoEntrada:
            self.tipos_entrada[tipo] = {"CANT": 0, "PRECIO": tipo.value}
        """
        podemos usar "comprehension" 
        self.tipos_entrada = {tipo: {"CANT": 0, "PRECIO": tipo.value} for tipo in TipoEntrada}
        """
                                   

    def agregar_entrada(self, edad: int):
                
        nueva_entrada = Entrada(edad)
        self.total += nueva_entrada.precio
        self.num_entradas += 1
        self.tipos_entrada[nueva_entrada.tipo]["CANT"] += 1
        #self.crear_dic(nueva_entrada.tipo)["CANT"] += 1

    def cant_entradas_tipo(self, tipo: TipoEntrada):
        return self.tipos_entrada[tipo]["CANT"] #self.crear_dic(tipo)["CANT"] 
    
    def subtotal_tipo (self, tipo: TipoEntrada):        
        return self.cant_entradas_tipo(tipo) * self.tipos_entrada[tipo]["PRECIO"] #self.crear_dic(tipo)["PRECIO"]