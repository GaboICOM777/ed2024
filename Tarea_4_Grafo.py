# Importar el módulo webbrowser para abrir el archivo HTML en el navegador
import webbrowser

# Función para generar la matriz de adyacencia
def matriz_adyacencia(vertices, aristas):
    matriz = [[0] * len(vertices) for _ in range(len(vertices))]  # Inicializar matriz con ceros
    for arista in aristas:
        origen, destino = arista
        # Marcar la conexión entre los vértices en la matriz de adyacencia
        matriz[vertices.index(origen)][vertices.index(destino)] = 1
        matriz[vertices.index(destino)][vertices.index(origen)] = 1
    return matriz

# Definir los vértices y aristas del grafo
vertices = ['A', 'B', 'C', 'D']
aristas = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D')]

# Generar la matriz de adyacencia
matriz = matriz_adyacencia(vertices, aristas)

# Crear el contenido HTML
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Matriz de Adyacencia</title>
    <style>
        table {{
            border-collapse: collapse;  /* Colapsar bordes de la tabla */
            margin: auto;  /* Centrar la tabla */
        }}
        th, td {{
            border: 1px solid black;  /* Borde de 1px sólido */
            padding: 8px;  /* Espacio interno */
            text-align: center;  /* Alinear contenido al centro */
        }}
        th {{
            background-color: #f2f2f2;  /* Color de fondo para los encabezados */
        }}
    </style>
</head>
<body>
    <h1 style="text-align: center;">Matriz de Adyacencia<br>Ángel Gabriel López Palacios<br>Estructira de datos 2024</h1>
    <table>
        <tr><th></th>{}</tr>  <!-- Encabezados de columna -->
        {}  <!-- Filas de la matriz -->
    </table>
</body>
</html>
"""

# Crear las filas de la tabla
filas = ""
for i, fila in enumerate(matriz):
    # Agregar una fila a la tabla con valores de la matriz
    filas += "<tr><th>{}</th>{}</tr>".format(vertices[i], "".join("<td>{}</td>".format(valor) for valor in fila))

# Escribir el archivo HTML
with open('matriz_adyacencia.html', 'w') as f:
    f.write(html.format("".join("<th>{}</th>".format(v) for v in vertices), filas))

# Abrir el archivo HTML en el navegador predeterminado
webbrowser.open('matriz_adyacencia.html')
