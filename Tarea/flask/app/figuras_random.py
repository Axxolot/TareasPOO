import json
import random


def figuras_random():
    figuras = []
    nombres = ["cuadrado", "triangulo", "circulo", "pentagono"]
    colores = [
        "red",
        "green",
        "blue",
        "yellow",
        "purple",
        "orange",
        "pink",
        "cyan",
    ]  # Lista de colores

    for i in range(0, random.randint(2, 10)):
        nombre = nombres[random.randint(0, 3)]
        color = colores[random.randint(0, len(colores) - 1)]  # Color aleatorio

        if nombre == "triangulo":
            # Para el triángulo, generamos base y altura
            base = random.randint(20, 100)
            altura = random.randint(20, 100)
            figura = {
                "nombre": nombre,
                "x": random.randint(0, 400),
                "y": random.randint(0, 400),
                "base": base,
                "altura": altura,
                "color": color,  # Agregar color
            }
        else:
            # Para cuadrado, círculo y pentágono, usamos "medida"
            figura = {
                "nombre": nombre,
                "x": random.randint(0, 400),
                "y": random.randint(0, 400),
                "medida": random.randint(20, 100),
                "color": color,  # Agregar color
            }
        figuras.append(figura)
    return json.dumps(figuras)

