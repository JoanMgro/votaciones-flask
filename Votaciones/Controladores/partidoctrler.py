from Votaciones.Modelos.partido import Partido
from Votaciones.Repositorios.PartidoRepositorio import PartidoRepositorio
class PartidoCtrler():
    def __init__(self):
        print('Creando el controlador de Partido')
        self.repositorio = PartidoRepositorio()

    def index(self):
        print("Controlador Listando todos los Partidos")
        return self.repositorio.findAll()

    def create(self, partido):
        print("Controlador para Creando un Partido")
        par = Partido(partido)
        return self.repositorio.save(par)

    def modificar(self, id, partido_data):
        print("Actualizando Partido con identificador ", id)
        partido = Partido(self.repositorio.findById(id))
        # partido.id = partido_data["id"] #creo que esto es un error ya hay un id.
        partido.nombre = partido_data["nombre"]
        partido.lema = partido_data["lema"]


        return self.repositorio.save(partido)


    def ver(self, id):
        #leer de la DB.
        print("Consultando el Partido con identificador ", id)
        partido = Partido(self.repositorio.findById(id))
        return partido.__dict__


    def eliminar(self, id):
        print("Eliminando el Partido con identificador ", id)
        return self.repositorio.delete(id)





