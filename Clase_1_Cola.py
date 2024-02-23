#Cola hecha en clase
import os
os.system('cls' if os.name == 'nt' else 'clear')

class cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, item):
        self.elementos.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        else:
            raise IndexError('Desencolar de una cola vacía')

    def esta_vacia(self):
        return len(self.elementos) == 0

#Uso de la encolar
cola = cola()
cola.encolar('elemento1')
cola.encolar('elemento2')
cola.encolar('elemento3')
cola.encolar('elemento4')
cola.encolar('elemento5')
cola.encolar('elemento6')

print('Elemento desencolado:', cola.desencolar())
