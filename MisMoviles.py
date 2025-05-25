from datetime import datetime
from EjemplarMovil import EjemplarMovil

class MisMoviles:
    def __init__(self, coleccion: list[EjemplarMovil]):
        self.coleccion = coleccion


    def __str__(self):
        resultado = ""

        for i, movil in enumerate(self.coleccion):
            # Convierte la lista de ram en str
            ram = " - ".join(f"{x}GB" for x in movil.ram)
            resultado += f"[{i +1 }] {movil.marca} -- Almacenamiento: {movil.almacenamiento}GB -- RAM: {ram} -- {movil.precio}€ -- {movil.mostrar_estado()}\n"
        return resultado
    

    def insertar(self, objeto: EjemplarMovil):
        
        self.coleccion.append(objeto)
        return self.coleccion
    

    def borrar(self, pos):
        self.coleccion.pop(pos)


    def mostrar(self, pos):
        return self.coleccion[pos]
    
    def guardar_en_csv(self, ruta_fichero: str):
        try:
            with open(ruta_fichero, "w", encoding="utf-8") as f:

                f.write("Marca,Sistema operativo,Batería,Almacenamiento,RAM,Fecha de fabricación,Precio,Estado\n")

                for movil in self.coleccion:
                    f.write(movil.to_csv() + "\n")

            print("Colección guardada correctamente en el archivo CSV.💾")
        except Exception as e:
            print(f"[ERROR]: No se pudo guardar la colección en el archivo CSV: {e}")