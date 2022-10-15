
from flask import Flask
from Votaciones.Routes.routescandidato import bp_candidatos

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)
    app.register_blueprint(bp_candidatos)

    return app