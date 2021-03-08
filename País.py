class Pais:
    def __init__(self, nomepais, lingua, praias):
        self._nomepais = nomepais
        self._lingua = lingua
        self._praias = praias

@property
def nomepais(self):
    return self._nomepais

@property
def lingua(self):
    return self._lingua

@property
def praias(self):
    return self.praias

@nomepais.setter
def nomepais(self, novo_nomepais):
    self._nomepais = novo_nomepais

@lingua.setter
def lingua(self, nova_lingua):
    self._lingua = nova_lingua

@praias.setter
def praias(self, nova_praias):
    self._praias = nova_praias

def __str__(self):
    return  "Nome:{}, Lingua:{}, Praias:{}" .format(self.nomepais, self.lingua, self.praias)