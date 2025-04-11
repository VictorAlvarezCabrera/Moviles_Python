from EjemplarMovil import EjemplarMovil
from MisMoviles import MisMoviles
from datetime import datetime

moviles = [
    EjemplarMovil("Samsung", "Android", 4000, 128, [6, 8], datetime(2021, 5, 10), 10, 5),
    EjemplarMovil("Apple", "iOS", 3000, 64, [4, 6], datetime(2020, 9, 15), 600, 2),
    EjemplarMovil("Xiaomi", "Android", 4500, 256, [8, 12], datetime(2022, 3, 25), 300, 4)
]

coleccion = MisMoviles(moviles)

print(coleccion)

coleccion.insertar(EjemplarMovil("pepe", "paco", 5000, 453, [6, 8], datetime(2026, 5, 2), 1000, 3))
print(coleccion)

coleccion.borrar(1)
print(coleccion)