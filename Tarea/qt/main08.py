import sys
import json
from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
import library06
import urllib.request


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(800, 800)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.leer_json()

    def leer_json(self):
        try:
            with urllib.request.urlopen("http://localhost:8000/figuras_random") as url:
                data = json.load(url)
                print(data)
                for figura in data:
                    self.dibuja_figura(figura)
        except Exception as e:
            print(f"Error al leer JSON: {e}")

    def dibuja_figura(self, json_fig):
        canvas = self.label.pixmap().copy()
        painter = QtGui.QPainter()
        painter.begin(canvas)

        # Obtener el color del JSON (si está presente)
        color = QColor(
            json_fig.get("color", "black")
        )  # Usar "black" como color predeterminado

        match json_fig["nombre"]:
            case "circulo":
                figura = library06.Circulo(
                    painter, json_fig["x"], json_fig["y"], json_fig["medida"]
                )
                figura.dibujar(color)  # Pasar el color
            case "cuadrado":
                figura = library06.Cuadrado(
                    painter, json_fig["x"], json_fig["y"], json_fig["medida"]
                )
                figura.dibujar(color)  # Pasar el color
            case "triangulo":
                figura = library06.Triangulo(
                    painter,
                    json_fig["x"],
                    json_fig["y"],
                    json_fig["base"],
                    json_fig["altura"],
                )
                figura.dibujar(color)  # Pasar el color
            case "pentagono":
                figura = library06.Pentagono(
                    painter, json_fig["x"], json_fig["y"], json_fig["medida"]
                )
                figura.dibujar(color)  # Pasar el color
            case _:
                print(f"No se reconoce la figura {json_fig}")

        painter.end()
        self.label.setPixmap(canvas)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
