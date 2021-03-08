class Surfista:
    def __init__(self, nomesurf, idadesurf, campeonatos = [], pranchas = []):
        self._nomesurf = nomesurf
        self._idadesurf = idadesurf
        self._campeonatos = campeonatos
        self._pranchasurf = pranchasurf

@property
def nomesurf(self):
    return self._nomesurf

@property
def idadesurf(self):
    return self._idadesurf

@property
def campeonatos(self):
    return self._campeonatos

@property
def pranchasurf(self):
    return self._pranchasurf

@nomesurf.setter
def nomesurf(self, novo_nomesurf):
    self._nomesurf = novo_nomesurf

@idadesurf.setter
def idadesurf(self, nova_idadesurf):
    self._idadesurf = nova_idadesurf

@campeonatos.setter
def campeonatos(self, novo_campeonato):
    self._campeonatos = novo_campeonato

@pranchasurf.setter
def pranchasurf(self, nova_pranchasurf):
    self._pranchasurf = nova_pranchasurf


def __str__(self):
    saida1 = ""
    saida2 = ""

    for i in range (len(self.campeonatos)):
        saida1 = saida1 + self.campeonatos[i]
    for c in range (len(self.pranchasurf)):
        saida2 = saida2 + self.pranchasurf[c]
    
    return  "Nome:{}, Idade:{}, Campeonatos:{}, Pranchas:{}" .format(self.nomesurf, self.idadesurf, saida1,saida2)