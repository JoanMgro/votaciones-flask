
from flask import Blueprint
from flask import request
from flask import jsonify

from Votaciones.Controladores.resultadoctrler import ResultadoCtrler

bp_resultados = Blueprint('resultados', __name__, url_prefix='/resultados')

#instancias de modelos
objeto_resultado = ResultadoCtrler()


@bp_resultados.route('/test-resultados')
def home():
    return '<h1>Resultados - testing server</h1>'



@bp_resultados.route("/crear/<string:id_candidato>/mesa/<string:id_mesa>", methods=['POST'])
def crear_resultado(id_candidato, id_mesa):
    datos = request.get_json()
    json = objeto_resultado.create(datos, id_mesa, id_candidato)
    return jsonify(json)

@bp_resultados.route('', methods =['GET'])
def index_resultado():
    json = objeto_resultado.index()
    return jsonify(json)

@bp_resultados.route('/modificar/<id>/candidato/<id_candidato>/mesa/<id_mesa>', methods =['PUT'])
def modificar_resultado(id, id_candidato, id_mesa):
    datos = request.get_json()
    json = objeto_resultado.modificar(id, datos, id_mesa, id_candidato)
    return jsonify(json)

@bp_resultados.route('/ver/<id>', methods =['GET'])
def ver_resultado(id):
    json = objeto_resultado.ver(id)
    return jsonify(json)

@bp_resultados.route('/eliminar/<id>', methods =['DELETE'])
def eliminar_resultado(id):
    json = objeto_resultado.eliminar(id)
    return jsonify(json)