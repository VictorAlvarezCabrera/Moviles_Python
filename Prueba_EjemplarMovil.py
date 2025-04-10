from EjemplarMovil import EjemplarMovil
from datetime import datetime


moviles = [
    EjemplarMovil("Samsung", "Android", 4000, 128, [6, 8], datetime(2021, 5, 10), 700, 4),
    EjemplarMovil("Apple", "iOS", 3000, 64, [4, 6], datetime(2020, 9, 15), 800, 2),
    EjemplarMovil("Xiaomi", "Android", 4500, 256, [8, 12], datetime(2022, 3, 25), 650, 5),
    EjemplarMovil("OnePlus", "Android", 4500, 128, [6, 8], datetime(2021, 8, 1), 750, 1),
    EjemplarMovil("Huawei", "HarmonyOS", 5000, 128, [6, 8], datetime(2020, 12, 10), 600, 3),
    EjemplarMovil("Google", "Android", 3500, 64, [4, 6], datetime(2021, 11, 20), 650, 2)
]

movil1 = moviles[0]

for movil in moviles:
    print(movil,"\n")
    print("8","=" * 30, ">")


print(movil1.mostrar_estado())