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

moviles = [
    EjemplarMovil("Samsung", "Android", 4000, 128, [6, 8], datetime(2021, 5, 10), 10, 5),
    EjemplarMovil("Apple", "iOS", 3000, 64, [4, 6], datetime(2020, 9, 15), 600, 2),
    EjemplarMovil("Xiaomi", "Android", 4500, 256, [8, 12], datetime(2022, 3, 25), 300, 4)
]

coleccion = MisMoviles(moviles)
while True:
    print(coleccion)

    print("¿Qué deseas hacer?")
    print("[A]ñadir")
    print("[O]ordenar (por precio)")
    print("[S]alir")
    
    opcion = input()

    if opcion.upper() == "S":
        print("Saliendo del sistema...")
        break

    if opcion.upper() == "A":
        marca = input("Marca: ")
        sistema_operativo = input("Sistema operativo: ")
        bateria = int(input("Batería: "))
        almacenamiento = int(input("Almacenamiento: "))
        # Coger la ram a traves de comas
        ram = input("Ram (Separa por comas y espacio Ejemplo -> 8, 12): ")
        lista_ram = ram.split(", ")
        # Transformamos la ram de str a int
        lista_ram = [int(r) for r in lista_ram]
        # Coger la fecha en str
        fecha_fabricacion_str = input("Fecha de fabricación (formato dia/mes/año): ")
        # Transformarla a datetime
        fecha_fabricacion = datetime.strptime(fecha_fabricacion_str, "%d/%m/%Y")
        precio = round(float(input("Precio: ")), 2)
        estado = int(input("Estado (1 a 5): "))

        # Creamos el objeto
        objeto = EjemplarMovil(marca, sistema_operativo, bateria, almacenamiento, lista_ram, fecha_fabricacion, precio, estado)

        # Insertamos el objeto
        coleccion.insertar(objeto)
        
        print("Movil añadido correctamente.")
        input()
    else:
        if int(opcion) > len(moviles):
            print("[ERROR]: Esa opción no existe.")
            input()
        else:
            if int(opcion) >= 1:
                print(coleccion.mostrar(int(opcion)))
                print("Inserta el número del atributo que desees cmabiar (0 para salir): ")
                atributo_cambiar = int(input())
                if atributo_cambiar == 0:
                    print("No cambiaste ningun atributo.")
                    input()
                else:
                    cambiar_atributo(moviles, int(opcion), atributo_cambiar)
            elif int(opcion) <= -1:
                print(f"Vas a proceder a borrar el movil {coleccion.mostrar(int(opcion)).marca} con sistema operativo {coleccion.mostrar(int(opcion)).sistema_operativo}")
                confirmacion = input("¿Está seguro? (S/N): ")

                while confirmacion.upper() != "S" and confirmacion.upper() != "N":
                    confirmacion = input("Es S o N: ")

                if confirmacion.upper() == "S":
                    coleccion.borrar(abs(int(opcion)))

                    print("Móvil eliminado.")
                    input()
                elif confirmacion.upper() == "N":
                    print("El Móvil no se ha eliminado.")
                    input()