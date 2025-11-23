from src.pessoa import Pessoa


class Motoca:

    def __init__(self, potencia: int):
        self.potencia = potencia
        self.tempo = 0
        self.pessoa = None

    def getPessoa(self):
        return self.pessoa

    def getTempo(self):
        return self.tempo

    def getPotencia(self):
        return self.potencia

    def subir(self, pessoa: Pessoa):
        if self.getPessoa() == None:
            self.pessoa = pessoa
            return True
        return False

    def descer(self):
        if self.getPessoa() != None:
            self.pessoa = None
            return True
        return False

    def colocarTempo(self, tempo: int):
        if tempo > 0:
            self.tempo += tempo
            return True
        return False

    def dirigir(self, tempo: int):
        pessoa = self.getPessoa()
        if self.getTempo() > 0 and self.getPessoa() != None and pessoa.getIdade()<=10:
            if self.getTempo() >tempo:
                self.tempo -= tempo
                return True
            else:
                self.tempo = 0
                return True
        else: return False

    def buzinar(self):
        if self.getPessoa() != None:
            pem = 'P'
            for i in range(0, self.potencia):
                pem += 'e'
            pem += 'm'
            return pem
        return ''