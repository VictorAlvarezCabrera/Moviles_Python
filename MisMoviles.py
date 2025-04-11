from datetime import datetime
from EjemplarMovil import EjemplarMovil

class MisMoviles:
    def __init__(self, coleccion: list[EjemplarMovil]):
        self.coleccion = coleccion


    def __str__(self):
        resultado = "Colección de móviles:\n"

        for i, movil in enumerate(self.coleccion):
            # Convierte la lista de ram en str
            ram = " - ".join(f"{x}GB" for x in movil.ram)
            resultado += f"[{i +1 }] {movil.marca} -- RAM: {ram} -- {movil.mostrar_estado()} \n"
        return resultado
    

    def insertar(self, objeto: EjemplarMovil):
        
        self.coleccion.append(objeto)
        return self.coleccion
    

    def borrar(self, pos):
        self.coleccion.pop(pos)


    def mostrar(self, pos):
        return self.coleccion[pos - 1]