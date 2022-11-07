from Votaciones.Repositorios.RepositorioInterface import RepositorioInterface
from Votaciones.Modelos.resultado import Resultado


from bson import ObjectId
from bson.son import SON

class ResultadoRepositorio(RepositorioInterface[Resultado]):

    # def getResultadosMesa(self, id_mesa): #me da la lista de resultados por mesa de cada candidato. no tiene orden.
    #     consulta = {'mesa.$id': ObjectId(id_mesa)}
    #     return self.query(consulta)

    def getVotacionTotalCandidatos(self): #me da lista de candidatos total con su votacion total.
        #http://127.0.0.1:9999/resultados/votos-total-candidatos
        consulta = {
            "$group": {
                "_id": { "mesa" :"$mesa.$id", "cand":"$candidato.$id"},
                "info_mesa": {"$first": "$$ROOT.mesa"},
                "info_candidato" : {"$first" : "$$ROOT.candidato"},
                "votos_candidato" : {"$max": "$votos"}
            }
        }

        consulta2 = {
            "$sort": SON([("votos_candidato", -1)], )

        }


        pipeline = [consulta, consulta2]
        return self.queryAggregation(pipeline)


#materia -> candidato
#estudiante -> mesa
#incripcion -> resultado
    def getResultadosMesa(self, id_mesa): #(checked) me da los votos de todos candidatos en una mesa
        #http://127.0.0.1:9999/resultados/mesa/635c30973973c3dc48e8546c
        consulta1 = {
            "$match": {"mesa.$id": ObjectId(id_mesa)}
        }

        consulta2 = {
            "$group": {
                "_id": "$candidato.$id",
                #"votos_candidato" : {"$max" : "$votos"},
                "votos_candidato" : {"$first" : "$$ROOT.votos"},
                "info_candidato": {"$first": "$$ROOT.candidato"}

                }
            }


        consulta3 = {
            "$sort": SON([("votos_candidato", -1)], )
            # "$sort": {"$votos" : "-1"}

        }

        pipeline = [consulta1,  consulta2, consulta3, ]
        print(pipeline)
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


    ########


    def getListaParticipacionMesas(self): #me da lista de particiopacion por mesa ordenados de menor a mayor (checked)
        #http://127.0.0.1:9999/resultados/participacion-mesa

        consulta = {
            "$group": {
                "_id": "$mesa.$id",
                "info_mesa" : {"$first" : "$$ROOT.mesa"},
                "total_votos": {
                    "$sum" : "$votos"
                },

            },

        }

        consulta2 = {
            "$sort": SON([("total_votos", 1)], )
        }


        pipeline = [ consulta, consulta2]

        return self.queryAggregation(pipeline)
