import pandas as pd
import json
from flask import Flask, render_template
from flask_cors import CORS
import socket
import os
from dotenv import load_dotenv

# Leer el archivo Excel
df = pd.read_excel("./source/dataFISI.xlsx")
columna_id = "alumno_codigo"


def buscar_por_columna(identificador):
    # Buscar la fila que coincide con el ID
    fila = df[df[columna_id] == identificador]
    # Si se encuentra la fila, devolver los datos en formato JSON
    if not fila.empty:
        json_data = fila.to_json(orient="records")
        json_obj = json.loads(json_data)
        if json_obj:
            return json.dumps(json_obj[0])
    # Si no se encuentra ningún resultado, devolver una fila vacía con los nombres de columna correctos
    fila_vacia = {
        columna: None if columna != columna_id else "" for columna in df.columns
    }
    return json.dumps([fila_vacia])


app = Flask(__name__)


# Configurar CORS para permitir solo dominios específicos
trusted_origins = [
    "https://raphaelwmr.github.io/BienestarConnect_FRONTEND/",
    "https://raphaelwmr.github.io/",
    "https://raphaelwmr.github.io/BienestarConnect_FRONTEND/alumnos/add"
]
CORS(app, resources={r"/*": {"origins": trusted_origins}})


@app.route("/")
def index():
    return render_template("index.html")


# Ruta para obtener datos por ID
@app.route("/datos/<int:id>", methods=["GET"])
def obtener_datos_por_id(id):
    resultado = buscar_por_columna(id)
    return resultado


# DOTENV
load_dotenv()


if __name__ == "__main__":
    _port = os.getenv("PORT")
    _host = os.getenv("HOST")
    ip_address = socket.gethostbyname(socket.gethostname())
    app.run(debug=False, host=_host, port=_port)
    print(f"Servidor flask corriendo en http://{ip_address}:{_port}")
