from flask import Flask
from app import buscar_por_columna

app = Flask(__name__)


# Ruta para obtener datos por ID
@app.route('/datos/<int:id>', methods=['GET'])
def obtener_datos_por_id(id):
    resultado = buscar_por_columna(id)
    return resultado


if __name__ == '__main__':
    app.run(debug=True)