from EjemplarMovil import EjemplarMovil
from datetime import datetime

movil1 = EjemplarMovil("Samsung", "Android", 4000, 128, [6, 8], datetime(2021, 5, 10), 10, 5)
movil2 = EjemplarMovil("Apple", "iOS", 3000, 64, [4, 6], datetime(2020, 9, 15), 600, 2)
movil3 = EjemplarMovil("Xiaomi", "Android", 4500, 256, [8, 12], datetime(2022, 3, 25), 300, 4)


print(movil1)
print(movil1 == movil2)
print(movil1 == movil3)
print(movil1.mostrar_estado())
print(movil1.mostrar_estado())
print(movil1 < movil2)
print(movil1 <= movil1)
print(movil2 > movil1)
print(movil2 >= movil2)

