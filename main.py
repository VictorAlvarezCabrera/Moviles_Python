from EjemplarMovil import EjemplarMovil
from MisMoviles import MisMoviles
from datetime import datetime


def cambiar_atributo(lista_moviles: list, opcion: int, atributo: int) -> list:
    movil = lista_moviles[int(opcion) - 1]
    
    if atributo == 1:
        nueva_marca = input("Inserta una nueva marca: ")
        movil.marca = nueva_marca
    elif atributo == 2:
        nuevo_so = input("Inserta un nuevo sistema operativo: ")
        movil.sistema_operativo = nuevo_so
    elif atributo == 3:
        nueva_bateria = int(input("Inserta nueva capacidad de batería: "))
        movil.bateria = nueva_bateria
    elif atributo == 4:
        nuevo_almacenamiento = int(input("Inserta nuevo almacenamiento: "))
        movil.almacenamiento = nuevo_almacenamiento
    elif atributo == 5:
        nueva_ram = input("Inserta nueva RAM (separa por comas y espacio): ")
        movil.ram = [int(r) for r in nueva_ram.split(", ")]
    elif atributo == 6:
        nueva_fecha_str = input("Inserta nueva fecha de fabricación (formato dia/mes/año): ")
        movil.fecha_fabricacion = datetime.strptime(nueva_fecha_str, "%d/%m/%Y")
    elif atributo == 7:
        nuevo_precio = round(float(input("Inserta nuevo precio: ")), 2)
        movil.precio = nuevo_precio
    elif atributo == 8:
        nuevo_estado = int(input("Inserta nuevo estado (1 a 5): "))
        movil.estado = nuevo_estado


def ordenar(moviles: list) -> list:
    moviles2 = []
    moviles2 = moviles.copy()
    lista_ordenada = []
    while moviles2:
        mayor_precio = moviles2[0].precio
        movil = moviles2[0]
        for i, m in enumerate(moviles2):
            if m.precio > mayor_precio:
                mayor_precio = moviles2[i].precio
                movil = m
        lista_ordenada.append(movil)
        moviles2.remove(movil)
    return lista_ordenada

moviles = [
    EjemplarMovil("Samsung", "Android", 4000, 128, [6, 8], datetime(2021, 5, 10), 10, 5),
    EjemplarMovil("Apple", "iOS", 3000, 64, [4, 6], datetime(2020, 9, 15), 600, 2),
    EjemplarMovil("Xiaomi", "Android", 4500, 256, [8, 12], datetime(2022, 3, 25), 300, 4),
    EjemplarMovil("OnePlus", "Android", 5000, 128, [8, 12], datetime(2023, 1, 5), 350, 4),
    EjemplarMovil("Huawei", "HarmonyOS", 4100, 128, [6], datetime(2021, 11, 20), 250, 3),
    EjemplarMovil("Google", "Android", 4080, 128, [6, 8], datetime(2022, 10, 13), 500, 5),
    EjemplarMovil("Realme", "Android", 4300, 64, [4, 6], datetime(2020, 6, 9), 180, 2),
    EjemplarMovil("Motorola", "Android", 4000, 128, [4], datetime(2019, 8, 21), 150, 1),
    EjemplarMovil("Sony", "Android", 4500, 256, [6, 8], datetime(2023, 4, 18), 600, 5),
    EjemplarMovil("Nokia", "Android", 3000, 32, [3], datetime(2018, 2, 28), 90, 1)
]

coleccion = MisMoviles(moviles)
while True:
    print("\n- Colección de móviles:\n")
    print(coleccion)

    print("==="*30)
    print("¿Qué deseas hacer?\n")
    print("[A]ñadir")
    print("[O]ordenar (por precio)")
    print("[S]alir")
    
    print("==="*30)
    opcion = input()
    print("==="*30)

    if opcion.upper() == "S":
        print("Saliendo del sistema...💀")
        break
    
    if opcion.upper() == "A":
        marca = input("Marca: ")
        sistema_operativo = input("\nSistema operativo: ")
        bateria = int(input("\nBatería: "))
        almacenamiento = int(input("\nAlmacenamiento: "))
        # Coger la ram a traves de comas
        ram = input("\nRam (Separa por comas y espacio Ejemplo -> 8, 12): ")
        lista_ram = ram.split(", ")
        # Transformamos la ram de str a int
        lista_ram = [int(r) for r in lista_ram]
        # Coger la fecha en str
        fecha_fabricacion_str = input("\nFecha de fabricación (formato dia/mes/año): ")
        # Transformarla a datetime
        fecha_fabricacion = datetime.strptime(fecha_fabricacion_str, "%d/%m/%Y")
        precio = round(float(input("\nPrecio: ")), 2)
        estado = int(input("\nEstado (1 a 5): "))

        # Creamos el objeto
        objeto = EjemplarMovil(marca, sistema_operativo, bateria, almacenamiento, lista_ram, fecha_fabricacion, precio, estado)

        # Insertamos el objeto
        coleccion.insertar(objeto)
        print("==="*30)
        print("Movil añadido correctamente.")
        input()
    elif opcion.upper() == "O":
        print("## Móviles ordenados de mayor a menor precio:")
        print(MisMoviles(ordenar(moviles)))
        input()


    else:
        if int(opcion) > len(moviles):
            print("[ERROR]: Esa opción no existe.❌")
            input()
        else:
            if int(opcion) >= 1:
                print(coleccion.mostrar(int(opcion ) - 1))
                print("Inserta el número del atributo que desees cmabiar (0 para salir): ")
                atributo_cambiar = int(input())
                if atributo_cambiar == 0:
                    print("No cambiaste ningun atributo.👎")
                    input()
                else:
                    cambiar_atributo(moviles, int(opcion), atributo_cambiar)
            elif int(opcion) <= -1:
                print(f"Vas a proceder a borrar el movil {coleccion.mostrar(int(opcion) - 1).marca} con sistema operativo {coleccion.mostrar(int(opcion) - 1).sistema_operativo}")
                confirmacion = input("¿Está seguro? (S/N): ")

                while confirmacion.upper() != "S" and confirmacion.upper() != "N":
                    confirmacion = input("Es S o N: ")

                if confirmacion.upper() == "S":
                    coleccion.borrar(abs(int(opcion)))

                    print("Móvil eliminado.📵")
                    input()
                elif confirmacion.upper() == "N":
                    print("El Móvil no se ha eliminado.👎")
                    input()