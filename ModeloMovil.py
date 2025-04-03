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
        
        if precio < 0:
            self.precio = 0.0
        else:
            self.precio = float(round(precio, 2))

    def __eq__(self, other):
        if isinstance(other, self):
            return self.modelo == other.modelo and self.marca == other.marca
        return False

    def __str__(self):
        return(
            "marca: ", self.marca, "\n"
            "modelo: ", self.modelo, "\n"
            "año de lanzamiento: ", self.anio_lanzamiento, "\n"
            "sistema operativo: ", self.sistema_operativo, "\n"
            "bateria: ", self.bateria, "\n"
            "almacenamiento: ", self.almacenamiento, "\n"
            "memoria ram: ", self.ram, "\n"
            "precio: ", self.precio, "€\n"

        )