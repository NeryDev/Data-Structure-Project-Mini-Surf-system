#PARTE DE IMPORTAÇÃO ONDE FOI IMPORTADO DE CADA ARQUIVO AS CLASSES NECESSÁRIAS PARA O PROJETO
from Campeonato import campeonato
from País import Pais
from Prancha import prancha
from Surfista import Surfista
from Praia import praia

#1º SURFISTA PRÉ CRIADO PARA AJUDAR NO PROJETO
n1 = "André Rodrigues".upper()
i1 = 24
camp1 = ["Circuito de Verão", "Cabo Surf", "Campeonato Paraibano de Surf", "Campeonato Brasileiro de Surf"]
pranchas1 = ["FireWire", "DHD"]

#2º SURFISTA PRÉ CRIADO PARA AJUDAR NO PROJETO
n2 = "Gabriel Medina".upper()
i2 = 21
camp2 = ["Circuito de Verão", None, None, "Campeonato Brasileiro de Surf"]
pranchas2 = ["FireWire", "DHD", "Hyren", " Pukas" ]

#A PARTIR DAQUI COMEÇA A INICIAÇÃO DA FICHA DO SURFISTA CRIADO PELO PRÓPRIO USUÁRIO ATRÁVES DO SISTEMA DE INPUT
#É QUAIS CAMPEONATOS ELE IRÁ PARTICIPAR, NOME, IDADE, E AS PRANCHAS QUE O MESMO POSSUI.
print("Seja Bem-Vindo para registrar sua ficha de surfista!")
print("Ficha de Descrição do Surfista:")
n3 = input("Nome: ").upper()
i3 = int(input("Idade: "))
print("Inscrição nos Campeonatos (S para Sim e N para Não)") 
S3camp1 = input("Circuito de Verão(S/N): ").upper()
S3camp2 = input("Cabo Surf(S/N): ").upper()
S3camp3 = input("Campeonato Paraibano de Surf(S/N): ").upper()
S3camp4 = input("Campeonato Brasileiro de Surf(S/N): ").upper()
print("Pranchas do Atleta:")
S3prancha1 = input("FireWIre(S/N): ").upper()
S3prancha2 = input("DHD(S/N): ").upper()
S3prancha3 = input("Hyren(S/N): ").upper()
S3prancha4 = input("Pukas(S/N): ").upper()
camp3 = []
if S3camp1 == "S":
  camp3.append("Circuito de Verão")
if S3camp2 == "S":
  camp3.append("Cabo Surf")
if S3camp3 == "S":
  camp3.append("Campeonato Paraibano de Surf")
if S3camp4 == "S":
  camp3.append("Campeonato Brasileiro de Surf")

pranchas3 = []
if S3prancha1 == "S":
  pranchas3.append("FireWIre")
if S3prancha2 == "S":
  pranchas3.append("DHD")
if S3prancha3 == "S":
  pranchas3.append("Hyren")
if S3prancha4 == "S":
  pranchas3.append("Pukas")
############################################################
print()
print()
print()
#2º SURFISTA CRIADO PELO SISTEMA DE INPUTS, DANDO AS MESMAS INFORMAÇÕES DOS OUTROS 3 SURFISTAS.
print("Ficha de Descrição do Surfista!")
n4 = input("Nome: ").upper()
i4 = int(input("Idade: "))
print("Inscrição nos Campeonatos (S para Sim e N para Não)") 
S4camp1 = input("Circuito de Verão(S/N): ").upper()
S4camp2 = input("Cabo Surf(S/N): ").upper()
S4camp3 = input("Campeonato Paraibano de Surf(S/N): ").upper()
S4camp4 = input("Campeonato Brasileiro de Surf(S/N): ").upper()
print("Pranchas do Atleta:")
S4prancha1 = input("FireWIre(S/N): ").upper()
S4prancha2 = input("DHD(S/N): ").upper()
S4prancha3 = input("Hyren(S/N): ").upper()
S4prancha4 = input("Pukas(S/N): ").upper()
camp4 = []
if S4camp1 == "S":
  camp4.append("Circuito de Verão")
if S4camp2 == "S":
  camp4.append("Cabo Surf")
if S4camp3 == "S":
  camp4.append("Campeonato Paraibano de Surf")
if S4camp4 == "S":
  camp4.append("Campeonato Brasileiro de Surf")

pranchas4 = []
if S4prancha1 == "S":
  pranchas4.append("FireWire")
if S4prancha2 == "S":
  pranchas4.append("DHD")
if S4prancha3 == "S":
  pranchas4.append("Hyren")
if S4prancha4 == "S":
  pranchas4.append("Pukas")
############################################################
#AQUI ESTÁ BASICAMENTE O DATA-BASE E DEFINAÇÃO DOS ATRIBUTOS DOS SURFISTAS ATRAVÉS DA CLASSE 'SURFISTA' APRESENTADA NA FUNÇÃO.
surfista1 = Surfista(n1, i1, camp1, pranchas1)
surfista2 = Surfista(n2, i2, camp2, pranchas2)
surfista3 = Surfista(n3, i3, camp3, pranchas3)
surfista4 = Surfista(n4, i4, camp4, pranchas4)

######################################################################
#A PARTE ONDE COMEÇA OS CAMPEONATOS, APRESENTAMOS 4 CAMPEONATOS PRÉ-EXISTENTES PARA COLOCAR EM PAUTA, OU SEJA, 4 CAMPEONATOS PARA 4 SURFISTAS
print()

campeao1 = input("Campeão do Circuito Verão: ").upper()
premio1 = 2000
surfistas1 = []
surfistas1.append(n1)
surfistas1.append(n2)
if S3camp1 == "S":
    surfistas1.append(n3)
    
if S4camp1 == "S":
    surfistas1.append(n4)
#SISTEMA DE ==S PARA IDENTIFICAÇÃO CASO OS SURFISTAS CRIADOS VÃO SER INTEGRADOS OU NÃO NO CAMPEONATO EM PAUTA

#PRÉ DEFINIDO O PREMIO E O INPUT PARA SABER DO PRÓPRIO USUÁRIO QUEM FOI O CAMPEÃO DESTE CAMPEONATO EDIÇÃO
#APPEND N1 E N2 PARA ADIÇÃO DE GABRIEL MEDINA E ANDRÉ RODRIGUES(DOIS SURFISTAS PRÉ EXISTENTES)



  


campeonato1 = campeonato("Circuito de Verao", "Maresias(SP)",premio1,campeao1,surfistas1)
#/////////////////////////////////////////////////////////////////////////////////////////////////////////
#CAMPEONATO 2:
print()

campeao2 = input("Campeão do Cabo Surf: ").upper()
premio2 = 2000
surfistas2 = []
surfistas2.append(n1)
if S3camp2 == "S":
    surfistas2.append(n3)
if S4camp2 == "S":
    surfistas2.append(n4)

campeonato2 = campeonato("Cabo Surf", "Cabo Branco(PB)",premio2,campeao2,surfistas2)
#////////////////////////////////////////////////////////////////////////////////////////////////////////
print()
#CAMPEONATO 3:

campeao3 = input("Campeão do Campeonato Paraibano de Surf: ").upper()
premio3 = 5000
surfistas3 = []
surfistas3.append(n1)
surfistas3.append(n2)
if S3camp3 == "S":
    surfistas3.append(n3)
if S4camp3 == "S":
    surfistas3.append(n4)
    
campeonato3 = campeonato("Campeonato Paraibano de Surf", "Cabo Branco(PB)",premio3,campeao3,surfistas3)
#///////////////////////////////////////////////////////////////////////////////////////////////
print()
#CAMPEONATO 4:

campeao4 = input("Campeão do Campeonato Brasileiro de Surf: ").upper()
premio4 = 10000
surfistas4 = []
surfistas4.append(n1)
surfistas4.append(n2)
if S3camp4 == "S":
    surfistas4.append(n3)
if S4camp4 == "S":
    surfistas4.append(n4)

campeonato4 = campeonato("Campeonato Brasileiro de Surf", "Itamambuca(SP)",premio4,campeao4,surfistas4)
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#SISTEMA MONTADO PARA SABER A O CAMPEÃO COLOCANDO EM PAUTA SUA IDADE, OU SEJA, SE O CAMPEÃO DA PRIMEIRA EDIÇÃO FOSSE O SURFISTA 1 (ANDRÉ RODRIGUES)
#SUA IDADE SERÁ INPUTADA NO SISTEMA NOS PRINTS FINAIS COMO O CAMPEÃO DA EDIÇÃO MAIS NOVO, VELHO, OU NAS INFO'S EXTRAS COMO SUA IDADE NORMAL
#FOI CRIADO BASICAMENTE UM PARA CADA CAMPEONATO, À FIM DE TESTAR QUAL O CAMPEÃO, E SUA IDADE UTILIZANDO LISTAS COM APPEND.
idadescamp = []
if campeao1 == n1:
  idadescamp.append(i1)
if campeao1 == n2:
  idadescamp.append(i2)
if campeao1 == n3:
  idadescamp.append(i3)
if campeao1 == n4:
  idadescamp.append(i4)

if campeao2 == n1:
  idadescamp.append(i1)
if campeao2 == n2:
  idadescamp.append(i2)
if campeao2 == n3:
  idadescamp.append(i3)
if campeao2 == n4:
  idadescamp.append(i4)

if campeao3 == n1:
  idadescamp.append(i1)
if campeao3 == n2:
  idadescamp.append(i2)
if campeao3 == n3:
  idadescamp.append(i3)
if campeao3 == n4:
  idadescamp.append(i4)

if campeao4 == n1:
  idadescamp.append(i1)
if campeao4 == n2:
  idadescamp.append(i2)
if campeao4 == n3:
  idadescamp.append(i3)
if campeao4 == n4:
  idadescamp.append(i4)
#SISTEMA PARA SABER QUAL O MAIOR E MENOR CAMPEÃO POR QUESTÃO DE IDADE, UTILIZANDO O IDADESCAMP QUE FOI PROVADO EM TODAS AS COMPETIÇÕES COMO EMBASAMENTO, E MIN E MÁX 
#PARA VER O MINIMO(MENOR) E O MÁXIMO(MAIS ALTO) DOS CAMPEÕES.
maiorcamp = (max(idadescamp))
menorcamp = (min(idadescamp))

#MÉTODO CRIADO COLOCADO COMO 0 À FIM DE PÔR UM VALOR FUTURAMENTE NO SISTEMA EM SI.
totals1 = 0
totals2 = 0
totals3 = 0
totals4 = 0

if campeao1 == n1:
    totals1 += premio1
if campeao2 == n1:
    totals1 += premio2
if campeao3 == n1:
    totals1 += premio3
if campeao4 == n1:
    totals1 += premio4

if campeao1 == n2:
    totals2 += premio1
if campeao2 == n2:
    totals2 += premio2
if campeao3 == n2:
    totals2 += premio3
if campeao4 == n2:
    totals2 += premio4

if campeao1 == n3:
    totals3 += premio1
if campeao2 == n3:
    totals3 += premio2
if campeao3 == n3:
    totals3 += premio3
if campeao4 == n3:
    totals3 += premio4

if campeao1 == n4:
    totals4 += premio1
if campeao2 == n4:
    totals4 += premio2
if campeao3 == n4:
    totals4 += premio3
if campeao4 == n4:
    totals4 += premio4
#NESTE CASO FOI CRIADO UMA TIPAGEM DE TENTATIVA DE INPUT DE PREMIAÇÃO PARA CADA NOME DE SURFISTA (N1,N2...)
#NO SISTEMA, SE ELE FOSSE INDENTIFICADO COMO CAMPEÃO DE UMA EDIÇÃO, O SEU TOTAL EM PREMIAÇÃO SERIA ADICIONADO O VALOR OFERECIDO NO CAMPEONATO
#COMO EXEMPLO: MEDINA PODE GANHAR 2K EM UM E 5K E OUTRO, SOMANDO 7K NO PRINT FINAL DELE.

#DEFINIÇÃO DO DATA-BASE DAS PRANCHAS UTILIZANDO O ARGUMENTO CLASSE IMPORTADO DO ARQUIVO PRANCHA.PY
prancha1  = prancha("Firewire",2.54, 1500, "preto")
prancha2  = prancha("DHD",2.50, 1450,"branco")
prancha3  = prancha("Hyren", 2.43, 1200,"azul")
prancha4  = prancha("Pukas", 2.62, 1750,"vermelho")

#DEFINIÇÃO DO DATA-BASE DO PAIS UTILIZANDO O ARGUMENTO PAIS IMPORTADO DO ARQUIVO PAIS.PY
pais = Pais("Brasil", "Português", "Maresias(SP), Cabo Branco(PB), Itamambuca(SP)")

#AQUI FORAM PRÉ-CRIADAS PRAIAS PARA SEREM COLOCADAS NAS COMPETIÇÕES EM QUESTÃO, COM AS PRE-DEFINIÇÕES DE QUANTAS VEZES FORAM COMPETIDAS EM PAUTA, É VISTO O CABO BRANCO
#COMO O MAIS ESCOLHIDO.
praia1 = praia("Maresias(SP)", 1, "Brasil")
praia2 = praia("Cabo Branco(PB)", 2, "Brasil")
praia3 = praia("Itamambuca(SP)", 1, "Brasil")

praiasselec = (max([praia1._ncr, praia2._ncr, praia3._ncr]))
praiamoreselec = ''
if praiasselec == 2:
  praiamoreselec = praia2._nomepraia
else:
  praiamoreselec = praia1._nomepraia , praia3._nomepraia

#SISTEMA PARA PÔR A PRAIA MAIS SELECIONADA ATRAVÉS DE ELEMENTOS DE CLASS E ATRIBUTO.
  

############################################################
print()
print()
print()
print()
print()
print("A menor idade de um campeão foi {}, e a maior idade de um campeão foi {}." .format(menorcamp, maiorcamp))
print()
print() 
print("Surfistas inscritos nos campeonatos:")
print("Surfistas de Circuito Verão: {}" .format(surfistas1))
print("Surfistas de Cabo Surf: {}" .format(surfistas2))
print("Surfistas de Campeonato Paraibano de Surf: {}" .format(surfistas3))
print("Surfistas de Campeonato BR de Surf: {}" .format(surfistas4))
print()
print()
print("Praia mais selecionada:")
print("A praia mais selecionada foi: {}".format(praiamoreselec))
print()
print()
print("Ganho dos Surfistas em todos os campeonatos:")
print("Ganhos totais do {} = R${}" .format(n1,totals1))
print("Ganhos totais do {} = R${}" .format(n2,totals2))
print("Ganhos totais do {} = R${}" .format(n3,totals3))
print("Ganhos totais do {} = R${}" .format(n4,totals4))
print()
print()

vextra = input("Se você quiser saber mais informações digite S para SIM  e N para Não:").upper()
#COLOCAMOS INFORMAÇÕES EXTRAS COMO AS DUAS FUNCIONALIDADES NECESSÁRIAS E PEDIDAS NO PROJETO, PORÉM, COMO SE REALMENTE FOSSE ALGO PARA O USUÁRIO VER CASO QUEIRA.
if vextra == "S":
  print("Informações Extras")
  print()
  print()
  print()
  print("Veja aqui quais as marcas das pranchas de cada surfista:")
  print()
  print()
  print("{} possui pranchas destas marcas: {}".format(n1, pranchas1))
  print("{} possui pranchas destas marcas: {}".format(n2, pranchas2))
  print("{} possui pranchas destas marcas: {}".format(n3, pranchas3))
  print("{} possui pranchas destas marcas: {}".format(n4, pranchas4))
  print()
  print()
  print("Idade dos Surfistas:")
  print()
  print()
  print("{} possui {} anos" .format(n1, i1))
  print("{} possui {} anos" .format(n2, i2))
  print("{} possui {} anos" .format(n3, i3))
  print("{} possui {} anos" .format(n4, i4))
  print()
  print()
  print()
  print("Fim do Programa.")
else:
  print("Fim do Programa.")














