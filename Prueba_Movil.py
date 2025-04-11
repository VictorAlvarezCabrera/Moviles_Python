from Movil import Movil
from datetime import datetime

movil1 = Movil("Samsung", "Android", 4000, 128, [6, 8], datetime(2021, 5, 10))
movil2 = Movil("Apple", "iOS", 3000, 64, [4, 6], datetime(2020, 9, 15))
movil3 = Movil("Xiaomi", "Android", 4500, 256, [8, 12], datetime(2022, 3, 25))


print(movil1)
print(movil1 == movil2)
print(movil1 == movil3)
print(movil1.comparar_bateria(movil2))
print(movil1.comparar_bateria(movil3))
print(movil1 < movil2)
print(movil1 <= movil1)
print(movil2 > movil1)
print(movil2 >= movil2)

