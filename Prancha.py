class prancha:
    def __init__(self, marcap, comprimentop, valorp, corp):
        self._marcap = marcap
        self._comprimentop = comprimentop
        self._valorp = valorp
        self._corp = corp

@property
def marcap(self):
    return self._marcap

@property
def comprimentop(self):
    return self._comprimentop

@property
def valorp(self):
    return self._valorp

@property
def corp(self):
    return self._corp

@marcap.setter
def marcap(self, nova_marcap):
    self._marcap = nova_marcap

@comprimentop.setter
def comprimentop(self, novo_comprimentop):
    self._comprimentop = novo_comprimentop

@valorp.setter
def valorp(self, novo_valorp):
    self._valorp = novo_valorp

@corp.setter
def corp(self, nova_corp):
    self._corp = nova_corp

def __str__(self):
    return  "Marca:{}, Comprimento:{}, Valor: R${}, Cor:{}" .format(self.marcap, self.comprimentop, self.valorp, self.corp)
