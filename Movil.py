from datetime import datetime

class Movil:

    def __init__ (self, marca: str, sistema_operativo: str, bateria: int, almacenamiento: int, ram: list, fecha_fabricacion: datetime):
        self.marca = marca

        self.sistema_operativo = sistema_operativo
        
        if bateria < 0:
            self.bateria = 0
        else:
            self.bateria = bateria

        if almacenamiento < 0:
            self.almacenamiento = 0
        else:
            self.almacenamiento = almacenamiento
        
        self.ram = ram
        self.fecha_fabricacion = fecha_fabricacion

    def comparar_bateria(self, other):
        if isinstance(other, self):
            if self.bateria > other.bateria:
                return "f{self.modelo} tiene más batería que {other.modelo}"
            elif self.bateria < other.bateria:
                return "f{other.modelo} tiene más batería que {self.modelo}"
            else: 
                return "Las baterías son iguales"


    def __eq__(self, other):
        if isinstance(other, self):
            return self.modelo == other.modelo and self.marca == other.marca
        return False

    def __gt__(self, other):
        return self.ram > other.ram
    

    def __ge__(self, other):
        return self.ram >= other.ram
    

    def __lt__(self, other):
        return self.ram < other.ram
    

    def __le__(self, other):
        return self.ram <= other.ram
    

    def __str__(self):
        return(
            "marca: ", self.marca, "\n"
            "sistema operativo: ", self.sistema_operativo, "\n"
            "bateria: ", self.bateria, "\n"
            "almacenamiento: ", self.almacenamiento, "\n"
            "memoria ram: ", self.ram, "\n"
            "fecha de lanzamiento: ", self.ram, "\n"
            "memoria ram: ", self.fecha_fabricacion,"\n"
        )