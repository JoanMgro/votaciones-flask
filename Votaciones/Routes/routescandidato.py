
from flask import Blueprint
from flask import request
from flask import jsonify

from Votaciones.Controladores.candidatoctrler import CandidatoCtrler

bp_candidatos = Blueprint('candidatos', __name__, url_prefix='/candidatos')

#instancias de modelos
objeto_candidato = CandidatoCtrler()


@bp_candidatos.route('/test')
def home():
    return '<h1>Home - testing server</h1>'


@bp_candidatos.route('/crear', methods =['POST'])
def crear_candidato():
    datos = request.get_json()
    json = objeto_candidato.create(datos)
    return jsonify(json)

@bp_candidatos.route('', methods =['GET'])
def index_candidatos():
    json = objeto_candidato.index()
    return jsonify(json)

@bp_candidatos.route('/modificar/<int:id>', methods =['PATCH'])
def modificar_candidato(id):
    datos = request.get_json()
    json = objeto_candidato.modificar(id, datos)
    return jsonify(json)

@bp_candidatos.route('/ver/<int:id>', methods =['GET'])
def ver_candidato(id):
    json = objeto_candidato.ver(id)
    return jsonify(json)

@bp_candidatos.route('/eliminar/<int:id>', methods =['DELETE'])
def eliminar_candidato(id):
    json = objeto_candidato.eliminar(id)
    return jsonify(json)



