#Conjuntos (Tarea 7)
#Angel Gabriel Lopez Palacios
#Estructura de datos 2024
#19/03/24.
from flask import Flask, render_template, request

app = Flask(__name__)

class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

pila = Pila()

@app.route('/')
def index():
    return render_template('index.html', elementos=pila.items)

@app.route('/agregar', methods=['POST'])
def agregar():
    elemento = request.form['elemento']
    if elemento:
        pila.push(elemento)
    return index()

@app.route('/sacar')
def sacar():
    pila.pop()
    return index()

if __name__ == '__main__':
    app.run(debug=True)
