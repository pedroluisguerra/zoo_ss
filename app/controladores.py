from app.vistas import VistaEntrada, VistaGrupo
from app.modelos import GrupoEntrada
from simple_screen import DIMENSIONS, cls, locate, Screen_manager, Input

class Zoo:
    # Creamos una clase que gestione la visual de la "app"
    def __init__(self):

        self.grupo_entradas = GrupoEntrada()
        self.x = (DIMENSIONS.w - 37) // 2
        self.vista_grupo = VistaGrupo(self.grupo_entradas, self.x, 1)
        self.entrada_edad = VistaEntrada("EDAD: ", self.x, 10)
        self.entrada_seguir = VistaEntrada("Otra vez (s/n): ", self.x, 12)
    
    def run(self):
        with Screen_manager:
            while True:
                cls()
                self.vista_grupo.paint()
                edad = self.entrada_edad.paint()
                if edad == "":
                    respuesta = self.entrada_seguir.paint()
                    if respuesta.upper() == "S":
                        self.grupo_entradas = GrupoEntrada()
                        self.vista_grupo.grupo = self.grupo_entradas
                        continue
                    else:
                        break 
                try:
                    edad = int(edad)
                    self.grupo_entradas.agregar_entrada(edad)
                except ValueError:
                    print("Por favor, ingrese una edad válida.")
                    continue

            # Final "controlado" del programa
            locate(1, DIMENSIONS.h - 2)
            Input("Pulse enter para salir")

if __name__ == "__main__":
    app_zoo = Zoo()
    app_zoo.inicar()
