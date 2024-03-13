from flask import Flask, render_template, request

app = Flask(__name__)

# Colección de personas
personas = []

# Ruta para mostrar la información de la colección de personas y agregar nuevas personas
@app.route('/', methods=['GET', 'POST'])
def mostrar_personas():
    if request.method == 'POST':
        # Agregar nueva persona a la colección
        nombre = request.form['nombre']
        fecha_cumpleaños = request.form['fecha_cumpleaños']
        sexo = request.form['sexo']
        nueva_persona = (nombre, fecha_cumpleaños, sexo)
        personas.append(nueva_persona)

    # Pasar la colección de personas a la plantilla HTML
    return render_template('plantilla.html', personas=personas)

if __name__ == '__main__':
    app.run(debug=True)
