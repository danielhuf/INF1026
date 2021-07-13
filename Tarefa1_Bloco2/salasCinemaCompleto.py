#Daniel Stulberg Huf - matricula 1920468
#Prof. Claudia - Turma 33C

import pandas as pd
import matplotlib.pyplot as plt

#============================================
#
# A ANCINE armazena no arquivo excel SalasdeCinema,
# em planilhas anuais, a quantidade de salas 
# de Cinema existentes nas UF.
# Há dados dos anos de 2019,2018 e 2009
# As planilhas têm cabeçalho e está na linha 1 
#  
#A planilha RegiãoEstado tem a Região de cada estado.
#A planilha PublicoUF mostra a quantidade de títulos, número de espectadores e Renda
#============================================

######################################################

#============================================
#  I) Construindo  Series a partir de um arquivo excel
#============================================
#
#============================================
#       a) Manipulando a series do sRegUF
#============================================
#   Utilizar a planilha RegiaoEstado para  criar a Series sRegUF
#       índice: coluna 0 (UF) e valor coluna 1 (Reg)
#	tem linha de cabeçalho
sRegUF= pd.read_excel('SalasdeCinema2019.xlsx',sheet_name='RegiaoEstado',index_col=0,header=0,squeeze=True)

#   Mostre os valores, índices e tamanho da sRegUF
print("\nI.a) primeiros 5 valores, índices e tamanho da sRegUF\n")
print('Primeiros 5 valores \n{}'.format(sRegUF.head(5).values))
print('\nPrimeiros 5 índices \n{}'.format(sRegUF.head(5).index.values))
print('\nTamanho \n{}'.format(sRegUF.size))
print('\n-----------------------------------------------------\n')

#============================================
#       b) Manipulando a series do sPubUF
#============================================
#   Utilizar a planilha PublicoUF para  criar a Series sPubUF
#       índice: coluna 0 (UF) e valor coluna 2 (Publico)
#	tem linha de cabeçalho
sPubUF= pd.read_excel('SalasdeCinema2019.xlsx',sheet_name='PublicoUF',usecols=(0,2),index_col=0,header=0,squeeze=True)

#   Mostre os valores, índices e tamanho da sRegUF
print("\nI.b) últimos 3 valores, índices e tamanho da sRegUF\n")
print('Úlimos 3 valores \n{}'.format(sPubUF.tail(3).values))
print('\nÚltimos 3 índices \n{}'.format(sPubUF.tail(3).index.values))
print('\nTamanho \n{}'.format(sPubUF.size))
print('\n-----------------------------------------------------\n')

# 
#============================================
#       c) Manipulando a series do 2018
#============================================
#   Utilizar a planilha 2018 para  criar a Series sS2018
#       índice: coluna 0 (UF) e valor coluna 1 (qt)
#		tem linha de cabeçalho
sS2018= pd.read_excel('SalasdeCinema2019.xlsx',sheet_name='2018',index_col=0,header=0,squeeze=True)

#   Observe: Todos as UFs têm valor?
#Não, BA e DF não possuem valores.

#            O que a linha em branco na planilha provocou?
#As linhas em branco retornaram o valor NaN, que siginifica "Not a number".
#   

# Mostre os valores, índices e tamanho da sS2018
print('\n-----------------------------------------------------\n')
print("\nI.c.1) valores , índices e tamanho da sS2018\n")
print('Valores \n{}'.format(sS2018.values))
print('\nÍndices \n{}'.format(sS2018.index.values))
print('\nTamanho \n{}'.format(sS2018.size))
print('\n-----------------------------------------------------\n')

#Alterando valores na Series
print("\nI.c.2)Ajuste a quantidade de salas de sS2018 da BA para 114 e DF, para 88 exiba-as\n")
sS2018.loc['BA']=114
sS2018.loc['DF']=88
print(sS2018.loc[['BA','DF']])
print('\n-----------------------------------------------------\n')

#Selecionando itens da Series
print("\nI.c.2) Quantas salas na RJ?\n")
print('{} salas'.format(int(sS2018.loc['RJ'])))

print("\nI.c.3) Qual a posição do RJ na Series--> index.get_loc()")
print(sS2018.index.get_loc('RJ'))

print("\nI.c.4) Quantas salas na RJ e no RS?\n")
print(sS2018.loc[['RJ','RS']].apply('{:.0f}'.format))
print('\n-----------------------------------------------------\n')

#Mostrar elementos da Series ordenado
print("\nI.c.5 Salas ordenadas por UF:\n")
print(sS2018.sort_index())

print("\nI.c.5 Salas ordenadas por valor::\n")
print(sS2018.sort_values())
print('\n-----------------------------------------------------\n')

#============================================
#       d) Manipulando a series do 2019
#============================================
#   Utilizar a planilha 2019 para  criar a Series sS2019
#       índice: coluna 0 (UF) e valor coluna 1 (qt)
#		tem linha de cabeçalho
sS2019= pd.read_excel('SalasdeCinema2019.xlsx',sheet_name='2019',index_col=0,header=0,squeeze=True)

# Mostre os valores, índices e tamanho da sS2019
print("\nI.d)valores, índices e tamanho da sS2019\n")
print('Valores \n{}'.format(sS2019.values))
print('\nÍndices \n{}'.format(sS2019.index.values))
print('\nTamanho \n{}'.format(sS2019.size))
print('\n-----------------------------------------------------\n')

#==================================================
#       II) Responder as seguintes perguntas em 2019:
#==================================================
# 
#   II.a) Quantos salas existem no Brasil?
print('II.a) Número de salas no Brasil: \n{}'.format(sS2019.sum()))
print('\n-----------------------------------------------------\n')
#
#   II.b) Qual a quantidade média de salas por UF? (soma das salas/ nº de UFs)
print('II.b) Quantidade média de salas no Brasil por UF: \n{}'.format(sS2019.sum()/sS2019.size))
print('\n-----------------------------------------------------\n')
#
#   II.c) Qual a quantidade média de salas por região? (soma das salas da região/ nº de Regiões)
gS2019Reg=sS2019.groupby(by=sRegUF)
print('II.c) Quantidade média de salas no Brasil por região: \n{}'.format(gS2019Reg.agg('sum')/gS2019Reg.agg('size')))
print('\n-----------------------------------------------------\n')
#
#   II.d) Qual o percentual de salas da UF sobre o total de salas do país? (qt salas da UF *100/ total de salas do país)
print('II.d) Percentual de salas da UF sobre o total de salas do país: \n{}'.format(sS2019.sum(level=0)*100/sS2019.sum()))
print('\n-----------------------------------------------------\n')
#
#   II.e) Qual o percentual de salas de cada região sobre o total de salas do país?(qt salas da região/ total de salas do país)
print('II.e) Percentual de salas de cada região sobre o total de salas do país: \n{}'.format(gS2019Reg.agg('sum')*100/sS2019.sum()))
print('\n-----------------------------------------------------\n')
#
#   II.f) Qual a  maior qt de sala? Em qual UF? Lembre-se que pode haver empate.
print('II.e) Maior quantidade de salas: \n{}'.format(sS2019.max()))
print('\nUF(s) com maior quantidade de salas: \n{}'.format(sS2019.loc[sS2019==sS2019.max()].index.values))
print('\n-----------------------------------------------------\n')
#
#   II.g) Qual a  região com maior qt de sala?  Lembre-se que pode haver empate.
sS2019Reg=gS2019Reg.agg('sum')
print('II.g) Região(ões) com maior quantidade de salas: \n{}'.format(sS2019Reg.loc[sS2019Reg==sS2019Reg.max()].index.values))
print('\n-----------------------------------------------------\n')
#
#   II.h) Quantos habitantes por sala (público/qt de salas) em cada UF? e por região? Exibir sem casas decimais
sPubUF.sort_index(inplace=True)
print('II.h) Habitantes por sala em cada UF: \n{}'.format(sPubUF//sS2019))
print('\n-----------------------------------------------------\n')
gPubReg=sPubUF.groupby(by=sRegUF)
sPubReg=gPubReg.agg('sum')
print('Habitantes por sala em cada região: \n{}'.format(sPubReg//sS2019Reg))
print('\n-----------------------------------------------------\n')
#
#   II.i) Qual UF com maior relação habitantes/sala? e com menor relação habitantes/sala?
sHabSalaUF=sPubUF/sS2019
print('II.i) UF com maior relação habitantes/sala: \n{}'.format(sHabSalaUF.loc[sHabSalaUF==sHabSalaUF.max()].index.values))
print('\nUF com menor relação habitantes/sala: \n{}'.format(sHabSalaUF.loc[sHabSalaUF==sHabSalaUF.min()].index.values))
print('\n-----------------------------------------------------\n')
#
#   II.j) Qual Região com maior relação habitantes/sala? e com menor relação habitantes/sala?
sHabSalaReg=sPubReg/sS2019Reg
print('II.j) Região com maior relação habitantes/sala: \n{}'.format(sHabSalaReg.loc[sHabSalaReg==sHabSalaReg.max()].index.values))
print('\nRegião com menor relação habitantes/sala: \n{}'.format(sHabSalaReg.loc[sHabSalaReg==sHabSalaReg.min()].index.values))
print('\n-----------------------------------------------------\n')
#
#   II.k) Mostrar graficamente a relação percentual habitantes/sala de cada região, ordenada por nome de região
sHabSalaReg.plot.pie(title='relação percentual habitantes/sala de cada região',figsize=(8,8),autopct='%.2f',legend=True)
plt.show()
#
######################################################
# 
#============================================
#       III) Analisando a evolução da quantidade de salas de 2019 e 2018
#============================================
#   
#   III.a)Quais estados tiveram crescimento no número de salas de 2018 e 2019?
sDif=sS2019-sS2018
print('\nIII.a) Estados que tiveram crescimento no número de salas de 2018 a 2019: \n{}'.format(sDif.loc[sDif>0].index.values))
print('\n-----------------------------------------------------\n')
#
#   III.b)Quantos estados reduziram o número de salas?
print('III.b) Número de estados que reduziram o número de salas de 2018 a 2019: \n{}'.format(sDif.loc[sDif<0].size))
print('\n-----------------------------------------------------\n')
#
######################################################

#============================================================================
#    IV) Analisando por categorias:
#
#   IV.a) Categorizar a quantidade de salas em duas categorias e mostrar:cQtMed
#               abaixo ou igual à média - ateMedia
#               acima da média- supMedia
cQtMed=pd.cut(sS2019,bins=[0,sS2019.mean(),sS2019.max()],labels=['ateMedia','supMedia'])
print('IV.a) Exibindo cQtMed:\n{}'.format(cQtMed))
print('\n-----------------------------------------------------\n')
#
#   IV.b) Categorizar a relação de habitantes/sala em 5 faixas e mostrar:cHabSala
#               1ª faixa - ruim
#               2ª faixa - baixo
#               3ª faixa - mediano
#               4ª faixa - bom
#               5ª faixa - ótimo
cHabSala=pd.cut(sHabSalaUF,bins=5,labels=['ruim','baixo','mediano','bom','ótimo'])
print('IV.b) Exibindo cHabSala:\n{}'.format(cHabSala))
print('\n-----------------------------------------------------\n')
#
#   IV.c) Mostrar para cada região sua categoria em relação à quantidade de salas
sRegTot=gS2019Reg.sum()
cRegQtMed=pd.cut(sRegTot,bins=[0,sRegTot.mean(),sRegTot.max()],labels=['ateMedia','supMedia'])
print('IV.c) Exibindo para cada região sua categoria em relação à quantidade de salas:\n{}'.format(cRegQtMed))
print('\n-----------------------------------------------------\n')
#
#   IV.d) Mostrar a tabela de frequência, por região, de cada categoria de quantidade de salas 
print('IV.d) Exibindo a tabela de frequência por região de cQtMed:\n{}'.format(pd.crosstab(sRegUF,cQtMed,rownames=['Regiões'],colnames=['Categorias'])))
print('\nExibindo a tabela de frequência por região de cHabSala:\n{}'.format(pd.crosstab(sRegUF,cHabSala,rownames=['Regiões'],colnames=['Categorias'])))
print('\n-----------------------------------------------------\n')
#
#   IV.e) Mostrar a média de salas, o menor número de salas e o maior número de salas em cada categoria de habitantes por sala
gHabSala=sS2019.groupby(by=cHabSala)
print('IV.e) Exibindo a média de salas, o menor número de salas e o maior número de salas em cada categoria de habitantes por sala:\n{}'.format(gHabSala.agg(['mean','min','max'])))
print('\n-----------------------------------------------------\n')
#
#   IV.f) Mostrar a tabela de frequência de cada faixa da relação de habitantes/sala no país
print('IV.f) Exibindo a tabela de frequência de cada faixa da relação de habitantes/sala no país:\n{}'.format(cHabSala.value_counts().reindex(['ruim','baixo','mediano','bom','ótimo'])))
print('\n-----------------------------------------------------\n')
#
#   IV.g) Mostrar, por região, a média de salas, o menor número de salas e o maior número de salas em cada categoria de habitantes por sala
#============================================================================
gRegHabSala=sS2019.groupby(by=[sRegUF,cHabSala])
print('IV.g) Exibindo, por região, a média de salas, o menor número de salas e o maior número de salas em cada categoria de habitantes por sala:\n{}'.format(gRegHabSala.agg(['mean','min','max']).fillna('-')))
print('\n-----------------------------------------------------\n')
