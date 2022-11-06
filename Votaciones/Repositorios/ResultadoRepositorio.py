from Votaciones.Repositorios.RepositorioInterface import RepositorioInterface
from Votaciones.Modelos.resultado import Resultado


from bson import ObjectId

class ResultadoRepositorio(RepositorioInterface[Resultado]):

    def getResultadosMesa(self, id_mesa): #me da la lista de resultados por mesa de cada candidato. no tiene orden.
        consulta = {'mesa.$id': ObjectId(id_mesa)}
        return self.query(consulta)

    def getVotacionTotalCandidatos(self): #me da lista de candidatos total con su votacion total.

        consulta = {
            "$group": {
                "_id": "$candidato",
                "total_votos": {
                    "$sum" : "$votos"
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }
        pipeline = [ consulta]
        return self.queryAggregation(pipeline)


#materia -> candidato
#estudiante -> mesa
#incripcion -> resultado
    def notaPromedio(self, id_materia):
        consulta1 = {
            "$match": {"materia.$id": ObjectId(id_materia)}
        }
        consulta2 = {
            "$group": {
                "_id": "$materia",
                "promedio": {
                    "$avg": "$nota_final"
                }
            }
        }
        pipeline = [consulta1, consulta2]
        return self.queryAggregation(pipeline)

    def sumatoriaVotos(self, id_mesa): #suma de votos (participiacion x mesa)
        consulta1 = {
            "$match": {"mesa.$id": ObjectId(id_mesa)}
        }
        consulta2 = {
            "$group": {
                "_id": "$mesa.$id",
                "votos_mesa": {
                "$sum": "$votos"
                }
            }
        }
        pipeline = [consulta1, consulta2]
        return self.queryAggregation(pipeline)


    def getListaParticipacionMesas(self): #me da lista de particiopacion por mesa

        consulta = {
            "$group": {
                "_id": "$mesa.$id",
                "total_votos": {
                    "$sum" : "$votos"
                },

            }
        }

        pipeline = [ consulta]

        return self.queryAggregation(pipeline)

    # def getVotacionPartidos(self): #me da lista
    #
    #     consulta = {
    #         "$group": {
    #             "_id": "candidato.partido.id",
    #             "total_votos": {
    #                 "$sum" : "$votos"
    #             },
    #
    #         }
    #     }
    #     pipeline = [ consulta]
    #     return self.queryAggregation(pipeline)