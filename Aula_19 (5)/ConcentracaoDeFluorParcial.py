# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 22:31:45 2019

@author: claudia ferlin
"""
import pandas as pd
import matplotlib.pyplot as plt
'''
O artigo  “Qualidade da água para consumo humano e concentração de fluoreto”( link http://ref.scielo.org/37cqsn) afirma que: 'as temperaturas nas capitais brasileiras indicam que o fluoreto deveria variar de 0,6 a 0,9 mg/L para prevenir cárie dentária. .... A ingestão diária de água com fluoreto em concentração > 0,9 mg/L representa risco à dentição em menores de oito anos de idade e os consumidores deveriam ser expressamente informados desse risco.' 
Durante um mês, diariamente foi medido o nível de concentração de fluoreto em duas estações de tratamentos distintas. Os resultados estão no arquivo RegEst.xlsx, nas planilhas Est1 e Est2 respectivamente.
a)	Construa as Series sEst1 e sEst2
b)	Responda as seguintes perguntas para cada Series:
Responda as seguintes perguntas: 
Por estação:
a.	Qual a concentração média?
b.	Quantos dias houve concentração abaixo da média?
c.	Qual a concentração mediana?
d.	Qual a menor e maior concentração? Em quais dias?
e.	Quantos dias estavam com a concentração correta (entre 0,6 a 0,9)?
f.	Construa  e exiba a tabela de frequência considerando as seguintes faixas: 
•	Abaixo:  concentração até 0,6 (exclusive) 
•	Normal: concentração de 0,6 a 0,91 (exclusive) 
•	Acima: concentração  acima de 0,91
Obs: Exiba a tabela de frequência na ordem das faixas 

Entre as estações:
a.	Em quantos dias a Est1 teve concentração inferior à Est2? Quais foram?
b.	Em quais dias a Est1 e a Est2 estiveram simultaneamente com a concentração correta? 
'''
#============================================
# Construindo  Series a partir de um arquivo excel
#============================================
# 
#============================================
#       Manipulando a series 
#============================================
#   Utilizar a planilha Est1 para  criar a Series sEst1
#       índice: usar automático  e construir uma nova series com índice==dias do mês
#       valor: coluna 0
#		não tem linha de cabeçalho
#   Observe os 20ºs elementos
#   Observe as medidas princiapis (.describe)
# 
#   


sEst1=pd.read_excel("RegEst.xlsx",sheet_name='Est1', squeeze=True,header=None)
sEst1=pd.Series(sEst1.values,index=range(1,31))
sEst2=pd.read_excel("RegEst.xlsx",sheet_name="Est2", squeeze=True,header=None)
sEst2=sEst2.reindex(range(1,31))

sSH1=pd.read_excel("RegEst.xlsx",sheet_name='SensorHoraEst1', squeeze=True,header=None)
sSH1=pd.Series(sSH1.values,index=range(1,31))
sSH2=pd.read_excel("RegEst.xlsx",sheet_name="SensorHoraEst2", squeeze=True,header=None)
sSH2=pd.Series(sSH2.values,index=range(1,31))

# Mostre os valores, índices e tamanho da sEst1
print('\n-----------------------------------------------------\n')
print("\nvalores, índices e tamanho da sEst1\n")

print('\n-----------------------------------------------------\n')

#============================================
#       Por Estação --> sEst1 e sEst2
#============================================

# a.	Qual a concentração média?
print('\n-----------------------------------------------------\n')
print("\na.Qual a concentração média?\n")
print('sEst1:{} sEst2:{}'.format(sEst1.mean(),sEst2.mean()))
print('\n-----------------------------------------------------\n')

# opção a)
print("\na.Qual a concentração média com Estações juntas por concat?\n")
sEstJuntas=pd.concat({'Est1':sEst1,'Est2':sEst2})
sCoMed= sEstJuntas.mean(level=0)
print(sCoMed.apply('{:.2f}'.format))

#b.	Quantos dias houve concentração abaixo da média?
print('\n-----------------------------------------------------\n')
print("\nb.	Quantos dias houve concentração abaixo da média?\n")
sAb1= sEst1.loc[sEst1<sEst1.mean()].count() # (sEst1<sEst1.mean()).sum()
sAb2= sEst2.loc[sEst2<sEst2.mean()].size
print('sEst1:{} sEst2:{}'.format(sAb1,sAb2))
print('\n-----------------------------------------------------\n')

#b.	Quantos dias houve concentração abaixo da média, usando sEstJuntas?
print('Quantos dias houve concentração abaixo da média, usando sEstJuntas')
print((sEstJuntas<sCoMed.mean()).sum(level=0))

#c.	Qual a concentração mediana?
print('\n-----------------------------------------------------\n')
print("\nc.	Qual a concentração mediana?\n")
print('sEst1:{} sEst2:{}'.format(sEst1.median(),sEst2.median()))
print('\n-----------------------------------------------------\n')

#d.	Qual a menor e maior concentração? Em quais dias?
print('\n-----------------------------------------------------\n')
print("\nd.	Qual a menor e maior concentração? Em quais dias?\n")
maiorEst1=sEst1.max()
menorEst1=sEst1.min()
sMaiorDiasEst1=sEst1.loc[sEst1==maiorEst1]
sMenorDiasEst1=sEst1.loc[sEst1==menorEst1]

maiorEst2=sEst2.max()
menorEst2=sEst2.min()
sMaiorDiasEst2=sEst2.loc[sEst2==maiorEst2]
sMenorDiasEst2=sEst2.loc[sEst2==menorEst2]

print('Máximo sEst1:{} - Nos dias:{} / Mínimo sEst1: {} - Nos dias: {}'.format(maiorEst1,list(sMaiorDiasEst1.index),menorEst1,list(sMenorDiasEst1.index)))
print('Máximo sEst2:{} - Nos dias:{} / Mínimo sEst2: {} - Nos dias: {}'.format(maiorEst2,list(sMaiorDiasEst2.index),menorEst2,list(sMenorDiasEst2.index)))
print('\n-----------------------------------------------------\n')

#e.	Quantos dias estavam com a concentração correta (entre 0,6 a 0,9)?
print('\n-----------------------------------------------------\n')
print("\ne.	Quantos dias estavam com a concentração correta (entre 0,6 a 0,9)?\n")
filtro1= (sEst1>=0.6) & (sEst1<=0.9)
filtro2= (sEst2>=0.6) & (sEst2<=0.9)
sCE1= sEst1.loc[filtro1]
qt1= sCE1.count()
sCE2=sEst2.loc[filtro2]
qt2= sCE2.count()
print('sEst1:{} sEst2:{}'.format(qt1,qt2))
print('\n-----------------------------------------------------\n')

#f.	Construa  e exiba a tabela de frequência considerando as seguintes faixas: 
#•	Abaixo:  concentração até 0,6 (exclusive) 
#•	Normal: concentração de 0,6 a 0,91 (exclusive) 
#•	Acima: concentração  acima de 0,91
print('\n-----------------------------------------------------\n')
print("\nf.	Tabela de Frequência nas faixas: abaixo, normal, acima: \n")
lIndex=['Abaixo','Normal','Acima']
sCatEst1= pd.cut(sEst1,bins=[0,0.6,0.91,sEst1.max()],labels=lIndex)
sCatEst2= pd.cut(sEst2,bins=[0,0.6,0.91,sEst2.max()],labels=lIndex)
sCatQtE1=sCatEst1.value_counts()
sCatQtE2=sCatEst2.value_counts()
sCatQtE1=sCatQtE1.reindex(lIndex)
sCatQtE2=sCatQtE2.reindex(lIndex)
print('sEst1:\n{}\n\n sEst2:\n{}'.format(sCatQtE1,sCatQtE2))
print('\n-----------------------------------------------------\n')

#============================================
#       Entre as estações sEst1 e sEst2
#============================================

#a.	Em quantos dias a Est1 teve concentração inferior à Est2? Quais foram?
print('\n-----------------------------------------------------\n')
print("\nEm quantos dias a Est1 teve concentração inferior à Est2? Quais foram?\n")
filtro1= sEst1<sEst2
sE1MenorE2= sEst1.loc[filtro1]
qtE1MenorE2=sE1MenorE2.count()
print('Quantos? {}'.format(qtE1MenorE2))

print('\nQuais foram? {}'.format(list(sE1MenorE2.index)))
print('\n-----------------------------------------------------\n')

#b.	Em quais dias a Est1 e a Est2 estiveram com a concentração correta? 
print('\n-----------------------------------------------------\n')
print("\nb.	Em quais dias as duas estações estiveram SIMULTANEAMENTE com a concentração correta?\n")
# Construir sAux, com os valores de sCE1 e os índices de sCE2
#    Os índices inexistentes em sCE1 ficam com valor NaN
sAux=sCE1.loc[sCE2.index].copy()
# Filtar elementos com valor de sAux
filtro=sAux.notnull()
print('\nSeries com os dias corretos de  Est1 e Est2 simultanemanete\n{}'.format(sAux.loc[filtro]))
print('\nSó os dias: {}'.format(list((sAux.loc[filtro]).index)))
print('\n-----------------------------------------------------\n')
