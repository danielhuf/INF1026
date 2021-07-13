# -*- coding: utf-8 -*-
"""
autor: Joisa/Claudia
Tempo Final de Semana
groupby
"""
"""
Perguntas sobre o clima no 1º FDS em 2018:
a) Temperatura maxima no FDS em cada cidade.
b) Vento Mínimo, Máximo e Medio em cada cidade
c) Cidade em que, na media, há mais vento
d) Total de dias chuvosos por cidade
e) Cidade(s) com mais dias de chuva
f) Quantas e quais cidade(s) com  SOL no sabado
g) Por dia: cidade(s) com temperatura maxima no dia
h) Quantas cidades começaram o 1º FDS com sol e terminaram sem sol? Quais foram?
    DICA: Crie uma coluna numérica para representar cada tipo de Céu/dia Semana
i) Quais tiveram o FDS todo de sol?
j) Qual a região com mais dias ensolarados? Mostrar a região de cada cidade
        Incluir a região da cidade (sul ou sudeste)
k) Indexar  por região/cidade/dia da semana, e responder:
    1) quantos dias sem sol ( nublado ou chuvoso) por região
    2) quantos dias sem sol ( nublado ou chuvoso) por dia da semana em cada região


Relacionando o clima no 1º FDS em 2017 com o de 2018:    
1) Construir um dataframe dfTempo2017 a partir do arquivo climaFDS2017.xlsx ( 1ª linha --> colunas)
2) Quantas cidades começaram o 1º FDS de 2017 com sol e terminaram sem sol? 
3) Quais foram?
4) Foram as mesmas de 2018?
5) Quais tiveram o FDS todo de sol?
"""
import pandas as pd
import matplotlib.pyplot as plt

'''
Criar o dataframe dfTempo a partir do arquivo climaFDS2018.xlsx,
primeira coluna como indice e primeira linha como columns
Exibir  as informacoes (info), colunas e index e sumarização de colunas numéricas')
''' 
print('\n-----------------------------------------------------')
print('1- DF  dfTempo:')
dfTempo=pd.read_excel('climaFDS2018.xlsx',decimal=',',header=0,index_col=0)
print(dfTempo)
print(dfTempo.info())

print('\n-----------------------------------------------------')
print('\nPara responder as perguntas a e b e´interessante agrupar ou indexar dados por cidade')
print('\n-----------------------------------------------------')
print('\n1-Exibir dados de cada cidade')
gCidade=dfTempo.groupby('CIDADE')
print(gCidade.agg('describe'))
    
print('\n-----------------------------------------------------')
print('\nExibir dados do rio de janeiro ')    
print('\n2-Rio de Janeiro')
print(gCidade.get_group('rio de janeiro'))

print('\n-----------------------------------------------------')
print('\nRESPOSTA da pergunta A (Temperatura Maxima por Cidade)')
print('\n3-So Temperatura maxima por cidade')
print(gCidade['TEMPERATURA'].agg('max'))
print('\n-----------------------------------------------------')
print('\n4-So Temperatura maxima por cidade e o dia de maxima ')
print(gCidade['TEMPERATURA'].agg(['max','idxmax']))

print('\n-----------------------------------------------------')
print('\nRESPOSTA da pergunta B (Vento Mínimo, Máximo e Medio por Cidade)')
print('\n5-Medidas de Vento por cidade - Lembre-se de renomear as colunas')
d=gCidade['VENTO'].agg(['min','max','mean'])
d.rename(columns={'min':'Mínimo','max':'Máximo','mean':'Médio'},inplace=True)
d.columns.name='VENTO'
print(d)

print('\n-----------------------------------------------------')
print('\nRESPOSTA da pergunta C: cidade em que na media ha mais vento')
print('\n6-Cidade em que na media há mais vento ')
print(gCidade['VENTO'].agg('mean').idxmax())

print('\n-----------------------------------------------------')
print('\nRESPOSTA da pergunta D: Total de dias chuvosos por cidade')
print('\n7-Total de dias chuvosos por cidade')
f1=dfTempo.loc[dfTempo['CEU']=='CHUVOSO']
gCidChuv=f1.groupby('CIDADE')
print(gCidChuv['CEU'].agg('count'))

print('\n-----------------------------------------------------')
print('\nRESPOSTA da pergunta E')
print('\n8-Cidade(s) com mais dias de chuva e quantos dias de chuva')
freq=gCidChuv['CEU'].agg('count')
print(freq.loc[freq==freq.max()])

print('\n-----------------------------------------------------')
print('\nRESPOSTA da pergunta F')
print('\n9-Quantas e quais cidade(s) com  SOL no sabado ')
dSab=dfTempo.loc['sab']
dSabSol=dSab.loc[dSab['CEU']=='SOL']
print(dSabSol['CIDADE'].values.size)
print(list(dSabSol['CIDADE'].values))

print('\n-----------------------------------------------------')
print('\nRESPOSTA da pergunta G')
print('\n10-Por dia: Cidade(s) com temperatura maxima no dia')
dfTempo.reset_index(inplace=True)
dfTempo.set_index('CIDADE',inplace=True)
gDia=dfTempo.groupby('DIA')
print(gDia['TEMPERATURA'].agg('idxmax'))

print('\n-----------------------------------------------------')
print('\nRESPOSTA da pergunta H')
print('\n11-Quantas cidades começaram o 1º FDS com sol e terminaram sem sol? Quais foram?')
def numera(x):
    if x['DIA']=='sex' and x['CEU']=='SOL':
        return 1
    else:
        return 0
dfTempo['NUM']=dfTempo.apply(numera,axis=1)
gCid=dfTempo.groupby(level=0)
veredito=gCid['NUM'].agg('sum')
resp=veredito.loc[veredito==1]
print(resp.index.size)
print(list(resp.index))

print('\n-----------------------------------------------------')
print('\nRESPOSTA da pergunta I')
print('\n12-Quais tiveram o FDS todo de sol?')
def numera2(x):
    if x['CEU']=='SOL':
        return 1
    else:
        return 0
dfTempo['NUM']=dfTempo.apply(numera2,axis=1)
gCid=dfTempo.groupby(level=0)
veredito=gCid['NUM'].agg('sum')
resp2=veredito.loc[veredito==3]
print(list(resp2.index))

print('\n-----------------------------------------------------')
print('\nRESPOSTA da pergunta J')
print('\n13-Mostrar  a região de cada cidade')
dfTempo.reset_index(inplace=True)
def detReg(x):
    if x['CIDADE']!='porto alegre' and x['CIDADE']!='curitiba' and x['CIDADE']!='florianopolis':
        return 'sudeste'
    else:
        return 'sul'
dfTempo['REG']=dfTempo.apply(detReg,axis=1)
gCid=dfTempo.groupby('CIDADE')
print(gCid['REG'].agg('max'))

print('\n14-Qual a região com mais dias ensolarados?')
gReg=dfTempo.groupby('REG')
d=gReg['NUM'].agg('sum')
print(list(d.loc[d==d.max()].index))

print('\n-----------------------------------------------------')
print('\nRESPOSTA da pergunta K')
print('  quantos dias sem sol ( nublado ou chuvoso) por região')
f2=dfTempo.loc[dfTempo['CEU']!='SOL']
gReg=f2.groupby('REG')
print(gReg['CEU'].agg('count'))

print('quantos dias sem sol ( nublado ou chuvoso) por dia da semana em cada região')
gRegDia=f2.groupby(['REG','DIA'])
print(gRegDia['CEU'].agg('count'))
