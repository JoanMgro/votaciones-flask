import json
import os

from flask_cors import CORS

from waitress import serve

from Votaciones import create_app





# Flask instance app
#app = Flask(__name__)
app = create_app()

#registrando el app en cors
cors = CORS(app)




def load_server_config():
    #baser_dir = os.getcwd() + '/Votaciones/config.json'
    with open('config.json', 'r') as json_file :
        # json.load -> file obj and returns a json obj
        data = json.load(json_file)
        return data


if __name__ == '__main__':
    server_data = load_server_config()
    print(f"* SERVING ON http://{server_data['url-backend']}:{server_data['port']} ")
    serve(app, host=server_data['url-backend'], port=server_data['port'])

