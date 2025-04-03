from datetime import datetime

class ModeloMovil:

    def __init__ (self, marca: str, modelo: str, anio_lanzamiento: int, sistema_operativo: str, bateria: int, almacenamiento: int, ram: int, precio: float):
        self.marca = marca
        self.modelo = modelo

        if anio_lanzamiento < 1973:
            self.anio_lanzamiento = 1973
        elif anio_lanzamiento > datetime.now().year:
            self.anio_lanzamiento = datetime.now().year
        
        self.sistema_operativo = sistema_operativo
        
        if bateria < 0:
            self.bateria = 0
        else:
            self.bateria = bateria

        if almacenamiento < 0:
            self.almacenamiento = 0
        else:
            self.almacenamiento = almacenamiento
        
        if ram < 0:
            self.ram = 0
        else:
            self.ram = ram
