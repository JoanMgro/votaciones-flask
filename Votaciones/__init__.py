
from flask import Flask
from flask_mongoengine import MongoEngine


#codigo del mongo
# client = pymongo.MongoClient("mongodb+srv://grupociclo4:<password>@clusterciclo4a.lwuilv8.mongodb.net/?retryWrites=true&w=majority")
# db = client.test


#imports de las vars bp_xxx de paquete Routes
from Votaciones.Routes.routescandidato import bp_candidatos
from Votaciones.Routes.routesmesa import bp_mesas
from Votaciones.Routes.routespartidos import bp_partido
def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)

    #registrando los blueprints de las rutas
    app.register_blueprint(bp_candidatos)
    app.register_blueprint(bp_mesas)
    app.register_blueprint(bp_partido)


    return app