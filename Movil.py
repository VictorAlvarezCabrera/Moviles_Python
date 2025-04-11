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
        if isinstance(other, Movil):
            if self.bateria > other.bateria:
                return f"{self.marca} tiene más batería que {other.marca}"
            elif self.bateria < other.bateria:
                return f"{other.marca} tiene más batería que {self.marca}"
            else: 
                return "Las baterías son iguales"


    def __eq__(self, other) -> bool:
        if isinstance(other, Movil):
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
        # Convierte la lista de ram en str
        ram = " - ".join(f"{x}GB" for x in self.ram)
        return(
            f"[1] 📱 Marca: {self.marca}\n"
            f"[2] 🚨 Sistema operativo: {self.sistema_operativo}\n"
            f"[3] 🔋 Bateria: {self.bateria}\n"
            f"[4] 💿 Almacenamiento: {self.almacenamiento}\n"
            f"[5] 💾 Memoria ram: {ram}\n"
            f"[6] 📅 Fecha de lanzamiento: {self.fecha_fabricacion.strftime('%d/%m/%Y')}\n"
        )