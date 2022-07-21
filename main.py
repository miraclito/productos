
import getpass
import time

from utils import limpiarPantalla
from productos import gestiongaseosa
from usuarios import gestionUsuarios


    
def run():
    while True:
        print("\033[91m" + " Gaseosas    " + "\033[91m")
        print("\033[0m")
        print("============================")
        print(" MENÚ PRINCIPAL DEL SISTEMA ")
        print("1. Gestión de gaseosas")
        print("2. Gestión de Usuarios")
        print("0. Salir")
        op = int(input("Opción: "))

        match (op):
            case 1:
                limpiarPantalla()
                gestiongaseosa()

            case 2:
                limpiarPantalla()
                gestionUsuarios()
            case 0:
                limpiarPantalla()
                print("Saliendo del sistema... hasta pronto")
                break

            case _:
                print("opción incorrecta")
                time.sleep(2)
                limpiarPantalla()


def main():
    acumulador = 0
    while True and acumulador != 3:

        user = input("Ingrese Usuario: ")
        
        passwd = getpass.getpass("Ingrese password: ")

        if passwd == "123":
            limpiarPantalla()
            run()
        else:
            print("Contraseña incorrecta")
            acumulador += 1
            time.sleep(2)
            limpiarPantalla()

            # break


if __name__ == "__main__":
    
    main()
