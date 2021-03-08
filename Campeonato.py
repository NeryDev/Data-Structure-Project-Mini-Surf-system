class campeonato:
    def __init__(self, nomecamp,praiacamp,premio,campeao,surfistas):
        self._nomecamp = nomecamp
        self._campeao = campeao
        self._praiacamp = praiacamp
        self._premio = premio
        self._surfistas = surfistas
    
@property
def nomecamp(self):
    return self._nomecamp

@property
def campeao(self):
    return self._campeao

@property
def praiacamp(self):
    return self._praiacamp

@property
def premio(self):
    return self._premio

@property
def surfistas(self):
    return self._surfistas

@nomecamp.setter
def nomecamp(self, novo_nomecamp):
    self._nomecamp = novo_nomecamp

@campeao.setter
def campeao(self, novo_campeao):
    self._campeao = novo_campeao

@praiacamp.setter
def praiacamp(self, nova_praiacamp):
    self._praiacamp = nova_praiacamp

@premio.setter
def premio(self, novo_premio):
    self._premio = novo_premio

@surfistas.setter
def surfistas(self, novo_surfistas):
    self._surfistas = novo_surfistas


def __str__(self):
    return  "Nome:{}, Praia:{}, Premio:{}, Campeão:{}, Surfistas:{}" .format(self.nomecamp, self.praiacamp, self.premio, self.campeao, self.surfistas)

