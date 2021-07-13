# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 22:31:45 2019
@author: claudia ferlin
"""
import pandas as pd
import matplotlib.pyplot as plt
'''
O arquivo Excel sonopaiemae registra as horas de sono do pai e da mãe de um bebê durante 
8 semanas, diariamente.
Na planilha mae, estão os registros de horas de sono da mãe e na planilha pai, estão os 
registros de horas de sono do pai.
As planilhas têm cabeçalho (linha 1) e possuem o seguinte formato:
               Dia da semana  e  horas de sono
Na planilha maeSem estão os registros de horas de sono da mãe diariamente durante 8 semanas.
        Esta planilha não têm cabeçalho e possue o seguinte formato:
               Dia da semana+numero da semana  e  horas de sono
               Exemplo: seg2 que significa segunda-feira da segunda semana
'''
#============================================
# Construindo  Series a partir de um arquivo excel
#============================================
# 
#============================================
#       Manipulando a series 
#============================================
#   Utilizar a planilha Mae para criar a Series sMae
#   Utilizar a planilha Pai para criar a Series sPai
#       índice: coluna 0
#		nao tem linha de cabeçalho
#   Observe os 10ºs elementos
#   Observe as medidas princiapis (.describe)
# 
#I.	Criar as series sMae e sPai respectivamente
sPai=pd.read_excel("sonopaiemae.xlsx",sheet_name="pai",index_col=0,header=None,squeeze=True)
sMae=pd.read_excel("sonopaiemae.xlsx",sheet_name="mae",index_col=0,header=None,squeeze=True)

sPaiS=pd.read_excel("sonopaiemae.xlsx",sheet_name="paiSem",index_col=0,header=0,squeeze=True)
sMaeS=pd.read_excel("sonopaiemae.xlsx",sheet_name="maeSem",index_col=0,header=0,squeeze=True)
#============================================
#      APENAS PARA A SERIES sMae:
#============================================
#**********************************************
#III.	Responder as seguintes perguntas:
#**********************************************
#a.	O maior tempo, o menor tempo, o mais frequente e o tempo médio 
print('-----------------------------------------------------')
print("\na. O maior tempo:, o menor tempo:,  o tempo médio:")
print("\nO mais frequente:\n")
print('-----------------------------------------------------')
#b.	O maior tempo, o menor tempo, o mais frequente e o tempo médio por dia da semana 
print('-----------------------------------------------------')
print("\nPor dia da semana:")
print("b. O maior tempo,o menor tempo, tempo médio:")

print("\nLista de tempos mais frequente POR DIA DA SEMANA:\n")
'''
Para resumos por dia da semana:
    1) agrupar pelo index ( como o index só tem um nível --> level = 0)-> g
    2) obter os resumo para cada grupo: g.agg(......)
  Problema: mode não pode ser aplicado sobre os grupos. 
            COMO MOSTRAR o(s) mais frequente(s) por dia???
            
  Possível Estratégia:
      Lembrando que o mode é  com maior  frequência:
          value_counts--> dá a frequência, obter o(s) com maior(es) valores
      criar uma função que:
           recebe os elementos de um grupo, 
           calcula a tabela de frequência e 
           retorna os elementos com maior frequência  
       aplicar esta função em cada grupo
'''       
def maisFreqPorGrupo(s):
    a=s.value_counts()
    m=a.max()
    sMaisFreq=a.loc[a==m]
    return list(sMaisFreq.index) # retorna apenas os índices em formato de lista


g=sMae.groupby(level=0) 
print(g.apply(maisFreqPorGrupo))

print('-----------------------------------------------------')