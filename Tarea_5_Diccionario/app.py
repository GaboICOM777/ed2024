#Diccionario de  datos (Tarea 5)
#Angel Gabriel Lopez Palacios
#Estructura de datos 2024
#10/03/24.
from flask import Flask, request, render_template, send_file
from diccionario_productos import productos
from generar_recibo import generar_recibo

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    return render_template('index.html', productos=productos)

@app.route('/generar_recibo', methods=['POST'])
def generar_recibo_endpoint():
    productos_seleccionados = {}
    for producto in request.form.getlist('producto'):
        productos_seleccionados[producto] = productos[producto]

    pdf_filename = generar_recibo(productos_seleccionados)
    return send_file(pdf_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
