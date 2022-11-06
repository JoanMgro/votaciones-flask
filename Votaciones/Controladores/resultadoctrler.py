from Votaciones.Modelos.resultado import Resultado
from Votaciones.Modelos.candidato import Candidato
from Votaciones.Modelos.mesa import Mesa
from Votaciones.Repositorios.ResultadoRepositorio import ResultadoRepositorio
from Votaciones.Repositorios.MesaRepositorio import MesaRepositorio
from Votaciones.Repositorios.CandidatoRepositorio import CandidatoRepositorio


class ResultadoCtrler():
    def __init__(self):

        self.resultado_repo = ResultadoRepositorio()
        self.mesa_repo = MesaRepositorio()
        self.candidato_repo = CandidatoRepositorio()

    def index(self):
        print("Controlador Listando todos los resultados")
        return self.resultado_repo.findAll()


    """
    Asignacion mesa y candidato a resultado al crear un resultado
    """
    def create(self, data_resultado, id_mesa, id_candidato):
        print("Controlador para Creando un resultado")
        resultado = Resultado(data_resultado)
        candidato = Candidato(self.candidato_repo.findById(id_candidato))
        mesa = Mesa(self.mesa_repo.findById(id_mesa))


        resultado.candidato = candidato
        resultado.mesa = mesa
        return self.resultado_repo.save(resultado)



    """
    Modificación de Resultado (Candidato y mesa)
    """
    def modificar(self, id, data_resultado, id_mesa, id_candidato):
        print("Actualizando Resultado con id ", id)
        resultado = Resultado(self.resultado_repo.findById(id))
        resultado.votos = data_resultado["votos"]
        #otros campos de resultados que deben de ir.
        candidato = Candidato(self.candidato_repo.findById(id_candidato))
        mesa = Mesa(self.mesa_repo.findById(id_mesa))
        resultado.candidato = candidato
        resultado.mesa = mesa
        return self.resultado_repo.save(resultado)



    def ver(self, id):
        print("Consultando resultado con identificador ", id)
        resultado = Resultado(self.resultado_repo.findById(id))
        return resultado.__dict__

    def eliminar(self, id):
        print("Eliminando resultado con id ", id)
        return self.resultado_repo.delete(id)

    def consultaResultadosMesa(self, id_mesa):
        print("Consultando todos los Resultados Mesa")
        return self.resultado_repo.getResultadosMesa(id_mesa)


    def consultarSumaVotosMesa(self, id_mesa):
        print("Consultando todos los votos Mesa")
        return self.resultado_repo.sumatoriaVotos(id_mesa)


    def consultarTotalVotosCandidatosMesas(self):
        print("Consultando max voto mesa")
        return self.resultado_repo.getVotacionTotalCandidatos()

    def consultarListaParticipacionMesa(self):
        print("Consultando participacion por mesa")
        return self.resultado_repo.getListaParticipacionMesas()

    # def consultarVotacionPartidos(self):
    #     print("Consultando votacion partidos")
    #     return self.resultado_repo.getVotacionPartidos()
    #
