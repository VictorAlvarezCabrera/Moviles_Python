from Movil import Movil
from datetime import datetime

class EjemplarMovil(Movil):

    def __init__(self, marca: str, sistema_operativo: str, bateria: int, almacenamiento: int, ram: list, fecha_fabricacion: datetime, precio: int, estado: int):
        super().__init__(marca, sistema_operativo, bateria, almacenamiento, ram, fecha_fabricacion)

        if precio < 0:
            self.precio = 0
        else:
            self.precio = precio
        
        if estado < 1:
            self.estado = 1
        elif estado > 5:
            self.estado = 5
        else:
            self.estado = estado

    
    def mostrar_estado(self) -> str:
        if self.estado == 1:
            return "Roto"
        elif self.estado == 2:
            return "Muy gastado"
        elif self.estado == 3:
            return "Desgastado"
        elif self.estado == 4:
            return "Casi nuevo"
        elif self.estado == 5:
            return "Nuevo"
        

    def __eq__(self, other):
        if isinstance(other, EjemplarMovil):
            return self.marca == other.marca
        return False


    def __gt__(self, other):
        return self.bateria > other.bateria
    

    def __ge__(self, other):
        return self.bateria >= other.bateria
    

    def __lt__(self, other):
        return self.bateria < other.bateria
    

    def __le__(self, other):
        return self.bateria <= other.bateria
    

    def __str__(self):
        return super().__str__() + (
            f"[7] 💲 Precio: {self.precio:.2f}€\n"
            f"[8] 💯 Estado: {self.mostrar_estado()}"
        )