# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:59:42 2020

@author: -
"""
#Daniel Stulberg Huf - 1920468
#prof. Claudia Ferlin - Turma 33C

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',None)

print('----------------------------------------------')
print('1) As observações com valores ausentes devem ser eliminadas')
dfDados=pd.read_excel('ChickWeight.xlsx',decimal=',',sheet_name='DadosBiometricos',header=0)
dfDados.dropna(axis=0,how='any',inplace=True)
print(dfDados)
print('----------------------------------------------')

print('----------------------------------------------')
print('2) A coluna “ Número do Pinto” deve ser renomeada para IDENT, as demais devem ser colocadas em maiúsculo')
dfDados.rename(columns={'Numero do Pinto':'IDENT','Peso':'PESO','Dias':'DIAS','Dieta':'DIETA'},inplace=True)
print(dfDados)
print('----------------------------------------------')

print('----------------------------------------------')
print('3) Apresente a média e a mediana dos pintinhos no dia 4')
f1=dfDados.loc[dfDados['DIAS']==4]
print(f1['PESO'].mean())
print(f1['PESO'].median())
print('----------------------------------------------')

print('----------------------------------------------')
print('4) Some ao peso do dia 4 do pintinho de IDENT = 41, 3000 (outlier). Apresente a média e a mediana no dia 4 novamente')
indice=list(f1.loc[f1['IDENT']==41].index)
f1.loc[indice[0]]['PESO']+=3000
print(f1['PESO'].mean())
print(f1['PESO'].median())
print('----------------------------------------------')

print('----------------------------------------------')
print('5) Apresente o maior peso atingido por cada pintinho')
gIdent=dfDados.groupby('IDENT')
print(gIdent['PESO'].agg('max'))
print('----------------------------------------------')

print('----------------------------------------------')
print('6) Apresente os dados dos pintos organizados por TEMPO')
print(dfDados.sort_values(by=['DIAS','IDENT']))  #Coloquei identificação como segundo critério para facilitar a vizualização
print('----------------------------------------------')

print('----------------------------------------------')
print('7) Apresente os dados dos pintos no último dia observado organizados por PESO')
dfDados.set_index('IDENT',inplace=True)
ultimoDia=dfDados['DIAS'].max()
f2=dfDados.loc[dfDados['DIAS']==ultimoDia]
print(f2.sort_values(by='PESO'))
#Para o caso da interpretação ser o último dia DE CADA pintinho:
#diasMax=list(gIdent['DIAS'].agg('idxmax').values)
#dfDiasMax=dfDados.loc[diasMax]
#dfDados.set_index('IDENT',inplace=True)
#print(dfDiasMax.sort_values('PESO'))
print('----------------------------------------------')

print('----------------------------------------------')
print('8) Apresente o peso médio por ESPECIE')
dfEsp=pd.read_excel('ChickWeight.xlsx',decimal=',',sheet_name='Especie',header=0,index_col=0)
dfDados['ESPECIE']=dfEsp
gEsp=dfDados.groupby('ESPECIE')
print(gEsp['PESO'].agg('mean'))
print('----------------------------------------------')

print('----------------------------------------------')
print('9) Apresente o peso médio por DIETA')
gDieta=dfDados.groupby('DIETA')
print(gDieta['PESO'].agg('mean'))
print('----------------------------------------------')

print('----------------------------------------------')
print('10) Apresente as medidas descritivas dos pintos ao longo do tempo')
gDias=dfDados.groupby('DIAS')
print(gDias['PESO'].agg(['min','max','mean','median','sum']))
#Também poderia ter colocado gDias['PESO'].agg('describe')
print('----------------------------------------------')

print('----------------------------------------------')
print('11) Qual ESPECIE teve a maior média de crescimento de peso? E maior média de peso final?')
dfDif=gIdent['PESO'].agg(['min','max'])
dfDif['Dif']=dfDif['max']-dfDif['min']
dfDif['Esp']=dfEsp
gEspDif=dfDif.groupby('Esp')
print(gEspDif['Dif'].agg('mean').idxmax())
print(gEspDif['max'].agg('mean').idxmax())
print('----------------------------------------------')

print('----------------------------------------------')
print('12)Qual DIETA teve a maior média de crescimento de peso? E maior média de peso final?')
gDieta=dfDados['DIETA'].groupby(level=0)
dfDif['DIETA']=gDieta.max()
gDietDif=dfDif.groupby('DIETA')
print(gDietDif['Dif'].agg('mean').idxmax())
print(gDietDif['max'].agg('mean').idxmax())
print('----------------------------------------------')

print('----------------------------------------------')
print('13) Apresente a tabela de frequência de PESOS POR DIETA')
print(pd.crosstab(dfDados['PESO'],dfDados['DIETA']))
#Fazendo por outra maneira
#gDie=dfDados.groupby('DIETA')
#print(gDie['PESO'].agg('value_counts'))
print('----------------------------------------------')

print('----------------------------------------------')
print('14) Apresente a tabela de frequência de PESOS POR ESPECIE POR DIETA')
print(pd.crosstab(dfDados['PESO'],[dfDados['ESPECIE'],dfDados['DIETA']]))
#gEspDie=dfDados.groupby(['ESPECIE','DIETA'])
#print(gEspDie['PESO'].agg('value_counts'))
print('----------------------------------------------')

print('----------------------------------------------')
print('15) Apresente a quantidade pintos por DIETA/ESPECIE ( tabcross)')
print(pd.crosstab(dfDados['DIETA'],dfDados['ESPECIE']))
print('----------------------------------------------')

print('----------------------------------------------')
print('16) Apresente o peso médio, a mediana do peso, peso máximo por DIETA/ESPECIE. Qual DIETA/ESPECIE, apresentou ao final o maior peso?')
gDieEsp=dfDados.groupby(['DIETA','ESPECIE'])
dfRes=gDieEsp['PESO'].agg(['mean','median','max'])
print(dfRes)
print(dfRes['max'].idxmax())
print('----------------------------------------------')

print('----------------------------------------------')
print('17) Mostre, graficamente, as relações entre: ( gráficos de dispersão)')
print('a. o TEMPO e o PESO')
dfDados.plot.scatter(x='DIAS',y='PESO',figsize=(10,4),title='Relação Tempo x Peso')
plt.show()
print('b. a DIETA e o PESO')
dfDados.plot.scatter(x='DIETA',y='PESO',figsize=(10,4),title='Relação Dieta x Peso')
plt.show()
print('----------------------------------------------')

print('----------------------------------------------')
print('18) Crie 4 categorias de tempo de vida (FAIXA_ETARIA): até os 8 dias (inclusive), de 8'
'até 20 dias(inc), de 20 até 36 (inc) e de 36 em diante. Rotule as categorias como'
'RN, BEBE, JOVEM e MADURO. Inclua a nova coluna FAIXA_ETARIA.')
cFaixa=pd.cut(dfDados['DIAS'],bins=[0,8,20,36,dfDados['DIAS'].max()],labels=['RN','BEBE','JOVEM','MADURO'],include_lowest=True)
dfDados['FAIXA_ETARIA']=cFaixa
print(dfDados)
print('----------------------------------------------')

print('----------------------------------------------')
print('19) Exiba as medidas descritivas das faixas etárias.')
gFaixa=dfDados.groupby('FAIXA_ETARIA')
print(gFaixa['PESO'].agg(['max','min','mean','median','sum']))
#Também poderia ter colocado gFaixa['PESO'].agg('describe')
print('----------------------------------------------')

print('----------------------------------------------')
print('20)Qual a ESPECIE vencedora em cada faixa etária?')
def maisFreqPorGrupo(faixa):
    f=faixa.value_counts()
    m=f.max()
    sMaisFreq=f.loc[f==m]
    return list(sMaisFreq.index)
print(gFaixa['ESPECIE'].apply(maisFreqPorGrupo))
#Entendo "espécie vencedora" como aquela que é a mais frequente, porém
# se o vencedor for a espécie de maior peso, seria assim:
#print(pd.crosstab(dfDados['ESPECIE'],dfDados['FAIXA_ETARIA'],values=dfDados['PESO'],aggfunc='max').idxmax())
print('----------------------------------------------')

print('----------------------------------------------')
print('21)Qual a DIETA vencedora em cada faixa etária?')
print(gFaixa['DIETA'].apply(maisFreqPorGrupo))
#Entendo "espécie vencedora" como aquela que é a mais frequente, porém
# se o vencedor for a dieta com maior peso, seria assim:
#print(pd.crosstab(dfDados['DIETA'],dfDados['FAIXA_ETARIA'],values=dfDados['PESO'],aggfunc='max').idxmax())
print('----------------------------------------------')

print('----------------------------------------------')
print('22) Crie 2 categorias de peso (PESO) : até a média (inclusive) , de média em diante.'
'Rotule as categorias como ABAIXO, ACIMA. Inclua a nova coluna FAIXA_PESO.')
cPeso=pd.cut(dfDados['PESO'],bins=[0,dfDados['PESO'].mean(),dfDados['PESO'].max()],labels=['ABAIXO','ACIMA'],include_lowest=True)
dfDados['FAIXA_PESO']=cPeso
print(dfDados)
print('----------------------------------------------')

print('----------------------------------------------')
print('23) Apresente a tabela de frequência de ESPECIE/FAIXA DE PESO por DIETA/FAIXA_ETARIA')
print(pd.crosstab([dfDados['ESPECIE'],dfDados['FAIXA_PESO']],[dfDados['DIETA'],dfDados['FAIXA_ETARIA']]))
print('----------------------------------------------')



