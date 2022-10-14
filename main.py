import json
from flask import Flask

from waitress import serve

# Flask instance app
app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Home - testing server</h1>'


def load_server_config():
    with open('config.json', 'r') as json_file:
        # json.load -> file obj and returns a json obj
        data = json.load(json_file)
        return data


if __name__ == '__main__':
    server_data = load_server_config()
    print(f"* SERVING ON http://{server_data['url-backend']}:{server_data['port']} ")
    serve(app, host=server_data['url-backend'], port=server_data['port'])
