#Cola doblemente circular (Tarea 2)
#Angel Gabriel Lopez Palacios
#Estructura de datos 2024
#18/02/24
import os
os.system('cls' if os.name == 'nt' else 'clear')

from colaDoblementeCircular import Cola

cola = Cola()

accionElegida = ""

while accionElegida != "6":
    print("Elige una de las siguientes opciones:\n1 = Añadir elemento a la cola\n2 = Remover primer elemento")
    print("3 = Mostrar elementos actuales\n4 = Mostrar el primer elemento\n5 = Mostrar cambios efectuados")
    print("6 = Salir")
    accionElegida = input()

    if accionElegida == "1":
        dato = int(input("Introduce el dato a añadir: "))
        cola.añadir(dato)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif accionElegida == "2":
        cola.desechar()
        os.system('cls' if os.name == 'nt' else 'clear')
    elif accionElegida == "3":
        cola.mostrar()
    elif accionElegida == "4":
        cola.frente()
    elif accionElegida == "5":
        for cambio in cola.cambiosHechos():
            print(cambio)
    elif accionElegida.lower() == "6":
        print("Saliendo...")
    else:
        print("Opción no válida. Inténtalo de nuevo.")

