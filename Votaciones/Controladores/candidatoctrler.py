from Votaciones.Modelos.candidato import Candidato
from Votaciones.Repositorios.CandidatoRepositorio import CandidatoRepositorio

class CandidatoCtrler():
    def __init__(self):
        print('Creando el controlador de Candidato')
        self.repositorio = CandidatoRepositorio()

    def index(self):
        print("Controlador Listando todos los candidatos")
        return self.repositorio.findAll()

    def create(self, candidato):
        print("Controlador para Creando un candidato")
        can = Candidato(candidato)
        return self.repositorio.save(can)

    def modificar(self, id, candidato_data):
        print("Actualizando candidato con identificador ", id)
        candidato = Candidato(self.repositorio.findById(id))
        candidato.nombre = candidato_data["nombre"]
        candidato.apellido = candidato_data["apellido"]
        candidato.cedula = candidato_data["cedula"]
        candidato.numero_resolucion = candidato_data["numero_resolucion"]

        return self.repositorio.save(candidato)


    def ver(self, id):
        #leer de la DB.
        print("Consultando el candidato con identificador ", id)
        candidato = Candidato(self.repositorio.findById(id))
        return candidato.__dict__


    def eliminar(self, id):
        print("Eliminando el candidato con identificador ", id)
        return self.repositorio.delete(id)





