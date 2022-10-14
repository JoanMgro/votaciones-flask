import json
from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

from waitress import serve

from Controladores.candidatoctrler import CandidatoCtrler

# Flask instance app
app = Flask(__name__)

#registrando el app en cors
cors = CORS(app)

#instancias de modelos
nuevo_candidato = CandidatoCtrler()

@app.route('/')
def home():
    return '<h1>Home - testing server</h1>'

@app.route('/candidato', methods =['POST'])
def crear_candidato():
    datos = request.get_json()
    json = nuevo_candidato.create(datos)
    return jsonify(json)





def load_server_config():
    with open('config.json', 'r') as json_file:
        # json.load -> file obj and returns a json obj
        data = json.load(json_file)
        return data


if __name__ == '__main__':
    server_data = load_server_config()
    print(f"* SERVING ON http://{server_data['url-backend']}:{server_data['port']} ")
    serve(app, host=server_data['url-backend'], port=server_data['port'])

