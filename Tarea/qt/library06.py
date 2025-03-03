from PyQt6 import QtGui
from PyQt6.QtCore import QPointF
import math


class Geometrica:
    def __init__(self, painter: QtGui.QPainter, x, y):
        self.x = x
        self.y = y
        self.painter = painter
        print(f"Se ha creado una figura en la posición ({self.x}, {self.y})")

    def dibujar(self, color: QtGui.QColor = None):
        if color:
            self.painter.setBrush(color)


class Circulo(Geometrica):
    def __init__(self, painter: QtGui.QPainter, x, y, radio):
        super().__init__(painter, x, y)
        self.radio = radio

    def dibujar(self, color: QtGui.QColor = None):
        if color:
            self.painter.setBrush(color)  # Establecer el color de relleno
        self.painter.drawEllipse(
            self.x - self.radio, self.y - self.radio, self.radio * 2, self.radio * 2
        )


class Cuadrado(Geometrica):
    def __init__(self, painter: QtGui.QPainter, x, y, lado):
        super().__init__(painter, x, y)
        self.lado = lado

    def dibujar(self, color: QtGui.QColor = None):
        if color:
            self.painter.setBrush(color)  # Establecer el color de relleno
        self.painter.drawRect(self.x, self.y, self.lado, self.lado)


class Triangulo(Geometrica):
    def __init__(self, painter: QtGui.QPainter, x, y, base, altura):
        super().__init__(painter, x, y)
        self.base = base
        self.altura = altura

    def dibujar(self, color: QtGui.QColor = None):
        if color:
            self.painter.setBrush(color)  # Establecer el color de relleno
        # Definir los puntos del triángulo
        triangulo = QtGui.QPolygonF(
            [
                QPointF(self.x, self.y + self.altura),  # Punto inferior izquierdo
                QPointF(
                    self.x + self.base, self.y + self.altura
                ),  # Punto inferior derecho
                QPointF(self.x + self.base / 2, self.y),  # Punto superior central
            ]
        )
        self.painter.drawPolygon(triangulo)


class Pentagono(Geometrica):
    def __init__(self, painter: QtGui.QPainter, x, y, lado):
        super().__init__(painter, x, y)
        self.lado = lado

    def dibujar(self, color: QtGui.QColor = None):
        if color:
            self.painter.setBrush(color)  # Establecer el color de relleno
        # Calcular los puntos del pentágono
        puntos = []
        for i in range(5):
            angle = 2 * math.pi * i / 5
            px = self.x + self.lado * math.cos(angle)
            py = self.y - self.lado * math.sin(angle)
            puntos.append(QPointF(px, py))  # Usar QPointF desde QtCore
        # Dibujar el pentágono
        self.painter.drawPolygon(puntos)
