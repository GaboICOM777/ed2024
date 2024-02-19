#Cola doblemente circular (Tarea 2)
#Angel Gabriel Lopez Palacios
#Estructura de datos 2024
#18/02/24.

class Cola():

    # Constructor de la clase
    def __init__(self):
        # Lista para almacenar los elementos de la cola
        self.cola = []
        # Entero que representa el tamaño actual de la cola
        self.tamaño = 0
        # Lista para almacenar un registro de las operaciones
        self.cambios = []

    # Verifica si la cola está vacía
    def vacio(self):
        return len(self.cola) == 0

    # Agrega un nuevo elemento a la cola
    def añadir(self, dato):
        # Añade el elemento al final de la lista
        self.cola += [dato]
        # Incrementa el tamaño de la cola
        self.tamaño += 1
        # Registra la inserción
        self.cambios.append("Inserción: {}".format(dato))

    # Elimina el primer elemento de la cola
    def desechar(self):
        if self.vacio():
            print("La cola esta vacía")
        else:
            # Elimina el primer elemento de la lista
            self.cola = [self.cola[i] for i in range(1, self.tamaño)]
            # Decrece el tamaño de la cola
            self.tamaño -= 1
            # Registra la eliminación
            self.cambios.append("Eliminación: {}".format(self.cola[0]))

    # Imprime los elementos de la cola
    def mostrar(self):
        n = self.tamaño - 1
        while n > -1:
            print("[%d] => %d"%(n,self.cola[n]))
            n-=1

    # Obtiene el primer elemento de la cola
    def frente(self):
        if self.vacio():
            print("Cola Vacía")
        else:
            print("Primer dato : %d"%(self.cola[0]))
            return self.cola[0]

    # Obtiene un registro de las operaciones realizadas
    def cambiosHechos(self):
        return self.cambios