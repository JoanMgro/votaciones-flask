from Votaciones.Modelos.resultado import Resultado

class ResultadoCtrler():
    def __init__(self):
        print(f'Constructor de {self.__class__}')

    def index(self):
        print('Listando Resultados')
        #leer de la DB.
        lista_resultados = [
            {'id': 1, 'numero_mesa' : 4, 'id_partido': 12},
            {'id': 2, 'numero_mesa' : 5, 'id_partido': 76},
            {'id': 3, 'numero_mesa' : 8, 'id_partido': 42},
        ]
        return lista_resultados

    def create(self, resultado):
        print('creando ')
        obj_resultado = Resultado(resultado)
        return obj_resultado.__dict__

    def modificar(self, id, dato_resultado):
        print(f'modificando resultado con id {id}')
        obj_resultado = Resultado(dato_resultado)
        return obj_resultado.__dict__

    def ver(self, id):
        #leer de la DB.
        lista_resultados = [
            {'id': 1, 'numero_mesa' : 4, 'id_partido': 12},
            {'id': 2, 'numero_mesa' : 5, 'id_partido': 76},
            {'id': 3, 'numero_mesa' : 8, 'id_partido': 42},
        ]
        for obj in lista_resultados:
            if obj.get('id') == id:
                obj_resultado = Resultado(obj)
                return obj_resultado.__dict__
        else:
                resp = {'Message' : 'resultado no encontrado'}
                return  resp


    def eliminar(sef, id):
        lista_resultados = [
            {'id': 1, 'numero_mesa' : 4, 'id_partido': 12},
            {'id': 2, 'numero_mesa' : 5, 'id_partido': 76},
            {'id': 3, 'numero_mesa' : 8, 'id_partido': 42},
        ]
        for obj in lista_resultados:
            if obj.get('id') == id:
                resp = {'Message': 'resultado eliminado'}
                return resp
        else:
            resp = {'Message': 'resultado no encontrada'}
            return resp