
from flask import Blueprint
from flask import request
from flask import jsonify

from Votaciones.Controladores.mesactrler import MesaCtrler

bp_mesas = Blueprint('mesas', __name__, url_prefix='/mesas')

#instancias de modelos
objeto_mesas = MesaCtrler()


@bp_mesas.route('/test-mesas')
def home():
    return '<h1>Mesas - testing server</h1>'


@bp_mesas.route('/crear', methods =['POST'])
def crear_mesas():
    datos = request.get_json()
    json = objeto_mesas.create(datos)
    return jsonify(json)

@bp_mesas.route('', methods =['GET'])
def index_mesas():
    json = objeto_mesas.index()
    return jsonify(json)

@bp_mesas.route('/modificar/<id>', methods =['PUT'])
def modificar_mesas(id):
    datos = request.get_json()
    json = objeto_mesas.modificar(id, datos)
    return jsonify(json)

@bp_mesas.route('/ver/<id>', methods =['GET'])
def ver_mesas(id):
    json = objeto_mesas.ver(id)
    return jsonify(json)

@bp_mesas.route('/eliminar/<id>', methods =['DELETE'])
def eliminar_mesas(id):
    json = objeto_mesas.eliminar(id)
    return jsonify(json)



