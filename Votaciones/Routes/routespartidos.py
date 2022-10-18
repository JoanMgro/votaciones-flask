
from flask import Blueprint
from flask import request
from flask import jsonify

from Votaciones.Controladores.partidoctrler import partidoctrler
bp_partido = Blueprint('partido', __name__, url_prefix='/partido')

#instancias de modelos
objeto_partido = partidoctrler()

@bp_partido.route('/test')
def home():
    return '<h1>Home - testing server</h1>'


@bp_partido.route('/crear', methods =['POST'])
def crear_partido():
    datos = request.get_json()
    json = objeto_partido.create(datos)
    return jsonify(json)

@bp_partido.route('', methods =['GET'])
def listar_partido():
    json = objeto_partido.listar()
    return jsonify(json)

@bp_partido.route('/modificar/<int:id>', methods =['PATCH'])
def modificar_partido(id):
    datos = request.get_json()
    json = objeto_partido.modificar(id, datos)
    return jsonify(json)

@bp_partido.route('/ver/<int:id>', methods =['GET'])
def ver_partido(id):
    json = objeto_partido.ver(id)
    return jsonify(json)

@bp_partido.route('/eliminar/<int:id>', methods =['DELETE'])
def eliminar_partido(id):
    json = objeto_partido.eliminar(id)
    return jsonify(json)
