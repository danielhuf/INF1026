# -*- coding: utf-8 -*-
"""
Nome: Daniel Stulberg Huf				                          
Matricula: 1920468
Turma: 33C
Professor: Joisa
"""

import pandas as pd
import matplotlib.pyplot as plt

'''
DataFrame e Series
'''
dfImoveis = pd.read_excel("Imoveis.xlsx",sheet_name="ImoveisEmOut",index_col=0)

print("-------------------------------------")
print('\Item a\n')
print('\nInformacoes do DataFrame criado')
print(dfImoveis.index.size)
print(dfImoveis.columns.size)
print(list(dfImoveis.columns))
print(dfImoveis.dtypes)
print(dfImoveis.head(5))
print(dfImoveis.tail(5))
print("-------------------------------------")    

print("-------------------------------------")
print('\nItem b\n')
print("tabela de frequência da Regiao numericamente e tabela de frequência relativa "\
      "(percentual) da variável Regiao")
gReg=dfImoveis.groupby('Regiao')
tabFreq=gReg.agg('count')['Bairro']
print(tabFreq)
tabFreq.plot.pie(autopct='%.1f')
plt.show()
print("-------------------------------------")  

print("-------------------------------------")
print('\nItem c\n')
print('\nCompara Imoveis em Botafogo com 2 quartos')
print("-------------------------------------")
f1=(dfImoveis['Bairro']=='BOTAFOGO') & (dfImoveis['Quartos']==2)
dfBot=dfImoveis.loc[f1]
print('Preço mínimo',dfBot['Preco'].min())
print(dfBot.loc[dfBot['Preco']==dfBot['Preco'].min()])

print("-------------------------------------")
print('\nItem d\n')
print("preco Metro Quadrado do RJ")
dfCop1=dfImoveis.copy()
dfCop1.dropna(inplace=True)
dfCop2=dfImoveis.copy()
dfCop2['Area']=dfImoveis['Area'].fillna(12*dfImoveis['Quartos']+40)
precoPorM21=dfCop1['Preco'].sum()/dfCop1['Area'].sum()
precoPorM22=dfCop2['Preco'].sum()/dfCop2['Area'].sum()
print('Copia 1',precoPorM21)
print('Copia 2',precoPorM22)
print("-------------------------------------")

print("-------------------------------------")
print('\nItem e\n')
print("Totais bairros")
gBai=dfImoveis.groupby('Bairro')
print(gBai['Preco'].agg(['count','max','min','mean']))
#Poderia colocar d['mean']=d['mean'].apply('{:.2f}'.format)
print("-------------------------------------")    

print("-------------------------------------")
print('\nItem f\n')
print("DF com a coluna PrPorM2")
dfImoveis.dropna(inplace=True)
dfImoveis['PrPorM2']=dfImoveis['Preco']/dfImoveis['Area']
print(dfImoveis.head(5))
print("-------------------------------------")  
