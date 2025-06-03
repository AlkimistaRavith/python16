from jugos.menu import menu
from jugos.crear_bebida import crear_bebida
from jugos.seleccionar_base import seleccionar_base


def main():
    bebida = crear_bebida()

    while True:
        opcion = input("Opción: ")

        if opcion == "1":
            seleccionar_base():
            pass
        elif opcion == "2":
            print ("2")
        elif opcion == "3":
            print ("3")
        elif opcion == "4":
            print ("4")
        elif opcion == "5":
            print ("5")
        elif opcion == "6":
            print ("6")
        elif opcion == "7":
            print ("7")
            break


print("end")