from EjemplarMovil import EjemplarMovil
from MisMoviles import MisMoviles
from datetime import datetime

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
        if int(opcion) > len(moviles) or int(opcion) < 1:
            print("[ERROR]: Esa opción no existe.")
            input()
        else:
            print(coleccion.mostrar(int(opcion)))
            print("Inserta el número del atributo que ")
            input()