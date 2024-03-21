#Grafos (Tarea 4)
#Angel Gabriel Lopez Palacios
#Estructura de datos 2024
#05/03/24.
# Matriz de adyacencia
adjacency_matrix = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 0],
    [1, 0, 0, 0]
]

# Función para generar el contenido HTML de la matriz de adyacencia
def generate_matrix_html(adjacency_matrix):
    # Encabezado de la tabla con las letras de las columnas
    table_html = '<table>'
    table_html += '<tr><td></td>' + ''.join([f'<td>{chr(65+i)}</td>' for i in range(len(adjacency_matrix))]) + '</tr>'
    
    # Contenido de la tabla
    for i in range(len(adjacency_matrix)):
        table_html += '<tr>'
        # Letra de la fila
        table_html += f'<td>{chr(65+i)}</td>'
        # Valores de la fila
        for j in range(len(adjacency_matrix[i])):
            table_html += f'<td>{adjacency_matrix[i][j]}</td>'
        table_html += '</tr>'
    table_html += '</table>'
    
    return table_html

# Generar el contenido HTML del grafo
def generate_html_graph(adjacency_matrix, matrix_html):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <style>
            body {{
                text-align: center;
            }}
            table {{
                border-collapse: collapse;
                margin: auto;
                margin-bottom: 20px;
            }}
            table, th, td {{
                border: 1px solid black;
                padding: 10px;
                text-align: center;
            }}
            h1, h2 {{
                margin-top: 50px;
            }}
        </style>
    </head>
    <body>
        <h1>Angel Gabriel Lopez Palacios - Estructura de datos 2024</h1>
        <h2>Matriz de adyacencia</h2>
        {matrix_html}
        <div class="graph">
    """

    # Agregar nodos al HTML
    nodes_html = ""
    for i in range(len(adjacency_matrix)):
        nodes_html += f'<div class="node">{chr(65+i)}</div>'
    
    html_content += nodes_html

    # Agregar aristas al HTML
    edges_html = ""
    for i in range(len(adjacency_matrix)):
        for j in range(i+1, len(adjacency_matrix[i])):
            if adjacency_matrix[i][j] == 1:
                if i == 0 and j == 1:
                    edges_html += f'<div class="edge" id="AB"></div>'
                elif i == 0 and j == 2:
                    edges_html += f'<div class="edge" id="AC"></div>'
                elif i == 1 and j == 2:
                    edges_html += f'<div class="edge" id="BC"></div>'
                elif i == 1 and j == 3:
                    edges_html += f'<div class="edge" id="BD"></div>'
                elif i == 2 and j == 3:
                    edges_html += f'<div class="edge" id="CD"></div>'

    html_content += edges_html

    html_content += """
        </div>
        <img src="Grafo.jpg" style="display:block; margin:auto;">
    </body>
    </html>
    """

    return html_content

# Generar el contenido HTML de la matriz de adyacencia
matrix_html = generate_matrix_html(adjacency_matrix)

# Generar el contenido HTML del grafo
html_content = generate_html_graph(adjacency_matrix, matrix_html)

# Escribir el contenido en un archivo HTML
with open("Tarea_4_Grafo/document.html", "w") as file:
    file.write(html_content)

# Abrir el archivo HTML en el navegador predeterminado
import os
import webbrowser
webbrowser.open("file://" + os.path.realpath("Tarea_4_Grafo/document.html"))
