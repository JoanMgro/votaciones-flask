import json
from flask import Flask

from waitress import serve

#Flask instance app
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Home - testing server</h1>'



def loadServerConfig():
    with open('config.json', 'r') as jsonFile:
        #json.load -> file obj and returns a json obj
        data = json.load(jsonFile)
        return data


if __name__ == '__main__':
    serverData = loadServerConfig()
    print(f"* SERVING ON http://{serverData['url-backend']}:{serverData['port']} ")
    serve(app, host = serverData['url-backend'], port = serverData['port'])



