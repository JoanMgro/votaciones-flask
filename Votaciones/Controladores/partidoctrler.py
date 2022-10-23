from Votaciones.Modelos.partido import partido

class partidoctrler():
    def __init__(self):
        print(f'Constructor de {self.__class__}')

    def create(self, partido):
        print('creando Partido')
        obj_partido = partido(partido)
        return obj_partido.__dict__

    def ver(self, id):
        #Query de la DB.
        lista_partido = [
            {'id': 1, 'nombre': 'union', 'lema': 'pueblo'},
            {'id': 2, 'nombre': 'futuro', 'lema': 'nuestro'}
        ]
        for obj in lista_partido:
            if obj.get('id') == id:
                obj_partido = partido(obj)
                return obj_partido.__dict__
        else:
                resp = {'Message' : 'Partido no encontrado'}
                return  resp

    def modificar(self, id, dato_partido):
        print(f'modificando Partido con id {id}')
        obj_partido = partido(dato_partido)
        return obj_partido.__dict__

    def listar(self):
        print('Listando Partidos')
        #Query de la DB.
        lista_partido = [
            {'id' : 1, 'nombre': 'union','lema': 'pueblo'},
            {'id' : 2, 'nombre': 'futuro','lema': 'nuestro'}
        ]
        return lista_partido

    def eliminar(sef, id):
        lista_partido = [
            {'id': 1, 'nombre': 'union', 'lema': 'pueblo'},
            {'id': 2, 'nombre': 'futuro', 'lema': 'nuestro'}
        ]
        for obj in lista_partido:
            if obj.get('id') == id:
                resp = {'Message': 'Partido eliminado'}
                return resp
        else:
            resp = {'Message': 'Partido no encontrado'}
            return resp



