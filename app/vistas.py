"""
               1         2         3        
      1234567890123456789012345678901234567
01    TIPO             PU     Q       TOTAL
02    =====================================
03    BEBE (≤2)      0.00    99     9999.99
04    NINO (≤12)    14.00    99     9999.99
05    ADULTO (<65)  23.00    99     9999.99
06    JUBILADO      18.00    99     9999.99
07    -------------------------------------
08                          999    99999.99
09                          
10    EDAD: 
11    CONF:
"""
from modelos import GrupoEntrada, TipoEntrada
from simple_screen import locate, Print, cls, Screen_manager, Input
class VistaGrupo:
    def __init__(self, grupo: GrupoEntrada, x=1, y=1):
        self.grupo = grupo
        self.x = x
        self.y = y

    def paint(self):
        locate(self.x,self.y,"TIPO            PU     CANT      TOTAL")
        locate(self.x,self.y + 1, "======================================")
        for indice,tipo in enumerate(TipoEntrada):
            locate(self.x,self.y + 2 + indice, f"{tipo.name:.<14s}{tipo.value[0]:5.2f}    {self.grupo.cant_entradas_tipo(tipo):2d}      {self.grupo.subtotal_tipo(tipo):7.2f}")
        locate(self.x, self.y + 6, "======================================")
        locate(self.x,self.y + 7, f"                      {self.grupo.num_entradas:3d}     {self.grupo.total:8.2f}")

class VistaEntrada:

    def __init__(self, etiqueta: str, x, y):
        self.etiqueta = etiqueta
        self.y = y
        self.x = x
        self.value = ""

    def paint(self):
        locate(self.x, self.y, self.etiqueta)
        return Input()


print(__name__)

if __name__ == "__main__":
    with Screen_manager:
        grupo = GrupoEntrada()
        grupo.agregar_entrada(2)
        grupo.agregar_entrada(6)
        grupo.agregar_entrada(15)

        vg = VistaGrupo(grupo)

        vedad = VistaEntrada("EDAD: ", 1, 10)

        vg.paint()
        vedad.paint()
        
        Input("Pulsa Enter para acabar")