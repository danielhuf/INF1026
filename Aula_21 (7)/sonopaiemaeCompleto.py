'''
NOME: Daniel Stulberg Huf - 1920468
TURMA: 33C
'''

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

print('Series sPai:')
print(sPai.head(10))
print(sPai.describe())
print('-----------------------------------------------------')
print('Series sMae:')
print(sMae.head(10))
print(sMae.describe())
print('-----------------------------------------------------')
print('Series sPaiS:')
print(sPaiS.head(10))
print(sPaiS.describe())
print('-----------------------------------------------------')
print('Series sMaeS:')
print(sMaeS.head(10))
print(sMaeS.describe())
print('-----------------------------------------------------')

#II. Há repetição nos índices, como saber quais os valores possíveis (metodo unique)
print('-----------------------------------------------------')
print("\n Valores dos Índices sem repetição\n")
lInd=sMae.index.unique()
print(lInd)
print('-----------------------------------------------------')
#============================================
#      APENAS PARA A SERIES sMae:
#============================================
#**********************************************
#III.	Responder as seguintes perguntas:
#**********************************************
#a.	O maior tempo, o menor tempo, o mais frequente e o tempo médio 
print('-----------------------------------------------------')
print("\na. O maior tempo:, o menor tempo:,  o tempo médio:\n")
print(sMae.max())
print(sMae.min())
print(sMae.mean())
print("\nO mais frequente:\n")
print(sMae.mode().values)
print('-----------------------------------------------------')
#b.	O maior tempo, o menor tempo, o mais frequente e o tempo médio por dia da semana 
print('-----------------------------------------------------')
print("\nPor dia da semana:")
print("b. O maior tempo,o menor tempo, tempo médio:")
print(sMae.max(level=0))
print(sMae.min(level=0))
print(sMae.mean(level=0))
print('-----------------------------------------------------')
#Exibindo graficamente em ordem de dia (reindex) as 3 informaçoes
#Use graficos diferentes para cada uma das informações
sMae.max(level=0).plot.line(linestyle='--',linewidth=3.0)
plt.show()
sMae.min(level=0).plot.barh(width=0.5)
plt.show()
sMae.mean(level=0).plot.pie(figsize=(8,8),autopct='%.1f')
plt.show()
print('-----------------------------------------------------')
#c.	Qual o dia da semana com menor tempo médio de sono (e se houver mais de um?)
print('-----------------------------------------------------')
print("\nc.Qual o dia da semana com menor tempo médio de sono ")
print("\nc.i)Um deles: \n")
print(sMae.idxmin())
print("\nc.ii)Todos: \n")
print(sMae.loc[sMae==sMae.min()].index.values)
print('-----------------------------------------------------')
#**********************************************
# d.	Filtrando:
#**********************************************
#i.	Consertar os valores negativos, isto é, torná-los positivos.  
#########################
#  Versão 1) - pelo apply
#########################
print('-----------------------------------------------------')
print("\nd.i)Por apply: Consertando os valores negativos\n")
def conserta(x):
    if x<0:
        return -x
    else:
        return x
print(sMae.apply(conserta))
print('-----------------------------------------------------')
#########################
#  Versão 2) - por filtro
#########################
print('-----------------------------------------------------')
print("\nd.i)Por filtro: Consertando os valores negativos\n")
sMae.loc[sMae<0]=-1*(sMae.loc[sMae<0])
print(sMae)
print('-----------------------------------------------------')
#ii.	O maior tempo, o menor tempo (ambos com os dias que os registraram))
print('-----------------------------------------------------')

print("\nd.ii) O maior tempo: {}  - Nos dias:{}".format(sMae.max(),sMae.loc[sMae==sMae.max()].index.unique().values))
print("\nd.ii) O menor tempo: {} - Nos dias:{} ".format(sMae.min(),sMae.loc[sMae==sMae.min()].index.unique().values))
print('-----------------------------------------------------')
#iii.	Quantos dias com menos horas de sono que a média?
print('-----------------------------------------------------')

print("\niii.	Quantos dias com menos  horas de sono que a média?")
print(sMae.loc[sMae<sMae.mean()].size)
print('-----------------------------------------------------')
#iv.Comparando com a sPai, quantos dias o pai teve mais horas de sono que a mãe?
print('-----------------------------------------------------')

print("\niv.Quantos dias o pai teve mais horas de sono que a mãe?")
print(sPai.loc[sPai>sMae].size)
print('-----------------------------------------------------')
#v.	Comparando com a sPai, em quais dias da semana, o pai teve, em média, 
#mais horas de sono que a mãe?
print('-----------------------------------------------------')
sPaiMed=sPai.mean(level=0)
sMaeMed=sMae.mean(level=0)
print("\nv.Em quais dias da semana, o pai teve, em média, mais horas de sono " \
      "que a mãe?")
print(sPaiMed.loc[sPaiMed>sMaeMed].index.values)
print('-----------------------------------------------------')

#**********************************************
# e.	Categorizando:
#**********************************************
'''
e.	Categorizando por duração do sono:
	Pouco-Dias até 4 horas de sono 
	Abaixo -Dias com 4 a 6 horas de sono (inclusive)
        Normal - Dias com 6 a 8 horas de sono (inclusive)
	Acima - Dias com mais de 8 horas de sono
'''
cMae=pd.cut(sMae,bins=[0,4,6,8,sMae.max()],labels=['Pouco','Abaixo','Normal','Acima'])
#Exiba a tabela de frequência por categoria e o percentual de dias por categoria
print('-----------------------------------------------------')
print("\ne.i) Tabela de Frequência em cada categoria:\n")
print(cMae.value_counts())
print("\ne.ii) Tabela de Frequência com índices na ordem correta em cada categoria:\n")
print(cMae.value_counts().reindex(['Pouco','Abaixo','Normal','Acima']))
print("\ne.iii) Percentual de dias por categoria:\n")
print(cMae.value_counts()*100/cMae.value_counts().sum())
print('-----------------------------------------------------')

#**********************************************
# f.	Agrupando por dia da semana
#**********************************************

#f.i.a)Qual o maior tempo, o menor tempo e o tempo médio por dia da semana? 
print('-----------------------------------------------------')
print("\nf.i.a) Qual O maior tempo, o menor tempo e o tempo médio por dia da semana?")
gMae=sMae.groupby(level=0)
print(gMae.agg(['max','min','mean']))
#f.i.b) Mostre, por dia da semana, a quantidade de registros em cada categoria de duração do sono 
print('-----------------------------------------------------')
print("\nf.i.b) Tabela de frequência por dia da semana/duração do sono")
gMaeCat=sMae.groupby(by=[pd.Grouper(level=0),cMae])
print(gMaeCat.agg('value_counts'))
print('-----------------------------------------------------')
#f.ii Qual a diferença, por dia da semana, entre o tempo médio e o tempo mínimo da semana?
print('-----------------------------------------------------')
print("\nf.ii) Qual a diferença, por dia da semana, entre o tempo médio e o tempo " \
      "mínimo da semana?")
print(gMae.agg('mean')-gMae.agg('min'))
print('-----------------------------------------------------')
#f.iii Qual a diferença, entre dias úteis e fds, do tempo médio e o tempo mínimo?
print('-----------------------------------------------------')
def tipoDia(g):
    if g in ['sab','dom']:
        return 'fds'
    else:
        return 'dias úteis'
gMaeDias=sMae.groupby(by=tipoDia)
print("\nf.iii)Qual a diferença, entre dias úteis e fds, do tempo médio e o tempo mínimo?\n")
print(gMaeDias.agg('mean')-gMaeDias.agg('min'))
print('-----------------------------------------------------')
#f.iv.Exiba a lista de tempos de sono inferiores a 5h, por dia da semana
print('-----------------------------------------------------')
print("\nf.iv)Exiba a lista de tempos de sono inferiores a 5h, por dia da semana\n")
s=sMae.loc[sMae<5]
gMaeMenos=s.groupby(level=0)
print(gMaeMenos.agg('unique'))
print('-----------------------------------------------------')
#f.v.Exiba a diferença no sábado, em cada semana, entre o tempo de sono da mãe e do pai
print('-----------------------------------------------------')
print("\nf.v)diferença no sábado, em cada semana, entre o tempo de sono da mãe e do pai\n")
sMaeSab=sMae.loc['sab']
sPaiSab=sPai.loc['sab']
print(sMaeSab-sPaiSab)
print('-----------------------------------------------------')   
#f.vi.Em qual semana houve a menor média de horas de sono? (usar a planilha maeSem)
print('-----------------------------------------------------')   
print("\nf.vi) Em qual semana houve a menor média de horas de sono da mãe?\n")
def semana(x):
    grupo='Semana '+x[-1]
    return grupo
gMaeSem=sMaeS.groupby(by=semana)
MedMae=gMaeSem.agg('mean')
print(MedMae.loc[MedMae==MedMae.min()].index.values)
print('-----------------------------------------------------')   
#f.vii.Em qual semana houve a menor média de horas de sono? (usar a planilha paiSem)
print('-----------------------------------------------------')   
print("\nf.vii) Em qual semana houve a menor média de horas de sono do pai?\n")
gPaiSem=sPaiS.groupby(by=semana)
MedPai=gPaiSem.agg('mean')
print(MedPai.loc[MedPai==MedPai.min()].index.values)
#f.viii.Em quantas semanas a mãe teve menor média de horas de sono do que o pai? (usar as planilhas mae/paiSem)
print('-----------------------------------------------------')   
print("\nf.viii) Em quantas semanas a mãe teve menor média de horas de sono do que o pai?\n")
sDif=MedPai-MedMae
print(sDif.loc[sDif>0].size)
print('-----------------------------------------------------')   
