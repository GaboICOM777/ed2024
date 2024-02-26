# Arbol Binario de decisiones (Tarea 3)
#Angel Gabriel Lopez Palacios
#Estructura de datos 2024
#23/02/24

class Nodo:
    def __init__(self, dato, nivel):
        self.dato = dato  # Asigna el dato al atributo 'dato' del nodo.
        self.nivel = nivel  # Asigna el nivel al atributo 'nivel' del nodo.
        self.izquierdo = None  # Inicializa el hijo izquierdo como None.
        self.derecho = None  # Inicializa el hijo derecho como None.

class ArbolBinario:
    def __init__(self):
        self.raiz = None  # Inicializa la raíz del árbol como None.

    def insertar(self, dato):
        if self.raiz is None:  # Si el árbol está vacío:
            self.raiz = Nodo(dato, 0)  # Crea un nodo y lo asigna como raíz.
        else:
            self._insertar_recursivo(dato, self.raiz, 1)  # Llama a la función de inserción recursiva.

    def _insertar_recursivo(self, dato, nodo, nivel):
        if dato <= nodo.dato:  # Si el dato es menor que el dato del nodo actual:
            if nodo.izquierdo is None:  # Si no hay un hijo izquierdo:
                nodo.izquierdo = Nodo(dato, nivel)  # Crea un nuevo nodo izquierdo.
            else:
                self._insertar_recursivo(dato, nodo.izquierdo, nivel + 1)  # Llama recursivamente a la función para el hijo izquierdo.
        else:
            if nodo.derecho is None:  # Si no hay un hijo derecho:
                nodo.derecho = Nodo(dato, nivel)  # Crea un nuevo nodo derecho.
            else:
                self._insertar_recursivo(dato, nodo.derecho, nivel + 1)  # Llama recursivamente a la función para el hijo derecho.

    def representar(self):
        niveles = {}  # Diccionario para almacenar los nodos por nivel.
        self._representar_recursivo(self.raiz, niveles)  # Llama a la función recursiva de representación.
        return niveles

    def _representar_recursivo(self, nodo, niveles):
        if nodo is not None:  # Si el nodo no es None:
            self._representar_recursivo(nodo.izquierdo, niveles)  # Recorre el subárbol izquierdo.
            if nodo.nivel in niveles:  # Si el nivel ya existe en el diccionario de niveles:
                niveles[nodo.nivel].append(nodo.dato)  # Agrega el dato al nivel correspondiente.
            else:
                niveles[nodo.nivel] = [nodo.dato]  # Crea una nueva lista para el nivel y agrega el dato.
            self._representar_recursivo(nodo.derecho, niveles)  # Recorre el subárbol derecho.

# Ejemplo de uso
arbol = ArbolBinario()  # Crea un objeto de la clase ArbolBinario.
datos = [20, 40, 50, 59, 1, 2, 3, 45, 300, 89,301,303]  # Datos de ejemplo.
for d in datos:  # Para cada dato en la lista de datos:
    arbol.insertar(d)  # Inserta el dato en el árbol.

# Generar HTML y CSS
niveles = arbol.representar()  # Obtiene los niveles del árbol.

html_niveles = ""  # Variable para almacenar el contenido HTML de los niveles.
for nivel in sorted(niveles.keys()):  # Para cada nivel ordenado:
    elementos = niveles[nivel]  # Obtiene los elementos del nivel.
    html_niveles += f"<div class='nivel'>"  # Abre una nueva etiqueta div para el nivel.
    for numero in elementos:  # Para cada elemento en el nivel:
        html_niveles += f"<div class='cuadro'>{numero}</div>"  # Crea una etiqueta div para mostrar el número.
    html_niveles += f"<div class='nivel-numero'>{nivel}</div>"  # Agrega el número de nivel.
    html_niveles += "</div>"  # Cierra la etiqueta div del nivel.
    html_niveles += "<hr>"  # Agrega una línea separadora entre niveles.

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Árbol Binario en Python</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: gray;
            text-align: center;
        }}
        .arbol-binario {{
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
        }}
        .nivel {{
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 10px 0;
        }}
        .cuadro {{
            background-color: cornflowerblue;
            border: 2px solid #ffd700;
            border-radius: 20px;
            font-size: 20px;
            padding: 10px;
            margin: 0 5px;
        }}
        .nivel-numero {{
            margin: 0 5px;
            font-size: 20px;
            color: white;
            background-color: black;
            padding: 5px 10px;
            border-radius: 10px;
        }}
        hr {{
            width: 100%;
            margin: 20px 0;
            border: none;
            border-top: 2px solid #ffd700;
        }}
    </style>
</head>
<body>
    <h2>Árbol Binario de Decisiones<br>Lopez Palacios Angel Gabriel<br>ED2024 ICOM CUCOSTA</h2>
    <div class="arbol-binario">
        {html_niveles}  # Inserta el contenido HTML generado.
    </div>
</body>
</html>
"""

# Guardar en un archivo HTML
file_name = "arbol_binario.html"  # Nombre del archivo HTML.
with open(file_name, "w", encoding="utf-8") as file:  # Abre el archivo en modo escritura.
    file.write(html_content)  # Escribe el contenido HTML en el archivo.

# Abrir el archivo HTML en el navegador
import webbrowser  # Importa el módulo webbrowser para abrir el navegador.
import os  # Importa el módulo os para trabajar con rutas de archivos.

file_path = os.path.abspath(file_name)  # Obtiene la ruta absoluta del archivo HTML.
webbrowser.open(f"file://{file_path}")  # Abre el archivo HTML en el navegador.
