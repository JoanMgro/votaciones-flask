from Votaciones.Modelos.mesa import Mesa
from Votaciones.Repositorios.MesaRepositorio import MesaRepositorio

class MesaCtrler():
    def __init__(self):
        print('Creando el controlador de Mesa')
        self.repositorio = MesaRepositorio()

    def index(self):
        print("Controlador Listando todos los Mesas")
        return self.repositorio.findAll()

    def create(self, mesa):
        print("Controlador para Creando un Mesa")
        mes = Mesa(mesa)
        return self.repositorio.save(mes)

    def modificar(self, id, mesa_data):
        print("Actualizando mesa con identificador ", id)
        mesa = Mesa(self.repositorio.findById(id))
        mesa.numero = mesa_data["numero"]
        mesa.cantidad_inscritos = mesa_data["cantidad_inscritos"]


        return self.repositorio.save(mesa)


    def ver(self, id):
        #leer de la DB.
        print("Consultando el Mesa con identificador ", id)
        mesa = Mesa(self.repositorio.findById(id))
        return mesa.__dict__


    def eliminar(self, id):
        print("Eliminando el Mesa con identificador ", id)
        return self.repositorio.delete(id)





