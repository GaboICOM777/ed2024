# Colas "FIFO" (Tarea 1)
#Angel Gabriel Lopez Palacios
#Estructura de datos 2024
#02/24
import os
os.system('cls' if os.name == 'nt' else 'clear')
# Actividad de cola en atención a clientes por parte de un call center.
colaServicios = ["Maria", "Alejandro", "Jose", "Mario"]
colaAtencion = ["Minerva", "Juanita", "Veronica", "Luis"]
colaAyuda = ["Carmina", "Britany", "Angel", "Alberto"]

# Usamos tuplas en lugar de listas para las claves del diccionario
valores = {
    "colaServicios": colaServicios,
    "colaAtencion": colaAtencion,
    "colaAyuda": colaAyuda
}

for cola, clientes in valores.items():
    print(cola)
    clientes.append("Llamada Nueva")
    print(clientes)
    cliente_atendido = clientes.pop(0)
    print(f"Atendiendo a {cliente_atendido}")
    print("La cola:", cola, "tiene restantes a", clientes)
