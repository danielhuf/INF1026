import pandas as pd
import matplotlib.pyplot as plt

#a)Tempo: cabeçalho na 1ª linha, tempo de cicatrização na coluna A
sTempo= pd.read_excel('Cicatrizacao.xlsx',sheet_name='Tempo',index_col=None,header=0,squeeze=True)

#b) Idade a partir da planilha SexoIdadeTempo
sIdade= pd.read_excel('Cicatrizacao.xlsx',sheet_name='SexoIdadeTempo',usecols=(1,),index_col=None,header=0,squeeze=True)

#c)Sexo: cabeçalho na 1ª linha, sexo da cobaia na coluna A
sSexo= pd.read_excel('Cicatrizacao.xlsx',sheet_name='Sexo',index_col=None,header=0,squeeze=True)

# Categorize a idade em 2 faixas: jovem ( até 10 semanas) e adulto (11 a 15 semanas)
cIdade=pd.cut(sIdade,bins=[0,10,15])

# Categorize o tempo de recuperação em 3 faixas (bx,médio,alto)
cRecu=pd.cut(sTempo,bins=3,labels=['bx','médio','alto'])

# Quantas cobaias em cada categoria de idade?
print('-----------------------')
print(cIdade.value_counts())
print('-----------------------')

# Qual o tempo de recuperação médio, mediano, mínimo, máximo em cada categoria de idade?
gIdade=sIdade.groupby(by=cIdade)
print(gIdade.agg(['mean','median',min,max]))
print('-----------------------')


# Quantas fêmeas e quantos machos em cada categoria de idade? agrupar sTempo por cId e sSexo
gTempo=sTempo.groupby(by=[cIdade,sSexo])
print(gTempo.agg(['count']))
print('-----------------------')

# Qual o tempo de recuperação médio, mediano, mínimo, máximo  categoria de idade/sx?
print(gTempo.agg(['mean','median',min,max]))
print('-----------------------')


# Quantas fêmeas e quantos machos em cada categoria de recuperação?
gRecu=sTempo.groupby(by=[cRecu,sSexo])
print(gRecu.agg('count'))
print('-----------------------')

# Qual o tempo de recuperação médio, mediano, mínimo, máximo em cada categoria de recuperação?
print(gRecu.agg(['mean','median',min,max]))
print('-----------------------')

# Exiba  o percentual de fêmeas e machos em cada categoria de recuperação
s=gRecu.agg('count')/sTempo.size*100
print(s)
print('-----------------------')
#Percentual abaixo considerando cada categoria
print((gRecu.agg('count')/(gRecu.size()).sum(level=0)*100).apply('{:.2f}'.format))