import pandas as pd
import json
# Leer el archivo Excel
df = pd.read_excel('./source/dataFISI.xlsx')
columna_id = 'alumno_codigo'

def buscar_por_columna(identificador):
    # Buscar la fila que coincide con el ID
    fila = df[df[columna_id] == identificador]
    # Si se encuentra la fila, devolver los datos en formato JSON
    if not fila.empty:
        json_data = fila.to_json(orient='records')
        json_obj = json.loads(json_data)
        if json_obj:
            return json.dumps(json_obj[0])
    # Si no se encuentra ningún resultado, devolver una fila vacía con los nombres de columna correctos
    fila_vacia = {columna: None if columna != columna_id else '' for columna in df.columns}
    return json.dumps([fila_vacia])