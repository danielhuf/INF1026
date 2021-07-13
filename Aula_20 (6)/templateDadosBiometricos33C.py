"""
NOME: Daniel Stulberg Huf
TURMA: 33C
    
Dados Biológicos
"""
import pandas as pd
import matplotlib.pyplot as plt
'''
No arquivo dadosbioVA.xlsx encontram-se registrados características biométricas 
de 50 alunos

Cada linha tem: cor do cabelo, cor dos olhos, tipo sanguineo, altura
'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#
#   CRIANDO as SERIES
#
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''
Crie e exiba as seguintes series a partir do arquivo: 
srCabTipo: usando as colunas Cabelo e Tipo Sanguineo, tendo  Tipo como índice
srOlhosTipo: usando as colunas Olhos e Tipo Sanguineo, tendo  Tipo como índice
srAltTipo: usando as colunas Altura e Tipo Sanguineo, tendo  Tipo como índice

Verifique as principais medidas  (.describe), se há valores ausentes, etc..
'''
print('\n---------------------------------------------------------\n')
print('\n1- Mostrar o 6 primeiros e os 6 últimos elementos de cada Series criads')
srCabTipo = pd.read_excel('dadosbioVA.xlsx', header=0,usecols=[0,2],index_col=1, squeeze=True)
srOlhosTipo = pd.read_excel('dadosbioVA.xlsx', header=0,usecols=[1,2],index_col=1, squeeze=True)
srAltTipo = pd.read_excel('dadosbioVA.xlsx', header=0,usecols=[2,3],index_col=0, squeeze=True)

print('6 primeiros da srCabTipo\n',srCabTipo.head(6))
print('6 ultimos da srCabTipo\n',srCabTipo.tail(6))
print('6 primeiros da srOlhosTipo\n',srOlhosTipo.head(6))
print('6 ultimos da srOlhosTipo\n',srOlhosTipo.tail(6))
print('6 primeiros da srAltTipo\n',srAltTipo.head(6))
print('6 ultimos da srAltTipo\n',srAltTipo.tail(6))
print('\n---------------------------------------------------------\n')
'''
Altere os tipos de cabelos para:
    'Preto' - 'escuro'  
    'Castanho' - 'marrom'
    'Loiro' - 'claro'
'''
def altera(v):
    d={'Preto':'escuro','Castanho':'marrom','Loiro':'claro'}
    novo=d.get(v,v)
    return novo
# aplicar uma transformação de valor sobre cada um dos valores de srCabTipoO
sAux=srCabTipo.apply(altera)
print(sAux)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#
#   OBSERVANDO DADOS DE UM TIPO
#
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''
1- a) Mostrar a soma das alturas dos tipo sangüíneo A
   b) Mostrar os olhos  dos tipo sangüíneo AB e O
   c) Mostrar a cor do cabelo dos que não são do tipo B 
'''
print('\n---------------------------------------------------------\n')
print('1.a) soma das alturas dos tipo sangüíneo A')
print(srAltTipo.loc['A'].sum())

print('1.b) olhos  dos tipo sangüíneo AB e O')
print(srOlhosTipo.loc[['AB','O']])

print('1.b) cabelo  dos não B')
print(srCabTipo.drop('B'))

print('\n---------------------------------------------------------\n')

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#
#   TRATANDO OS VALORES AUSENTES
#
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''
2 - a) Valores ausentes na srAltTipo devem ser substituídos por 0.
      Exiba  a series resultante
    b) Valores ausentes na srCabTipo e srOlhosTipo devem ser substituídos 
       por qualquer um dos valores mais usuais do tipo sanguineo
      Exiba  as series resultantes
'''
print('2a- srAltTipo com os valores ausentes substituidos por 0\n')
srAltTipo.fillna(0,inplace=True)
print('\n---------------------------------------------------------\n')

print('2b- srCabTipo com os valores ausentes substituidos pelo mais frequente\n')    
# Agrupar por tipo --> index --> level=0
# Alterar os NaN de  cada grupo pelo mais frequente do grupo
#   Pega um grupo, acha o mais frequente do grupo , alterar os NaN do grupo
g1=srCabTipo.groupby(level=0)
g2=srOlhosTipo.groupby(level=0)
def preenche(sG):
    v=sG.mode().iloc[0]   #caso a moda tenha mais de um valor
    sG.fillna(v,inplace=True)
    return sG

srCabTipo=g1.transform(preenche)
print('\n---------------------------------------------------------\n')

print('2b- srOlhosTipo com os valores ausentes substituidos pelo mais frequente do tipo\n')
srOlhosTipo=g2.transform(preenche)
print('\n---------------------------------------------------------\n')

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#
#   CONHECENDO AS RELAÇOES INTRA/ENTRE SERIES: 
#        Medidas de Sumarização
#        Agrupamentos por tipo sanguineo
#        Relações/Agrupamentos entre as series 
#
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''
3 - Crie a tabela de frequência das Cores dos Olhos 
     e a Tabela de frequencia percentual das Cores dos Olhos 
  a) Exiba a tabela de frequência das Cores dos Olhos
  b) Exiba a Tabela de frequencia percentual das Cores dos Olhos 
'''
print('\n3a-Tabela de frequência das Cores dos Olhos\n')
print(srOlhosTipo.value_counts())
print('\n---------------------------------------------------------\n')

print('\n3b-Tabela de frequência Percentual  das Cores dos Olhos\n')
s=srOlhosTipo.value_counts()
print((s/s.sum()*100).apply('{:.2f}'.format))
print('\n---------------------------------------------------------\n')

'''
4- a) Qual a cor de cabelo mais comum? (com maior número de ocorrências?)
   b) E por tipo sangüineo?   # inverte: index=cor, values=index
'''
print('\n4a- A cor de cabelo mais comum (com maior nº de ocorrências)\n')
print(s.idxmax())
print('\n---------------------------------------------------------\n')

print('4b- Cores de cabelo mais comum por tipo sanguineo\n')
sInv=pd.Series(srCabTipo.index,srCabTipo.values)   #inverti a Series
#Nesse caso não adiantou nada, vamos manter na series original
g=srCabTipo.groupby(level=0)
lista_tipos=list(srCabTipo.index.unique())
for tipo in lista_tipos:
    print(tipo,'-',g.get_group(tipo).mode().values)
print('\n---------------------------------------------------------\n')

'''
5- a) Mostre a tabela de frequência das cores de cabelos em cada tipo sanguineo, 
      isto é, tabela de frequência das cores dos cabelos para o tipo A, para o tipo B,...
      Forma 1: agrupar por Tipo sanguineo e pelos valores dos cabelos e depois conte os registros
      Forma 2: usar crosstab (help (pd.crosstab)
   b) Mostre o gráfico de pizza da distribuição das cores dos cabelos 
     de cada  tipo sanguineo ( tabela de frequência de cada tipo sanguineo)
'''
print('\n5a-Tabela de frequência das cores de cabelos em cada tipo sanguineo')
gCabTipo=srCabTipo.groupby(level=0)
freq=gCabTipo.agg('value_counts')
print(freq)
print('\n---------------------------------------------------------\n')

print('\n5b-Distribuição das cores dos cabelos graficamente (pizza), de cada tipo sanguineo')
for tipo in lista_tipos:
    freq.loc[tipo].plot.pie(title='Distribuição dos cabelos do tipo {}'.format(tipo),figsize=(8,8),autopct='%.2f')
    plt.show()
print('\n---------------------------------------------------------\n')
  
'''
6- Qual a relação quantitativa entre a cor do cabelo e a cor dos olhos? 
    Mostre, para cada tipo de cabelo, a distribuição de cores de olhos 
     (tabela de frequência cabelo x olhos)
Forma 1: utiliza a series srCabTipo para agrupar a srOlhTipo e depois conte os registros
Forma 2: utilize crosstab
'''
print('\n6- Cores de cabelos x Cores de Olhos\n')
print(pd.crosstab(srOlhosTipo,srCabTipo))
print('\n---------------------------------------------------------\n')

'''
7- Qual(is) o(s) tipo(s) sangüineo(s) com maior número de ocorrências?
   E qual a quantidade de ocorrencias desse(s) tipo(s) sangüineo(s)?
'''
print('\n7- Tipo(s) Sanguineo(s) com maior numero de ocorrencias e quantidade de ocorrências')
sTipoOcor=sInv.value_counts()
print(sTipoOcor.loc[sTipoOcor==sTipoOcor.max()])
print('\n---------------------------------------------------------\n')

'''
8- a) Qual a média de altura dos entrevistados? 
   b) e por tipo sanguineo?
   
'''
print('\n8a - Média de altura dos entrevistados')
print(srAltTipo.mean())
print('\n---------------------------------------------------------\n')

print('\n8b) Média por tipo Sanguineo:\n')
print(srAltTipo.mean(level=0))
print('\n---------------------------------------------------------\n')

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#
#   CRIANDO NOVAS CATEGORIAS 
#
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
9- Crie a series sTamEnt com 3 categorias de acordo com a 
altura (de 0 a 150, de 150 a 180, acima 180) rotulando-as como baixo, normal, alto
a) Exiba a series criada 
b) Exiba a tabela de frequência das Categorias de Altura por tipo sanguineo
c) Exiba a quantidade de entrevistados em cada categoria, a altura média 
de cada categoria, a menor e a maior altura em cada categoria
As medidas devem ser rotuladas como 'Quantidade','Media','Menor','Maior'
'''

print("\n9a - Series com Categoria de Altura por tipo sanguineo\n")
sTamEnt=pd.cut(srAltTipo,bins=[0,150,180,srAltTipo.max()],labels=['baixo','normal','alto'])
print(sTamEnt)
print('\n---------------------------------------------------------\n')

print("\n9b - Tabela de frequência  das Categorias de Altura por tipo sanguineo\n")
sTFCat=sTamEnt.value_counts()
print(sTFCat)
print('\n---------------------------------------------------------\n')

# A tabela de frequência de sTFCat está ordenada decrescentemente pelo 
# nº de ocorrências de  cada categoria.  Reindexá-la para Baixo,Média,Alta
print("\n9b-Tabela de frequência  das Categorias de Altura por tipo sanguineo  reindexada\n")
print(sTFCat.reindex(['baixo','normal','alto']))
print('\n---------------------------------------------------------\n')

print('\n9c - Medidas de Sumarização da Altura dos entrevistados categorizadas')
g=srAltTipo.groupby(by=sTamEnt)
resumo=g.agg(['count','mean','min','max'])
resumo.rename(columns={'count':'Quantidade','mean':'Média','min':'Menor','max':'Maior'},inplace=True)
print(resumo)
print('\n---------------------------------------------------------\n')

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#
#   FILTRANDO REGISTROS DE ACORDO COM MAIS DE UMA CARACTERÍSTICA 
#
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
10- Mostre a tabela de frequência da cor dos olhos por cada categoria
    Utilize a series sTamEnt para agrupar srOlhosTipo ou utilizar crosstab
   
'''
print('\n10- frequência da cor dos olhos por categoria de altura')
print(pd.crosstab(sTamEnt,srOlhosTipo))
print('\n---------------------------------------------------------\n')

'''
11- a) Exiba as pessoas de olhos verdes ou azuis cujo tipo sanguineo é O, ordenado
    por cor dos olhos
    b) Mostre graficamente (gráfico de barras) a tabela de frequência das cores
       claras de olhos no tipo sanguineo O
'''
print('\n11a-Olhos Claros e tipo sanguineo O')   # É útil esta forma de visualização, neste caso?
f1=srOlhosTipo.loc['O']
cond1=f1=='Verde'
cond2=f1=='Azul'
f2=f1.loc[cond1|cond2].sort_values()
print(f2)
print('\n---------------------------------------------------------\n')
  
print('\n11a-Tabela de Frequência em gráfico de barras de Olhos Claros e tipo sanguineo O') 
f2.value_counts().plot.bar(color=['g','b'])
plt.show()
print('\n---------------------------------------------------------\n')



