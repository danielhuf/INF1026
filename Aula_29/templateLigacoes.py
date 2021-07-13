# -*- coding: utf-8 -*-
"""
Nome: Daniel Stulberg Huf				                          
Matricula: 1920468
Turma: 33C
Professor: Joisa
"""
import pandas as pd
import matplotlib.pyplot as plt

print('*******************************************')
print('---------------- Questao Series ----------------')
print('*******************************************')
sLig = pd.read_excel('ligacoes.xlsx',index_col=0,header=0,squeeze=True)

print('---------------- item a) ------------------')
print('\nTempo total das ligacoes:')
print(sLig.sum())

print('\nMediana das ligacoes:')
print(sLig.sort_values().median())

print('---------------- item b) ------------------')
print('\nDestino das ligacoes com tempo abaixo da mediana:')
f1=sLig.loc[sLig<sLig.median()]
print(f1.index.values)

print('---------------- item c) ------------------')
print('\nTabela de frequencia das faixas:')
cFaixa=pd.cut(sLig,bins=[0,180,300,sLig.max()])
print(cFaixa.value_counts())

print('---------------- item d) ------------------')
print('\nEstatisticas por destino da ligacao:')
print('\tGraficamente (barras), tempo total das ligacoes:')
gDestino=sLig.groupby(level=0)
tot=gDestino.agg('sum')
tot.plot.bar()
plt.show()
print('\tTempo medio das ligacoes:')
print(gDestino.agg('mean'))

print('---------------- item e) ------------------')
print('\nGrafico de pizza com o percentual de ligaçoes para fora do Brasil:')
#Poderia usar sLig.index.str.contais('+55',regex=False)
def brasil(x):
    if x[:3]=='+55':
        return 'Dentro do Brasil'
    else:
        return 'Fora do Brasil'
sInv=pd.Series(sLig.index,sLig.values)
sBr=sInv.apply(brasil)
sBr.value_counts().plot.pie(autopct='%.1f')
plt.show()

print('---------------- item f) ------------------')
print('\nA forma de ligacao com maior tempo total das ligaçoes e a com maior quantidade de ligacoes:')
def forma(x):
    return x[-1]
sForma=sInv.apply(forma)
invForma=pd.Series(sForma.index,sForma.values)
gForma=invForma.groupby(level=0)
print(gForma.agg('sum').idxmax())
print(gForma.agg('count').idxmax())