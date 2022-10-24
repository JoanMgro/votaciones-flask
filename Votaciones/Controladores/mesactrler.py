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
        print("Actualizando candidato con identificador ", id)
        mesa = Candidato(self.repositorio.findById(id))
        mesa.nombre = mesa_data["nombre"]
        mesa.apellido = mesa_data["apellido"]
        mesa.cedula = mesa_data["cedula"]
        mesa.numero_resolucion = mesa_data["numero_resolucion"]

        return self.repositorio.save(candidato)


    def ver(self, id):
        #leer de la DB.
        print("Consultando el Mesa con identificador ", id)
        mesa = Mesa(self.repositorio.findById(id))
        return mesa.__dict__


    def eliminar(self, id):
        print("Eliminando el Mesa con identificador ", id)
        return self.repositorio.delete(id)





