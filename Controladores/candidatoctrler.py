from Modelos.candidato import Candidato

class CandidatoCtrler():
    def __init__(self):
        print(f'Constructor de {self.__class__}')

    def create(self, candidato):
        print('creando candidato')
        obj_candidato = Candidato(candidato)
        return obj_candidato.__dict__

