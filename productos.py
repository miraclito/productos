import time

from utils import limpiarPantalla
from models import Producto

ruta_archivo = "./archivos/producto.txt"


def creargaseosa():
    codigo = input("Código: ")
    marca = input("marca: ")
    detalle = input("tamaño: ")
    precio = input("Precio: ")

    gaseosa = Producto(codigo, marca, detalle, precio)

    archivogaseosa = open(ruta_archivo, "a")
    archivogaseosa.write(str(gaseosa))
    archivogaseosa.close()


def buscargaseosa(codigo):
    gaseosa = None
    archovogaseosa = open(ruta_archivo, "r")
    for linea in archovogaseosa.readlines():
        atributos = linea.split(";")
        if codigo == atributos[0]:
            gaseosa = Producto(atributos[0], atributos[1], atributos[2], atributos[3])
            break
    archovogaseosa.close()

    return gaseosa


def gestiongaseosa():
    limpiarPantalla()
    while True:
        print("SUBMENU: Gestion de gaseosas ")
        print("1. Ingresar gaseosa")
        print("2. Mostrar gaseosas")
        print("3. Buscar gaseosas")
        print("4. Regresar al menu principal")
        op = int(input("Opción: "))

        match (op):
            case 1:
                limpiarPantalla()
                creargaseosa()
                print("Creado Correctamente!!!")
            case 2:
                limpiarPantalla()
                archivogaseosa = open(ruta_archivo, "r")
                print("Código\tNombre\t\tDetalle\t\t\tPrecio")
                for linea in archivogaseosa.readlines():
                    atributos = linea.split(";")
                    print(
                        "{}\t{}\t\t{}\t\t\t{}".format(
                            atributos[0], atributos[1], atributos[2], atributos[3]
                        )
                    )
                archivogaseosa.close()

            case 3:
                limpiarPantalla()
                codigo = input("Ingrese código de la gaseosa: ")
                fila = str(buscargaseosa(codigo))
                print(f"{fila}")
                
                output = fila.split(";")
                
                print(output)

            case 4:
                limpiarPantalla()
                print("Gracias por usar el submenu")
                time.sleep(2)
                break
            case _:
                print("opción incorrecta")
                time.sleep(2)
                limpiarPantalla()
