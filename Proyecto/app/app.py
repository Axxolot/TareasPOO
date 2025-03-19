import clima
import dibuja_clima
from flask import Flask, json, render_template, Response, request

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def home():
    """Renderiza la página principal."""
    return render_template('index.html')


@app.route('/clima', methods=('GET', 'POST'))
def clima_view():
    ciudad = request.args.get('ciudad')  # Obtener el parámetro 'ciudad' desde la URL
    if ciudad:
        clima_obj = clima.Clima()  # Crear una instancia de la clase Clima
        weather_data = clima_obj.extrae_relevantes(ciudad)  # Obtener los datos del clima
        icon_code = weather_data['icono']  # Obtener el código del icono
        return render_template('index.html', weather=weather_data, icon_code=icon_code)  # Pasar los datos y el código del icono al HTML
    else:
        return render_template('index.html', error="No se proporcionó una ciudad")  # Manejar el caso sin ciudad

@app.route('/dibuja_clima/<icon_code>', methods=('GET', 'POST'))
def dc(icon_code):
    # Usamos la función dibuja_icono con el código del icono recibido como parámetro
    r = Response(response=dibuja_clima.dibuja_icono(icon_code), status=200, mimetype="image/png")
    r.headers["Content-Type"] = "image/png"
    return r

if __name__ == '__main__':
    # Configuración de la aplicación Flask
    app.run(debug=True, host='0.0.0.0', port=5000)
