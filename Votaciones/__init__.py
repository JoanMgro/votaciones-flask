
from flask import Flask

#imports de las vars bp_xxx de paquete Routes
from Votaciones.Routes.routescandidato import bp_candidatos
from Votaciones.Routes.routesmesa import  bp_mesas

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)

    #registrando los blueprints de las rutas
    app.register_blueprint(bp_candidatos)
    app.register_blueprint(bp_mesas)

    return app