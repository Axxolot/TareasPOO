import json, random

def figuras_random():
    figuras = []
    nombres = ['cuadrado', 'triangulo', 'circulo']
    for i in range(0, random.randint(2, 10)):
        figuras.append ({
            'nombre': nombres[random.randint(0, 2)],
            'x': random.randint(1, 400),
            'y': random.randint(1, 400),
            'media': random.randint(1, 100)
        })
        return json.dumps(figuras) 
