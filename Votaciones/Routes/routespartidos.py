
from flask import Blueprint
from flask import request
from flask import jsonify

from Votaciones.Controladores.partidoctrler import PartidoCtrler
bp_partido = Blueprint('partido', __name__, url_prefix='/partidos')

#instancias de modelos
objeto_partido = PartidoCtrler()

@bp_partido.route('/test-partidos')
def home():
    return '<h1>Home - testing server</h1>'


@bp_partido.route('/crear', methods =['POST'])
def crear_partido():
    datos = request.get_json()
    json = objeto_partido.create(datos)
    return jsonify(json)

@bp_partido.route('', methods =['GET'])
def listar_partido():
    json = objeto_partido.index()
    return jsonify(json)

@bp_partido.route('/modificar/<id>', methods =['PUT'])
def modificar_partido(id):
    datos = request.get_json()
    json = objeto_partido.modificar(id, datos)
    return jsonify(json)

@bp_partido.route('/ver/<id>', methods =['GET'])
def ver_partido(id):
    json = objeto_partido.ver(id)
    return jsonify(json)

@bp_partido.route('/eliminar/<id>', methods =['DELETE'])
def eliminar_partido(id):
    json = objeto_partido.eliminar(id)
    return jsonify(json)
