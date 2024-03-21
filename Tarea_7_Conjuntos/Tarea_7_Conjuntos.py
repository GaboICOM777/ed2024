#Conjuntos (Tarea 7)
#Angel Gabriel Lopez Palacios
#Estructura de datos 2024
#17/03/24.
from flask import Flask, request

app = Flask(__name__)

# Definir los conjuntos de hijos de Carla y Juan
hijos_carla = set()
hijos_juan = set()

@app.route('/')
def index():
    return '''
    <h1>Ingresa los nombres de los hijos de Carla y Juan:</h1>
    <form method="post" action="/submit">
        <label for="carla">Hijos de Carla:</label><br>
        <input type="text" id="carla" name="carla"><br>
        <label for="juan">Hijos de Juan:</label><br>
        <input type="text" id="juan" name="juan"><br><br>
        <input type="submit" value="Enviar">
    </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    global hijos_carla, hijos_juan
    hijos_carla = set(request.form['carla'].split())
    hijos_juan = set(request.form['juan'].split())
    return '''
    <h1>¡Parámetros recibidos!</h1>
    <p><a href="/intersection">Intersección</a></p>
    <p><a href="/superconjunto">Superconjunto</a></p>
    <p><a href="/subconjunto">Subconjunto</a></p>
    <p><a href="/unicidad">Unicidad</a></p>
    <p><a href="/union">Unión</a></p>
    <p><a href="/complemento">Complemento</a></p>
    <p><a href="/diferencias">Diferencias</a></p>
    <p><a href="/disjunto">Disjunto</a></p>
    '''

@app.route('/intersection')
def intersection():
    result = hijos_carla.intersection(hijos_juan)
    if result:
        return generate_html("Intersección", result)
    else:
        return generate_html("Intersección", "No hay hijos en común entre Carla y Juan")

@app.route('/superconjunto')
def superconjunto():
    if hijos_carla.issuperset(hijos_juan) or 'Carla' in hijos_juan:
        result = "Carla es superconjunto de Juan<br>"
    else:
        result = "Carla NO es superconjunto de Juan<br>"
    if hijos_juan.issuperset(hijos_carla) or 'Juan' in hijos_carla:
        result += "Juan es superconjunto de Carla<br>"
    else:
        result += "Juan NO es superconjunto de Carla<br>"
    return generate_html("Superconjunto", result)

@app.route('/subconjunto')
def subconjunto():
    if hijos_carla.issubset(hijos_juan) or 'Juan' in hijos_carla:
        result = "Carla es subconjunto de Juan<br>"
    else:
        result = "Carla NO es subconjunto de Juan<br>"
    if hijos_juan.issubset(hijos_carla) or 'Carla' in hijos_juan:
        result += "Juan es subconjunto de Carla<br>"
    else:
        result += "Juan NO es subconjunto de Carla<br>"
    return generate_html("Subconjunto", result)

@app.route('/unicidad')
def unicidad():
    unique_carla = len(hijos_carla) == len(set(hijos_carla))
    unique_juan = len(hijos_juan) == len(set(hijos_juan))
    result = f"Carla tiene hijos únicos: {unique_carla}<br>Juan tiene hijos únicos: {unique_juan}"
    return generate_html("Unicidad", result)

@app.route('/union')
def union():
    result = hijos_carla.union(hijos_juan)
    return generate_html("Unión", result)

@app.route('/complemento')
def complemento():
    result_carla = hijos_juan.difference(hijos_carla)
    result_juan = hijos_carla.difference(hijos_juan)
    return generate_html("Complemento", f"Hijos de Carla que no están en Juan: {result_carla}<br>Hijos de Juan que no están en Carla: {result_juan}")

@app.route('/diferencias')
def diferencias():
    result = hijos_carla.symmetric_difference(hijos_juan)
    return generate_html("Diferencias", result)

@app.route('/disjunto')
def disjunto():
    if hijos_carla.isdisjoint(hijos_juan):
        result = "Los conjuntos de Carla y Juan son disjuntos, no tienen hijos en común"
    else:
        result = "Los conjuntos de Carla y Juan NO son disjuntos, tienen hijos en común"
    return generate_html("Disjunto", result)

def generate_html(title, result):
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
    </head>
    <body>
        <h1>{title}</h1>
        <p>{result}</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
