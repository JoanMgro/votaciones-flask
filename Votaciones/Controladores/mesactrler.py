from Votaciones.Modelos.mesa import Mesa

class MesaCtrler():
    def __init__(self):
        print(f'Constructor de {self.__class__}')

    def index(self):
        print('Listando Mesas')
        #leer de la DB.
        lista_mesas = [
            {'id': 1, 'cantidad_inscritos' : 4},
            {'id': 2, 'cantidad_inscritos' : 5},
            {'id': 3, 'cantidad_inscritos' : 8},
        ]
        return lista_mesas

    def create(self, mesa):
        print('creando mesa')
        obj_mesa = Mesa(mesa)
        return obj_mesa.__dict__

    def modificar(self, id, dato_mesa):
        print(f'modificando mesa con id {id}')
        obj_mesa = Mesa(dato_mesa)
        return obj_mesa.__dict__

    def ver(self, id):
        #leer de la DB.
        lista_mesas = [
            {'id': 1, 'cantidad_inscritos' : 4},
            {'id': 2, 'cantidad_inscritos' : 5},
            {'id': 3, 'cantidad_inscritos' : 8},
        ]
        for obj in lista_mesas:
            if obj.get('id') == id:
                obj_mesa = Mesa(obj)
                return obj_mesa.__dict__
        else:
                resp = {'Message' : 'mesa no encontrado'}
                return  resp


    def eliminar(sef, id):
        lista_mesas = [
            {'id': 1, 'cantidad_inscritos' : 4},
            {'id': 2, 'cantidad_inscritos' : 5},
            {'id': 3, 'cantidad_inscritos' : 8},
        ]
        for obj in lista_mesas:
            if obj.get('id') == id:
                resp = {'Message': 'mesa eliminado'}
                return resp
        else:
            resp = {'Message': 'mesa no encontrada'}
            return resp







