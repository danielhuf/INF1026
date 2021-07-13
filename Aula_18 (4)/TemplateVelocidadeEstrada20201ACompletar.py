import pandas as pd
import matplotlib.pyplot as plt


#============================================
#
# Durante 3 dias, um radar da polícia rodoviária 
# registrou as velocidades (em km/h)) de veículos 
# em uma rodovia, armazenando-as em 3 planilhas excel: 
#    dia1.xlsx, dia2.xlsx, dia3,xlsx
#
#============================================

#============================================
# Construindo  Series a partir de um arquivo excel
#============================================
# 
#============================================
#       Manipulando a series do dia3
#============================================
#   Utilizar a planilha excel dias3.xlsx para  criar a Series sDia3
#       índice: coluna 0 (hora) e valor coluna 1 (vel)- tem linha de cabeçalho
#   Mostrar 10ºs elementos
#   
sDia3=pd.read_excel('dia3.xlsx', header=0,index_col=0,squeeze=True,decimal=',')
print(sDia3.head(10))

# Mostrar os registros  das 22h
print('\n-----------------------------------------------------\n')
print(sDia3.loc[22].apply('{:.2f}'.format))

# Mostrar o registro mais cedo e o mais tarde
menor=sDia3.index.min()
maior=sDia3.index.max()
print(sDia3.loc[[menor,maior]].apply('{:.2f}'.format))
print('\n-----------------------------------------------------\n')

# Mostrar 3 registros do meio do período
meio=sDia3.size//2
print(sDia3.iloc[meio-1:meio+2].apply('{:.2f}'.format))
print('\n-----------------------------------------------------\n')

#   Exibir graficamente (barras horizontal) 
sDia3.plot.barh(figsize=(8,8))
plt.show()
print('\n-----------------------------------------------------\n')

#   Exibir graficamente (pizza) 
sDia3.plot.pie(figsize=(8,8),autopct='%.1f')
plt.show()
print('\n-----------------------------------------------------\n')

#=================================================================
#       Responder as seguintes perguntas sobre sDia3:
#=================================================================
# 
#   a)  Quantos carros foram registrados?
print(sDia3.size)
print('\n-----------------------------------------------------\n')

#   b)  Quantos registros estão sem  velocidade registrada? sDia3.size - sDia3.count (nao tem NaN)
print(sDia3.size - sDia3.count())
print('\n-----------------------------------------------------\n')

#   c)  Qual a velocidade média por dia? 
print('{:.2f}'.format(sDia3.mean()))
print('\n-----------------------------------------------------\n')

#   d) Qual a velocidade média por hora? Exibi-las também graficamente(barra)
gDia3=sDia3.groupby(level=0)
print(gDia3.agg('mean').apply('{:.2f}'.format))
gDia3.agg('mean').plot.bar(figsize=(8,8))
plt.show()
print('\n-----------------------------------------------------\n')

#   e) Qual a velocidade mais frequente?
print(sDia3.mode().apply('{:.2f}'.format))
print('\n-----------------------------------------------------\n')

#   f) Qual a maior velocidade registrada? Em qual(is) hora(s)?
print('{:.2f}'.format(sDia3.max()))
print(sDia3.idxmax())
print('\n-----------------------------------------------------\n')

#   g) Qual a maior velocidade registrada por hora?
print(gDia3.agg('max').apply('{:.2f}'.format))
print('\n-----------------------------------------------------\n')

#   h) Em qual(is) hora(s) foi(ram) registrada(s) a menor velocidade? 
print(sDia3.idxmin())
print('\n-----------------------------------------------------\n')

#============================================
# Crie as series dos dias 1 e 2
# Acrescente-as  à  Series sDia3, gerando a series sTot
# utilize o método .append 
#============================================
sDia2=pd.read_excel('dia2.xlsx', header=0,index_col=0,squeeze=True,decimal=',')
print(sDia2.head(10))
sDia1=pd.read_excel('dia1.xlsx', header=0,index_col=0,squeeze=True,decimal=',')
print(sDia1.head(10))
print('\n-----------------------------------------------------\n')

sTot=sDia3.append([sDia1,sDia2])
print(sTot)
print('\n-----------------------------------------------------\n')

#============================================
#       Usando Filtros sobre sTot
#============================================
#  a)Crie uma cópia de sTot ( sCopia)
sCopia=sTot.copy()
print(sCopia)
print('\n-----------------------------------------------------\n')

#  b)Substitua os valores ausentes(NaN) pela menor velocidade
sTot.fillna(value=sTot.min(),inplace=True)
print(sTot)
print('\n-----------------------------------------------------\n')

#  c)Mostre todas as horas dos registros da menor velocidade
print(sTot.loc[sTot==sTot.min()].index.unique().values)
print('\n-----------------------------------------------------\n')

#  d)Exiba por hora, a quantidade de registros abaixo de 40 km/h
s40=sTot.loc[sTot<40]
g40=s40.groupby(level=0)
print(g40.agg('count'))
print('\n-----------------------------------------------------\n')

#  e)Exiba a velocidade média por hora em sCopia
gCopia=sCopia.groupby(level=0)
print(gCopia.agg('mean').apply('{:.2f}'.format))
print('\n-----------------------------------------------------\n')

#  f)Crie a Series sRapidinhos com os elementos cujos valores são 
#  superiores à média de sCopia,  exiba-a graficamente
sRapidinhos=sCopia.loc[sCopia>sCopia.mean()]
print(sRapidinhos)
sRapidinhos.plot.bar(figsize=(8,8))
plt.show()
print('\n-----------------------------------------------------\n')

#  g) Mostre a porcentagem de veículos com velocidade entre 80km/h e 110km/h
s80_110=sTot[sTot.between(80,110,inclusive=True)]
print('{:.2f}%'.format((s80_110.size/sTot.size)*100))
print('\n-----------------------------------------------------\n')

#====================================================
# CONSTRUINDO a TABELA DE FREQUENCIA DE VALORES (no caso Velocidades):
# CRIAR a partir da sDia3 uma nova series (sVelD3) onde os indices sao 
# velocidades ocorridas (uma vez cada)  e os valores a quantidade  de vezes que cada 
# velocidade ocorreu em sDia3:  usar  value_counts()
# ====================================================

sVelD3=sDia3.value_counts()

#====================================================
#   EXIBIR graficamente e na forma de tabela  a series sVel3 (que corresponde a tabela de frequencia)
print(sVelD3)
print('\n-----------------------------------------------------\n')
sVelD3.plot.bar(figsize=(8,8))
plt.show()
print('\n-----------------------------------------------------\n')
#====================================================

#============================================
#       Usando o apply sobre sDia3
#============================================
# Exibir as velocidades com apenas uma casa decimal
print(sDia3.apply('{:.2f}'.format))
print('\n-----------------------------------------------------\n')

# Conferindo os valores, observou-se que o radar aumentava em 10% o valor medido
# quando a velocidade registrada estava superior a 105 km/h. Conserte-os.
#     #POSSIBILIDADE DE SOLUCAO: aplicar uma funcao que retorna a vel corrigida 
#        Passo 1:  criar a função que recebe a vel e retorna-a corrigida
def aumentaPercent(x,num):
    if x>105:
        return ((100+num)/100)*x
    return x
#        Passo 2: aplicar essa funcao a todos os valores da series: usar apply
#            O metodo apply se encarrega de chamar a funcao para cada um dos 
#            valores da serie
print(sDia3.apply(aumentaPercent,args=(10,)))
print('\n-----------------------------------------------------\n')

#  Como permitir que o % de aumento seja informado pelo usuário?
# Já fiz em cima
#
# Crie uma nova series, categorizando as velocidades em 3 grupos:
#       até  80km/h : lento
#       entre 80 e 100: adequado
#       acima de 100: rápido
cDia3=pd.cut(sDia3,bins=[0,80,100,sDia3.max()],labels=['lento','adequado','rápido'])
print(cDia3)
print('\n-----------------------------------------------------\n')

# usando esta Series, mostre a Tabela de Frequência na forma tabular e graficamente
gDia3=sDia3.groupby(by=cDia3)
print(gDia3.agg('count'))
print('\n-----------------------------------------------------\n')
gDia3.agg('count').plot.bar(figsize=(8,8))
plt.show()
print('\n-----------------------------------------------------\n')

# Lembrar que há registros com valores ausentes!!!
# Verifique como a tabela é organizada... se necessário reindexe ( método .reindex)
#

#============================================
#       Usando o groupby sobre sDia3
#============================================
# Agrupar as velocidades  por turno:
# 	madrugada: 0h às 5h 
#       manhã : 6h às 13h
#	tarde: 13h às 19h
#       noite: 19h às 24 h
def turno(x):
    if x<=5:
        return 'madrugada'
    elif x<=13:
        return 'manhã'
    elif x<=19:
        return 'tarde'
    else:
        return 'noite'

gDia3=sDia3.groupby(by=turno)
# Mostrar para cada grupo:
#   i)  Quantos carros foram registrados?
print(gDia3.agg('size'))
print('\n-----------------------------------------------------\n')

#   j)  Quantos registros estão sem  velocidade registrada?
print(gDia3.agg('size')-gDia3.agg('count'))
print('\n-----------------------------------------------------\n')

#   k)  Qual a velocidade média? 
print(gDia3.agg('mean'))
print('\n-----------------------------------------------------\n')

#   l)  Qual a velocidade mais frequente?
s=gDia3.agg('value_counts')
print(s.loc[s==s.max()])
print('NÃO HÁ VELOCIDADE MAIS FREQUENTE')
print('\n-----------------------------------------------------\n')

#   m) Qual a maior velocidade registrada? Em qual(is) hora(s)?
print(gDia3.agg(['max','idxmax']))
print('\n-----------------------------------------------------\n')

#	n) Quantos registros de velocidade >=90 km/h foram feitos?
def seleciona(elG):
    return (elG>=90).sum()
print(gDia3.apply(seleciona))
print('\n-----------------------------------------------------\n')

#	Qual(is) o(s) grupo(s) com maior quantidade de registros?
print(gDia3.agg('size').idxmax())  
print('\n-----------------------------------------------------\n')
'''
#============================================
 # Retire os comentário dos comandos abaixo. 
# Qual as diferenças entre eles?
#============================================

import random
l=list(range(10,20))
lval=random.sample(l,8)
sAmostra=pd.Series(lval)
print("Amostra\n", sAmostra)
print('\n-----------------------------------------------------\n')

s2=pd.Series([10]*5)
print("Método append e o parâmetro ignore_index")
print("No Método append, ignore_index=False  (default)\n",sAmostra.append(s2))
print("Após Método append\n", sAmostra)
print("No Método append ignore_index=True\n",sAmostra.append(s2,ignore_index=True))
print("Após Método append\n", sAmostra)
print("Método append  x Método update")
print("No Método append\n",sAmostra.append(s2))
print("Após Método append\n",sAmostra)
print("No Método update\n",sAmostra.update(s2))
print("Após Método update\n",sAmostra)
print("Método replace\n",sAmostra.replace(10,18))
print("sAmostra após Método replace\n",sAmostra)
'''

#COMPLETE:
#============================================
#
# Crie as series dos dias 1 e 2
sDia2=pd.read_excel('dia2.xlsx', header=0,index_col=0,squeeze=True,decimal=',')
print(sDia2.head(10))
sDia1=pd.read_excel('dia1.xlsx', header=0,index_col=0,squeeze=True,decimal=',')
print(sDia1.head(10))
print('\n-----------------------------------------------------\n')
#
#============================================
# Após criar as series dos dias 1 e 2
#============================================   
#   
#=----------------------------------------------------------
# Concatene-as, mantendo a informação do dia no índice
sDiaJunto=pd.concat({'Dia1':sDia1,'Dia2':sDia2})
print(sDiaJunto)
print('\n-----------------------------------------------------\n')

#   Analise as medidas estatísticas por dia/hora
print(sDiaJunto.mean(level=[0,1]))
print(sDiaJunto.median(level=[0,1]))
print(sDiaJunto.max(level=[0,1]))
print(sDiaJunto.min(level=[0,1]))
print('\n-----------------------------------------------------\n')

#   Analise as medidas estatísticas por hora/dia
print(sDiaJunto.mean(level=[1,0]).sort_index())
print(sDiaJunto.median(level=[1,0]).sort_index())
print(sDiaJunto.max(level=[1,0]).sort_index())
print(sDiaJunto.min(level=[1,0]).sort_index())
print('\n-----------------------------------------------------\n')

# 	Em qual dia há maior número  de registros?
s=sDiaJunto.count(level=0)
print(s.loc[s==s.max()].index.values)
#A QUANTIDADE DE REGISTROS É IGUAL!!!
#============================================



