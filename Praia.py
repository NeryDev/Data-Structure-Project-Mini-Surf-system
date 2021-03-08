class praia:
    def __init__(self, nomepraia, ncr, pais):
        self._nomepraia = nomepraia
        self._ncr = ncr
        self._pais = pais

@property
def nomepraia(self):
    return self._nomepraia

@property
def ncr(self):
    return self._ncr

@property
def pais(self):
    return self._pais

@nomepraia.setter
def nomepraia(self, novo_nomepraia):
    self._nomepraia = novo_nomepraia

@ncr.setter
def ncr(self, novo_ncr):
    self._ncr = novo_ncr

@pais.setter
def pais(self, novo_pais):
    self.pais = novo_pais

def __str__(self):
    return  "Nome:{}, Número de Campeonatos Realizados:{}, País:{}" .format(self.nomepraia, self.ncr, self.pais)


