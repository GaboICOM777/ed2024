# Definición del grafo como un diccionario de listas de adyacencia
grafo = {
    'A': ['B', 'C'],    # Nodo A conectado a los nodos B y C
    'B': ['C', 'D'],    # Nodo B conectado a los nodos C y D
    'C': ['D'],         # Nodo C conectado al nodo D
    'D': ['A']          # Nodo D conectado al nodo A
}

# Función para generar el código HTML y CSS para representar el grafo
def generar_grafo_html_css(grafo):
    # Inicializar el código HTML y CSS
    html = '''
    <div class="container">
        <h1>Angel Gabriel Lopez Palacios</h1>
        <h2>Representacion grafica de un grafo en python</h2>
        <h3>Estructura de datos 2024</h3>
        <div class="grafo">
    '''
    css = '''
    body, html {
        height: 100%;
        margin: 0;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .container {
        text-align: center;
    }
    .grafo { 
        display: flex; 
        margin-top: 20px; 
    }
    .nodo { 
        border: 1px solid black; 
        margin: 10px; 
        padding: 5px; 
        background-color: lightblue; 
        border-radius: 50%; 
        width: 30px; 
        height: 30px; 
        text-align: center; 
        line-height: 30px; 
    }
    .arista { 
        border-top: 1px solid black; 
        flex: 1; 
    }
    img{
     width:635px;
     height:480px;
     border-radius:5px;
    }
    '''

    # Recorrer cada nodo en el grafo
    for nodo, vecinos in grafo.items():
        # Agregar el nodo al HTML con su clase correspondiente
        html += f'<div class="nodo {nodo}">{nodo}</div>'
        # Recorrer los vecinos del nodo actual
        for vecino in vecinos:
            # Agregar una arista entre el nodo y su vecino
            html += f'<div class="arista"></div>'

    # Cerrar el contenedor del grafo en HTML
    html += '''
        </div>
    </div>
    '''

    # Retornar el código HTML y CSS generados
    return html, css

# Generar el código HTML y CSS del grafo
html_grafo, css_grafo = generar_grafo_html_css(grafo)

# Combinar el código HTML y CSS en un archivo HTML
codigo_html = f'''
<!DOCTYPE html>
<html>
<head>
    <title>Grafo</title>
    <style>{css_grafo}</style>
</head>
<body>
    {html_grafo}
    <img src = "Grafo.jpg" alt = "img">
</body>
</html>
'''

# Guardar el código HTML en un archivo
with open('grafo.html', 'w') as archivo:
    archivo.write(codigo_html)

# Abrir el archivo HTML en el navegador predeterminado del sistema
import webbrowser
webbrowser.open('grafo.html')

print("Se ha generado y abierto el archivo 'grafo.html' con la representación gráfica del grafo.")
