#Diccionario de  datos (Tarea 5)
#Angel Gabriel Lopez Palacios
#Estructura de datos 2024
#10/03/24.
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from diccionario_productos import productos

def generar_recibo(productos_seleccionados):
    # Ruta del directorio actual del script
    directorio_actual = os.path.dirname(__file__)
    
    # Ruta de la carpeta donde se guardará el archivo PDF
    carpeta_destino = os.path.join(directorio_actual, "Recibos_compra")

    # Comprueba si la carpeta de destino existe, y si no, créala
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Nombre del archivo PDF
    pdf_filename = os.path.join(carpeta_destino, "recibo.pdf")

    c = canvas.Canvas(pdf_filename, pagesize=letter)
    y = 750
    total = 0

    c.drawString(100, y, "Recibo de Compra:")
    y -= 20

    for producto, precio in productos_seleccionados.items():
        c.drawString(100, y, f"{producto}: ${precio}")
        total += precio
        y -= 20

    c.drawString(100, y, f"Total: ${total}")

    c.save()

    return pdf_filename
