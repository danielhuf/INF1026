# -*- coding: utf-8 -*-
"""
Created on Sun May  3 15:00:52 2020

@author: cf
"""
import pandas as pd
import matplotlib.pyplot as plt

sGastosDia=pd.read_excel("gastosAlimPaiMae.xlsx", header=None, usecols=(1,2),
                      index_col=0,squeeze=True,decimal=',')

sGastosPMDia= pd.read_excel('gastosAlimPaiMae.xlsx',index_col=[0,1],header=0,squeeze=True)

# Responder as seguintes perguntas sobre sGastosDias:

# Qual o total de gastos do Gasparzinho  nos dias úteis (segunda à sexta) e o total no final de semana? Qual a relação percentual entre eles? 

def tipo(x):
    if x in ['Sab','Dom']:
        return 'Fim de Semana'
    return 'Dias Úteis'

g=sGastosDia.groupby(by=tipo)
print('-------------------------')
print(g.agg(sum))
s=g.agg('count')/sGastosDia.size*100
print(s)
print('-------------------------')

# Qual o gasto médio nos dias úteis e no final se semana?
print(g.agg('mean'))
#devo colocar entre aspas, já que não é uma função do python
print('-------------------------')

# Mostre de forma tabular, a quantidade de gastos, a média, mediana, menor valor, maior valor por tipo
print(g.agg(['count','mean','median','min','max']))
print('-------------------------')

# Dividir os valores gastos em 3 grupos: Baixo (até R$ 5,00), Médio (entre R$ 5,01 e R$ 20,00) e Alto (acima de R$ 20,00) e mostrar:
cGastos=pd.cut(sGastosDia,bins=[0,5,20,sGastosDia.max()],labels=['Baixo','Médio','Alto'])
print(cGastos)
print('-------------------------')

#	quantidade de ocorrências em cada grupo
gGastos=sGastosDia.groupby(by=cGastos)
print(gGastos.agg('count'))
print('-------------------------')

#	valor médio,mínimo e máximo de cada grupo
print(gGastos.agg(['mean','min','max']))
print('-------------------------')

#	a soma dos valores em cada grupo e a relação percentual entre eles graficamente 	(gráfico de pizza)
print(gGastos.agg('sum'))
gGastos.agg('count').plot.pie(autopct='%.1f')
print('-------------------------')
