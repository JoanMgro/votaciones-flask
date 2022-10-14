from Modelos.candidato import Candidato

class CandidatoCtrler():
    def __init__(self):
        print(f'Constructor de {self.__class__}')

    def index(self):
        print('Listando Candidatos')
        #leer de la DB.
        lista_canditatos = [
            {'id' : 1111, 'nombre': 'Juan'},
            {'id' : 2222, 'nombre': 'Pedro'},
            {'id' : 3333, 'nombre': 'Jose'},
        ]
        return lista_canditatos

    def create(self, candidato):
        print('creando candidato')
        obj_candidato = Candidato(candidato)
        return obj_candidato.__dict__

    def modificar(self, id, dato_candidato):
        print(f'modificando candidato con id {id}')
        obj_candidato = Candidato(dato_candidato)
        return obj_candidato.__dict__

    def ver(self, id):
        #leer de la DB.
        lista_canditatos = [
            {'id' : 1111, 'nombre': 'Juan'},
            {'id' : 2222, 'nombre': 'Pedro'},
            {'id' : 3333, 'nombre': 'Jose'},
        ]
        for obj in lista_canditatos:
            if obj.get('id') == id:
                obj_candidato = Candidato(obj)
                return obj_candidato.__dict__
        else:
                resp = {'Message' : 'Candidato no encontrado'}
                return  resp


    def eliminar(sef, id):
        lista_canditatos = [
            {'id': 1111, 'nombre': 'Juan'},
            {'id': 2222, 'nombre': 'Pedro'},
            {'id': 3333, 'nombre': 'Jose'},
        ]
        for obj in lista_canditatos:
            if obj.get('id') == id:
                resp = {'Message': 'Candidato eliminado'}
                return resp
        else:
            resp = {'Message': 'Candidato no encontrado'}
            return resp







