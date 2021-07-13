# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 08:36:37 2019

@author: julia
"""
#Daniel Stulberg Huf - 1920468
#Prof. Claudia Ferlin - turma 33C

import pandas as pd
import matplotlib.pyplot as plt
"""
Analise o  DataFrame (dfInv) a partir do arquivo Excel Investidores.xlsx disponibilizado.
Esse arquivo retrata o perfil dos investidores brasileiros nos últimos anos, 
sendo disponibilizados em colunas seu sexo, nível acadêmico, atividade remunerada e idade.
O DataFrame deve ser indexado pela coluna Id.
Alunos: Julia Smith e Jhuan Maia
Matrícula: 1813113 e 1620706
Turma: 33A
Fontes: https://financeone.com.br/qual-o-perfil-do-investidor-brasileiro/ e https://g1.globo.com/economia/noticia/2018/10/04/bovespa-ganhou-mais-de-110-mil-novos-investidores-em-2018.ghtml
"""

dfInv = pd.read_excel('Investidores.xlsx',index_col=0,header=0)

'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

1) Conhecendo a estrutura de seu DataFrame: 
a) Nome e tipo das colunas.
b) Tamanho da planilha.
c) Tem colunas com valores ausentes? (Se sim, exiba-os)	
d) Medidas sumarização descritivas.
e)  Exiba as 5 primeiras e 5 últimas linhas.
'''    

print('1.a)Nome e tipo das colunas ')
print(list(dfInv.columns.values))
print(dfInv.dtypes)
print('---------------------------------------------------')

print('1.b) Tamanho da planilha.')
print(dfInv.shape)
print('---------------------------------------------------')

print('1.c) Tem colunas com valores ausentes? (Se sim, exiba-os)')
dfSem=dfInv.dropna()
print(dfInv.drop(dfSem.index))
print('---------------------------------------------------')

print('1.d) Medidas sumarização descritivas.')
print(dfInv.describe())
print('---------------------------------------------------')

print('1.e) Exiba as 5 primeiras e 5 últimas linhas.')
print(dfInv.head(5))
print(dfInv.tail(5))
print('---------------------------------------------------')

''' 
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

2) Consertando os dados do DataFrame: 
a) Mude o nome das colunas:
	-  Nível Acadêmico = Nivel
	- Atividade Remunerada = Remuneracao
	Agora transforme tudo em maiúsculo.

b) Verifique se na coluna Sexo os valores estão como M e F, caso não, conserte-os.
c) Transforme, na coluna Nível Acadêmico:
	- Ensino Médio = EM
	- Graduação = GRAD
   Transforme, na coluna Atividade Remunerada:
	- Não Declarou = NaD
d) Verifique se há valores ausentes e se houver apague-os.
'''

print('2.a) Dados Modificados ')
dfInv.rename(columns={'Nível Acadêmico':'Nivel','Atividade Remunerada':'Remuneracao'},inplace=True)
dfInv.columns=dfInv.columns.str.upper()
print(dfInv)
print('---------------------------------------------------')

print('2.b) Dados Sexo Modificados ')
dfInv['SEXO']=dfInv['SEXO'].str.upper()
print(dfInv)
print('---------------------------------------------------')

print('2.c) Dados Nível Acadêmico')
def transforma(x):
    if x=='Ensino Medio':
        return 'EM'
    elif x=='Graduação':
        return 'GRAD'
    return x
dfInv['NIVEL']=dfInv['NIVEL'].apply(transforma)
nd=dfInv['REMUNERACAO']=='Não Declarou' #ESSE É O METODO CORRETO
dfInv.loc[nd,'REMUNERACAO']='NaD'
print(dfInv)
print('---------------------------------------------------')

print('2.d) Sem valores ausentes')
print(dfInv.isnull())
#Sim, há valores ausentes
dfInv.dropna(how='any',inplace=True)
print(dfInv)
print('---------------------------------------------------')
'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

3) Conhecendo os dados de seu DataFrame:
a) Exiba a tabela de frequência para cada Sexo.
b) Exiba a tabela percentual de frequência para cada Sexo.
c) Exiba a tabela de frequência de Sexo por Nível Acadêmico.
d) Exiba a tabela de frequência de Sexo por Nível Acadêmico por Remuneração.
e) Qual a média das idades dos investidores brasileiros?
f) Qual a idade do investidor mais novo? E do mais velho? Quem são?
g) Exiba o valor mais frequemte de cada coluna.
h) Qual o percentual de remunerações não declaradas?
i) Qual sexo predomina entre os investidores graduados?

j) Crie uma coluna chamada Faixa Etária, dividindo as idades:
	- 16 a 25 anos = JOVEM
	- 26 a 35 anos = ADULTO 1
	- 36 a 45 anos = ADULTO 2
	- 46 a 55 = ADULTO 3
	- 56 a 65 = ADULTO 4
	- Maior de 66 = IDOSO
k) Exiba a tabela de frequência para a faixa etária.
l) Faça um gráfico em pizza que mostre o percentual de cada nível acadêmico.
m) Faça um gráfico em barras que mostre o total de cada Atividade Remunerada.
n) Faça um gráfico de pizza com a faixa etária.
'''
   
print('3.a) tabela de frequência para cada Sexo ')
freq=dfInv['SEXO'].value_counts()
print(freq)
print('---------------------------------------------------')

print('3.b) tabela percentual de frequência para cada Sexo. ')
freq.plot.pie(figsize=(5,5),autopct='%.1f')
plt.show()
print('---------------------------------------------------')

print('3.c) tabela de frequência de Sexo por Nível Acadêmico.')
print(pd.crosstab(dfInv['SEXO'],dfInv['NIVEL']))
print('---------------------------------------------------')

print('3.d) tabela de frequência de Sexo por Nível Acadêmico por Remuneração.')
print(pd.crosstab(dfInv['SEXO'],[dfInv['NIVEL'],dfInv['REMUNERACAO']]))
print('---------------------------------------------------')

print('3.e) média das idades dos investidores brasileiros')
print(dfInv['IDADE'].mean())
print('---------------------------------------------------')

print('3.f) idade do investidor mais novo? E do mais velho? Quem são? ')
print('Idade e id´s dos mais novos:')
print(dfInv['IDADE'].min())
print(list(dfInv.loc[dfInv['IDADE']==dfInv['IDADE'].min()].index.values))
print('Idade e id´s dos mais velhos:')
print(dfInv['IDADE'].max())
print(list(dfInv.loc[dfInv['IDADE']==dfInv['IDADE'].max()].index.values))
print('---------------------------------------------------')

print('3.g) valor mais frequente de cada coluna')
def maisFreqPorCol(Id):
    f=Id.value_counts()
    m=f.max()
    sMaisFreq=f.loc[f==m]
    return list(sMaisFreq.index)
print(dfInv.apply(maisFreqPorCol))
print('---------------------------------------------------')

print('3.h) o percentual de remunerações não declaradas')
total=dfInv['REMUNERACAO'].size
naoDec=dfInv['REMUNERACAO'].loc[dfInv['REMUNERACAO']=='NaD'].size
print(naoDec*100/total,'%')
print('---------------------------------------------------')

print('3.i) sexo predominante entre os investidores graduados')
grad=dfInv.loc[dfInv['NIVEL']=='GRAD']
freqSexo=grad['SEXO'].value_counts()
print(freqSexo.loc[freqSexo==freqSexo.max()].index.values)
print('---------------------------------------------------')

print('3.j) coluna  Faixa Etária')
cFaixa=pd.cut(dfInv['IDADE'],bins=[16,25,35,45,55,65,dfInv['IDADE'].max()],labels=['JOVEM','ADULTO 1','ADULTO 2','ADULTO 3','ADULTO 4','IDOSO'],include_lowest=True)
dfInv['Faixa Etária']=cFaixa
print(dfInv)
print('---------------------------------------------------')

print('3.k) tabela de frequência para a faixa etária')
print(cFaixa.value_counts())
print('---------------------------------------------------')

print('3.l) gráfico em pizza que mostre o percentual de cada nível acadêmico')
freqNivel=dfInv['NIVEL'].value_counts() 
freqNivel.plot.pie(figsize=(5,5),autopct='%.1f')
plt.show()
print('---------------------------------------------------')

print('3.m) um gráfico em barras que mostre o total de cada Atividade Remunerada. ')
dfInv['REMUNERACAO'].value_counts().plot.bar()
plt.show()
print('---------------------------------------------------')

print('3.n) um gráfico de pizza com a faixa etária')
cFaixa.value_counts().plot.pie(figsize=(5,5),autopct='%.1f')
plt.show()
print('---------------------------------------------------')



