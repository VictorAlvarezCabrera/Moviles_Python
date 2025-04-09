from Movil import Movil
from datetime import datetime

class EjemplarMovil(Movil):

    def __init__(self, marca: str, sistema_operativo: str, bateria: int, almacenamiento: int, ram: list, fecha_fabricacion: datetime, precio: int, estado: int):
        super().__str__()