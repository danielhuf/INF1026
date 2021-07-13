import pandas as pd

# Use 3 casas decimais na saída
pd.set_option("display.precision", 3)

sNota= pd.read_excel("NotaFilme.xlsx", header=0,usecols=[1,3],index_col=0,squeeze=True)
print(sNota)

#Medidas Gerais- Criando uma Series com as Medidas Principais

l=[sNota.count(),sNota.mean(),sNota.median(),sNota.min(), sNota.max()]
print("\nI) Medidas Gerais:\n")
sMedC=pd.Series(l,index=('qt','média','mediana','min','max'))
print("\nI.a) Medidas Gerais Com Ausentes:\n{}".format(sMedC))

# Medidas eliminando ausentes
sSem=sNota.dropna()

l=(sSem.count(),sSem.mean(),sSem.median(),sSem.min(), sSem.max())
sMedS=pd.Series(l,index=('qt','média','mediana','min','max'))

print("\nI.b)Medidas Gerais Eliminando Ausentes:\n{}".format(sMedS))
#Pode-se observar que os métodos desprezaram o NaN

print('\nI.c) Diferença das Medidas Gerais eliminando valores ausentes\n:{}'.format(sMedC-sMedS))

########################################################################

# Medidas substituindo ausentes pelo menor valor
#completando valores ausentes com a nota mínima
sAusMin=sNota.fillna(sNota.min())
l=(sAusMin.count(),sAusMin.mean(),sAusMin.median(),sAusMin.min(), sAusMin.max())
sMedAusMin=pd.Series(l,index=('qt','média','mediana','min','max'))

print("\nII.a)Medidas Gerais Substituindo Ausentes pelo menor valor:\n{}".format(sMedAusMin))

print('\nII.b) Diferença das Medidas Gerais substituindo valores ausentes pelo menor valor:\n{}'.format(sMedAusMin-sMedC))

########################################################################

# Medidas substituindo ausentes pela nota média

#completando valores ausentes com a média
sAusMean=sNota.fillna(sNota.mean())
l=(sAusMean.count(),sAusMean.mean(),sAusMean.median(),sAusMean.min(), sAusMean.max())
sMedAusMean=pd.Series(l,index=('qt','média','mediana','min','max'))

print("\nIII.a)Medidas Gerais Substituindo Ausentes pela Média:\n{}".format(sMedAusMean))

print('\nIII.b) Diferença das Medidas Gerais substituindo valores ausentes pela Média\n:{}'.format(sMedAusMean-sMedC))

lMedidas=['count','median','mean','min','max']
########################################################################

# Medidas por gênero
print("------------------------------")
print("\nIV) Medidas por Gênero:\n")
gGen=sNota.groupby(level=0)
sMedGen=gGen.agg(lMedidas)
print("IV.a)Medidas Gerais Agrupadas por Gênero{}\n".format(sMedGen))
print("------------------------------")

# agrupando sMedia: valores ausentes preenchidos com a nota média 

sMedia=sNota.fillna(sNota.mean())
g1=sMedia.groupby(level=0)
sMed1=g1.agg(lMedidas)
print("IV.b)Medidas por Gênero valores ausentes preenchidos com a nota média:\n{}".format(sMed1))

g=sNota.groupby(level=0)
print(g.groups)
f=g.agg('mean')
print(sNota.fillna(f))

#Tambem existe essa opção
def altera(s):
    return s.fillna(s.mean())

print(g.transform(altera))
print("------------------------------")
#Observa-se que dá no mesmo

# diferença entre as medidas com e sem valores ausentes 
print('\nIV.c) Diferença das Medidas Gerais substituindo valores ausentes pela Média\n:{}'.format(sMed1-sMedGen))
print("------------------------------")

########################################################################
# completando valores ausentes com a nota média por Gênero

def altera2(g):
    med=g.mean()
    g=g.fillna(med)
    return g

print("------------------------------")
print("V.a) Completando valores ausentes com a nota média por Gênero via transform")
s2=gGen.transform(altera2)

g2=s2.groupby(level=0)
sMed2=g2.agg(lMedidas)
print("{}\n".format(sMed2))
print("------------------------------")

print("V.b) Completando valores ausentes com a nota média por Gênero via fillna")
f2=gGen.agg('mean')
s2=sNota.fillna(f2)

g2=s2.groupby(level=0)
sMed2=g2.agg(lMedidas)
print("{}\n".format(sMed2))
print("------------------------------")
#Observa-se que dá no mesmo

# diferença entre as medidas dos grupos com e sem valores ausentes 
print('\nV.c) Diferença das Medidas substituindo valores ausentes pela Média Geral e do Grupo\n:{}'.format(sMed2-sMed1))
print("------------------------------")

# completando valores ausentes com a nota mínima do grupo

sMedia=sNota.fillna(sNota.min())
g1=sMedia.groupby(level=0)
sMed1=g1.agg(lMedidas)
print("VI.b)Medidas por Gênero valores ausentes preenchidos com a nota mínima:\n{}".format(sMed1))
print("------------------------------")

#  Exercício I:
# Construa uma series relacionando o assento com a nota
sAssNota= pd.read_excel("NotaFilme.xlsx", header=0,usecols=[0,3],index_col=0,squeeze=True)
print(sAssNota)
print("------------------------------")

# Agrupe-os pela fileira (a,b,c) 
def separaFileira(valor):
    return valor[0]
gFileira=sAssNota.groupby(by=separaFileira)

# Complete os  valores ausentes pela média do grupo 
def preenche(s):
    return s.fillna(s.mean())
sAssNota=gFileira.transform(preenche)
print(sAssNota)
print("------------------------------")

# Complete os  valores ausentes pelo valor mínimo do grupo 
def preenche2(s):
    return s.fillna(s.min())
sAssNota=gFileira.transform(preenche2)
print(sAssNota)
print("------------------------------")

# Mostre as medidas principais
g=sAssNota.groupby(by=separaFileira)
print(g.agg(lMedidas))
print("------------------------------")

#  Exercício II:
# Construa uma series relacionando a idade com a nota
sIdNota= pd.read_excel("NotaFilme.xlsx", header=0,usecols=[2,3],index_col=0,squeeze=True)
print(sIdNota)
print("------------------------------")


# Crie 3 classes: menores(até 17), jovens( até 35), demais( 36 em diante)
def idade(x):
    if x<=17:
        return 'menores'
    elif x<=35:
        return 'jovens'
    else:
        return 'demais'
gIdNota=sIdNota.groupby(by=idade)
print(gIdNota.groups)
print("------------------------------")

# Complete os  valores ausentes pela média da classe
def completa1(s):
    return s.fillna(s.mean())
sIdNota=gIdNota.transform(completa1)
print(sIdNota)
print("------------------------------")

# Complete os  valores ausentes pelo valor mínimo da classe
def completa2(s):
    return s.fillna(s.min())
sIdNota=gIdNota.transform(completa2)
print(sIdNota)
print("------------------------------")

 # Mostre as medidas principais
g=sIdNota.groupby(by=idade)
print(g.agg(lMedidas))
print("------------------------------")
