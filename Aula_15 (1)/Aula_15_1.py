import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#SEM ESPECIFICAÇÃO DOS ÍNDICES
aS1=pd.Series([4,7,-5])
aS2=pd.Series(list('abc'))
aS3=pd.Series({69:'E',65:'A','C':67})

#COM ESPECIFICAÇÃO DOS ÍNDICES
l=[4,7,-5]
bS1=pd.Series(l,index=['a','c','b'])

vogais=['vog1','vog5','vog2']
bS2=pd.Series({'vog1':'A','vog3':'I','vog5':'U'},index=vogais)
#QUEM MANDA É O INDICE!!

#A PARTIR DE UM ARQUIVO EXCEL

# a)  Planilha1: sem cabeçaho, tempo de cicatrização na coluna A
sHoras=pd.read_excel('Cicatrizacao.xlsx',index_col=None,header=None,squeeze=True)
#Por default, seleciona a primeira planilha

#b)Tempo: cabeçalho na 1ª linha, tempo de cicatrização na coluna A
sTempo= pd.read_excel('Cicatrizacao.xlsx',sheet_name='Tempo',index_col=None,header=0,squeeze=True)


#c)Sexo: cabeçalho na 1ª linha, sexo da cobaia na coluna A
sSexo= pd.read_excel('Cicatrizacao.xlsx',sheet_name='Sexo',index_col=None,header=0,squeeze=True)

#d) SexoTempo: cabeçalho na 1ª linha, índices - coluna A, valores - coluna B
sTempoSx= pd.read_excel('Cicatrizacao.xlsx',sheet_name='SexoTempo',index_col=0,header=0,squeeze=True)


#e) SexoTempo: cabeçalho na 1ª linha, índices - coluna B, valores - coluna A
sSxTempo= pd.read_excel('Cicatrizacao.xlsx',sheet_name='SexoTempo',index_col=1,header=0,squeeze=True)

#e) Idade a partir da planilha SexoIdadeTempo
sIdade= pd.read_excel('Cicatrizacao.xlsx',sheet_name='SexoIdadeTempo',usecols=(1,),index_col=None,header=0,squeeze=True)
#usecols serve para selecionar quais colunas eu vou usar
#Se usar somente uma coluna, o index_col será None

#f) SexoIdade a partir da planilha SexoIdadeTempo, indexados por idade
sSxIdade= pd.read_excel('Cicatrizacao.xlsx',sheet_name='SexoIdadeTempo',usecols=(0,1),index_col=1,header=0,squeeze=True)

#f) TempoIdade a partir da planilha SexoIdadeTempo,indexados por idade
sTempoIdade= pd.read_excel('Cicatrizacao.xlsx',sheet_name='SexoIdadeTempo',usecols=(1,2),index_col=0,header=0,squeeze=True)

#g) TempoSxId, a partir da planilha SexoIdadeTempo,indexados por sexo/idade
sTempoSxIdade= pd.read_excel('Cicatrizacao.xlsx',sheet_name='SexoIdadeTempo',index_col=[0,1],header=0,squeeze=True)
#Nessa última, a terceira coluna se torna a values

##################################################################
#   Exibindo  primeiros e  últimos
###################################################################
print('\n-----------------------------------------------------\n')
print('Exibindo 4 primeiros e 5 últimos de sHoras e sSxTempo')
print(sHoras.head(4),'\n',sHoras.tail())
print(sSxTempo.head(4),'\n',sSxTempo.tail())
print('\n-----------------------------------------------------\n')

print('\n-----------------------------------------------------\n')
print('Exibindo 4 primeiros e 5 últimos de sTempoSxIdade')
print(sTempoSxIdade.head(4),'\n',sTempoSxIdade.tail())
print('\n-----------------------------------------------------\n')

print('\n-----------------------------------------------------\n')
print('Exibindo cópia de sTempoSxIdade após ordenar por índice')
sOrd=sTempoSxIdade.sort_index()
print(sOrd)
print('\n-----------------------------------------------------\n')

##################################################################
#   Acessando,incluindo, alterando, excluindo elementos em Series
###################################################################

print('\n-----------------------------------------------------\n')
# Exibir o 3º elemento sHoras e sTempoSx
print('3º elemento sHoras e sTempoSx')
print(sHoras.iloc[2],sSxTempo.iloc[2])
print('\n-----------------------------------------------------\n')

print('\n-----------------------------------------------------\n')
# Exibir o 3º,5º e 6º elementos sHoras e sTempoSx
print('3º,5º e 6º elementos sHoras e sTempoSx')
print(sHoras.iloc[[2,4,5]],sSxTempo.iloc[[2,4,5]])
print('\n-----------------------------------------------------\n')

print('\n-----------------------------------------------------\n')
# Exibir o  elemento do índice 2 de sHoras -sem repetição nos labels do  index
print('elemento do índice 2 de sHoras: sem repetição nos labels do  index')
print(sHoras.loc[2])
print('\n-----------------------------------------------------\n')

print('\n-----------------------------------------------------\n')
# Exibir o  elemento do índice 16 de sTempoSx - com repetição nos labels do  index
print('elemento do índice 16 de sTempoSx: com repetição nos labels do  index')
print(sSxTempo.loc[16])

# Incluir os resultados de 2 cobaias no experimento em  sTempo e em sTempoSx:
#         31º  Macho, 10 semanas de vida, 555 dias para recuperação
#         32º  Macho, 12 semanas de vida, 999 dias para recuperação
#   Foi possível em sTempoSx??? 
# Excluir os resultados das  2 últimas  cobaias incluídas no experimento:
#         31º  Macho, 10 semanas de vida, 35 dias para recuperação
#         32º  Macho, 12 semanas de vida, 40 dias para recuperação
# 
#
sTempo.loc[30]=10
sTempo.loc[31]=12
#Não foi possível em sTempoSx
sTempo.drop([30,31],inplace=True)


#--------------------------------------------------------------------------
#  1) Criar a series sDias, a partir de sHoras. sDias contém o valor 
#   em intervalos de dias sem arredondamentos. Por ex 26h --> 1.0833333333333333.
#  2) Exibir os elementos de sDias, formatados com 1 casa decimal
#--------------------------------------------------------------------------
print("2) sHoras em dias")
def criadia(x):
    return '{:.1f}'.format(x/24)

sDias=sHoras.apply(criadia,args=())

####################################################################
#   Visualização Gráfica
###################################################################
#
#
# Exibir graficamente 
# 
#  Pizza:
#     sTempoIdade com representação %
#  Barra:
#     Vertical  : sTempoSx, ordene os índices e reexiba
#     Horizontal: sSxTempo  --> o que acontece? por que?
#     

print('\n-----------------------------------------------------\n')
print('STempoIdade com %')
sTempoIdade.plot.pie(legend=True,autopct='%.1f',figsize=(6,6))
plt.show()
sTempoSx.sort_index(inplace=True)
sTempoSx.plot.bar(width=0.5)
plt.show()
sSxTempo.plot.barh(width=0.8)
plt.show()

#---------------------------------------------------------------
#   Trabalhando com sTempoSxIdade
#---------------------------------------------------------------

# Exibir graficamente (barra)
sTempoSxIdade.plot.bar(width=0.5)
plt.show()

# Exibir numericamente o total, a média, mediana, moda, maior e menor valores
print('\n-----------------------------------------------------\n')
print('total, a média, mediana, moda, maior e menor valores desTempoSxIdade' )
print('\n-----------------------------------------------------\n')
print(sTempoSxIdade.sum())
print('\n-----------------------------------------------------\n')
print(sTempoSxIdade.mean())
print('\n-----------------------------------------------------\n')
print(sTempoSxIdade.median())
print('\n-----------------------------------------------------\n')
print(sTempoSxIdade.mode())
print('\n-----------------------------------------------------\n')
print(sTempoSxIdade.max())
print('\n-----------------------------------------------------\n')
print(sTempoSxIdade.min())

# Exibir numericamente por sx ( level = 0): o total, a média, mediana, maior e menor valores
print('\n-----------------------------------------------------\n')
print(sTempoSxIdade.sum(level=0))
print(sTempoSxIdade.mean(level=0))
print(sTempoSxIdade.median(level=0))
print(sTempoSxIdade.mode())
print(sTempoSxIdade.max(level=0))
print(sTempoSxIdade.min(level=0))

# Exibir numericamente por id ( level = 1): o total, a média, mediana, maior e menor valores
print('\n-----------------------------------------------------\n')
print(sTempoSxIdade.sum(level=1))
print(sTempoSxIdade.mean(level=1))
print(sTempoSxIdade.median(level=1))
print(sTempoSxIdade.mode())
print(sTempoSxIdade.max(level=1))
print(sTempoSxIdade.min(level=1))

# Exibir numericamente por sx/id ( level = (0,1): o total, a média, mediana, maior e menor valores
print('\n-----------------------------------------------------\n')
print(sTempoSxIdade.sum(level=(0,1)))
print(sTempoSxIdade.mean(level=(0,1)))
print(sTempoSxIdade.median(level=(0,1)))
print(sTempoSxIdade.mode())
print(sTempoSxIdade.max(level=(0,1)))
print(sTempoSxIdade.min(level=(0,1)))

# Exibir numericamente por id/sx ( level = (1,0): o total, a média, mediana, maior e menor valores
print('\n-----------------------------------------------------\n')
print(sTempoSxIdade.sum(level=(1,0)))
print(sTempoSxIdade.mean(level=(1,0)))
print(sTempoSxIdade.median(level=(1,0)))
print(sTempoSxIdade.mode())
print(sTempoSxIdade.max(level=(1,0)))
print(sTempoSxIdade.min(level=(1,0)))

#-----------------------------------------------------------------------------
# Responda as seguintes perguntas:
# A) Exibir a tabela de frequência, mediana, moda, maior e menor valores das Series sTempo
# B) Exibir a tabela de frequência,  moda, maior,  menor, média, mediana dos valores das Series sSexo
#                Todos foram possíveis?
# C) Qual a média de tempo de cicatrização? E por sx? E por idade?
# Execute : sSxTempo.min(level=0),e sSxTempo.loc[15].  
#           por que em sSxTempo.min(level=0) todos são F?  
# D) Qual o menor tempo de cicatrização? E por sx? E por idade?
# E) Qual o maior tempo de cicatrização? E por sx? E por idade?
# use sTempoIdade para responder:
# F) Qual a tabela de frequência de Idades?  Qual a idade mais frequente?
# G) Qual a tabela de frequência de tempos?  Qua(is) tempo(s) mais frequente(s)?
# Exibir graficamente, ambos como pizza:
#H)     sTempoIdade com representação %
#I)    a tabela de frequência de Idades (de sTempoIdade) com representação %
#------------------------------------------------------------------------------
print('\n-----------------------------------------------------\n')
print('A) tabela de frequência, mediana, moda, maior e menor valores das Series sTempo')

