# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 10:11:03 2017

@author: claudia ferlin
"""

import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#  Criando DataFrame a partir do  arquivo excelo arquivo Alunos.xlsx contém dados dos alunos 
#     Todas as planilhas contém linhas de cabeçalho e 
#     a COLUNA 1 - Nome - deve ser utilizada como index
#
#   dfDad: planilha Dados: Matr,Nome,Curso,CreditosCursados de todos os alunos
#   dfNtA: planilha A : Matr,Nome,Faltas,P1,P2 dos alunos da turma A
#   dfNtB: planilha B : Matr,Nome,Faltas,P1,P2 dos alunos da turma B
#   dfTes: planilha Testes : Nome, nota do T1A,nota do T1B,nota do T2A,nota do T2B dos alunos

#
#   Planilha com dados da Turma, indexar pela coluna 0
#   dfTur: planilha Turma : Turma,Turno, valor do Acréscimo na P1

#------------------------------------------------------------------------------
#-------------------------------------------------------------------------------


dfDad=pd.read_excel("Alunos.xlsx",sheet_name='Dados',decimal=',',header=0,index_col=1)
dfNtA=pd.read_excel("Alunos.xlsx",sheet_name='A',decimal=',',header=0,index_col=1)
dfNtB=pd.read_excel("Alunos.xlsx",sheet_name='B',decimal=',',header=0,index_col=1)
dfTes=pd.read_excel("Alunos.xlsx",sheet_name='Testes',decimal=',',header=0,index_col=1)
#   dfTur: planilha Tuma
dfTur=pd.read_excel("Alunos.xlsx",sheet_name='Turma',decimal=',',header=0,index_col=0)

# Para o Spyder
dfDad=pd.DataFrame(dfDad)
dfNtA=pd.DataFrame(dfNtA)
dfNtB=pd.DataFrame(dfNtB)
dfTes=pd.DataFrame(dfTes)
dfTur=pd.DataFrame(dfTur)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#   2. INSERINDO/SELECIONANDO/ALTERANDO/DESCARTANDO/REARRUMANDO o dfNtA
#------------------------------------------------------------------------------
#----------------------------------------------------------------------------

#incluir no dfNtA, o número da turma: A (1ª coluna)
lIndiceNotas=list(dfNtA.columns)
lIndiceNotas.insert(0,'Turma') #['Turma','Matr','Faltas','P1','P2'] 
dfNtA['Turma']='A'
dfNtB['Turma']='B'
dfNtA=dfNtA[lIndiceNotas]
print("\n###############################\n")
print("\n2. dfNtA com a turma\n",dfNtA)
print("\n###############################\n")
 
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#   3. CONCATENANDO
#------------------------------------------------------------------------------
#----------------------------------------------------------------------------


#3.1) Concatenar  dfNtA e  dfNtB==> dfNt  com Turma,Matr,Faltas, P1,P2
#  
dfNt=pd.concat([dfNtA,dfNtB], sort=False)

print("\n###############################\n")
print("\n3.1) dfNt - Turmas concatenadas:\n Primeiros\n",dfNt.head(3),"\n Últimos\n",dfNt.tail(3))
print("\n###############################\n")


#3.2) Concatenar   dfNt  com os testes (dfTes), gerando dfNotas
#  Para alunos de mesmo nome (mesmo index), incluir as notas de teste ( eixo: columns)
#      Colunas de DfTes: ['Matr', 'T1A', 'T1B', 'T2A', 'T2B']
#      Colunas de dfNt: ['Turma', 'Matr', 'Faltas', 'P1', 'P2']
#  Para não duplicar a coluna Matr, excluir ANTES da concatenação uma das cols Matr
# Observar o que acontece com alunos (Pedrinho e Zezinho) do dfNt que não constam no dfTes

dfNotas=pd.concat([dfNt,dfTes.drop('Matr',axis='columns')],axis=1,sort=False)
dfNotas.index.name='Nome'
lIndiceNotas.extend(['T1A','T1B','T2A','T2B'])
print("\n###############################\n")
print("\n3.2) dfNotas - Provas e Testes:\n Primeiros \n",dfNotas.head(5),'\n  Últimos\n',dfNotas.tail(2))
print("\n###############################\n")

#--------------------------------------------------------------
# substituir valores ausentes por 0
#--------------------------------------------------------------
dfNotas.fillna(0,inplace=True)

#--------------------------------------------------------------
# 3.4)Acrescentar à P1, o acréscimo respectivo à turma do aluno (A ou B )--> dfTur
#        Turno  Acr
#  Turma           
#  A        M  0.8
#  B        T  0.6
#  
#   Estratégia  1:
#      1.1)Construir dfAux com Turma,Nome e P1 de dfNotas, 
#          indexado por turma p/concatenar com dfTur que
#           é indexado por turma 
#      1.2)Concatenar dfTur à dfAux (como novas colunas)
#           join='inner' para realizar a interseção dos índices
#      1.3) Somar colunas P1 e Acr em dfAux  (o que fazer com notas >10?)
#      1.4) Indexar dfAux por nome
#      1.5) Atualizar P1 de dfNotas e incluir Turno

#   Estratégia  2:
#      2.1)Construir uma função Atualiza que recebe:
#                   a) uma linha do dfNotas (que é uma series com os dados de 1 aluno) e 
#                   b) dfTur
#          A função 
#             a) localiza em dfTur a turma  do aluno
#             b) Soma o acréscimo  da turma à P1 do aluno (ajustando valores >10)
#             c) Inclui a coluna Turno
#             d) Retorna a linha atualizada    
#          como indexador do dfTur
#      2.2)aplicar a função Atualiza a cada linha do dfNotas
#--------------------------------------------------------------

# Estratégia  1:
# 3.4-1.1 - Construir dfAux indexado por turma
dfAux=dfNotas[['P1','Turma']]
dfAux.reset_index(inplace=True)
dfAux.set_index('Turma', inplace=True)
# 3.4-1.2 - Concatenar dfTur à dfAux
dfAux=pd.concat([dfAux,dfTur], join='inner',axis=1,sort=False)
# 3.4-1.3 - Somar colunas P1 e Acr em dfAux
dfAux['P1']=dfAux['P1'].add(dfAux['Acr'])
# 3.4-1.4 - Indexar dfAux por nome
dfAux.set_index('Nome',inplace=True)
# 3.4-1.5 - Criar dfGeral com P1 de dfNotas atualizada e incluir Turno
dfGeral=dfNotas.copy()
dfGeral[['P1','Turno']]=dfAux[['P1','Turno']]
#--------------------------------------------------------------
''''
#--------------------------------------------------------------
# Estratégia  2:
# 2.1 - Construir uma função Atualiza 
def Atualiza(slinhaAluno,dfTur):
    # 2.1.a -localiza em dfTur a series (linha) da turma  do aluno
    turma=slinhaAluno.loc['Turma']
    sTurmaAluno=dfTur.loc[turma]
    # 2.1.b -Soma o acréscimo  da turma à P1 do aluno (ajustando valores >10)
    acr=sTurmaAluno.loc['Acr']
    slinhaAluno.loc['P1']+=acr
    if slinhaAluno.loc['P1']>10:
        slinhaAluno.loc['P1']=10
    # 2.1.c - Inclui a coluna Turno
    slinhaAluno.loc['Turno']=sTurmaAluno.loc['Turno']
    # 2.1.d - Retorna a series do aluno atualizada
    return slinhaAluno

# 2.2 - aplicar a função Atualiza a cada linha do dfNotas
dfGeral=dfNotas.apply(Atualiza, args=(dfTur,), axis=1)
'''
print("\n###############################\n")
print("\n3.4) dfNotas com P1 ajustada e Turno:\n Primeiros \n",dfGeral.head(5),'\n  Últimos\n',dfGeral.tail(2))
print("\n###############################\n")
#--------------------------------------------------------------


#--------------------------------------------------------------
#3.5) Concatenar   dfDad à dfGeral
#  Para alunos de mesmo nome (mesmo index), incluir o curso e os créditos cursados ( eixo columns)
#      Colunas de dfGeral: 
#        ['Turma', 'Matr', 'Faltas', 'P1', 'P2', 'T1A', 'T1B', 'T2A', 'T2B','Turno']
#      Colunas de dfDad: 
#         ['Matr', 'Curso', 'CreditosCursados']
#  Para não duplicar a coluna Matr, excluir ANTES da concatenação uma das cols Matr
# 
#--------------------------------------------------------------
dfGeral=pd.concat([dfGeral,dfDad.drop('Matr',axis='columns')],axis=1,sort=False)
print("\n###############################\n")
print("\n3.5) dfGeral com dados:\n Primeiros \n",dfGeral.head(5),'\n  Últimos\n',dfGeral.tail(2))
print("\n###############################\n")


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#   4) OPERAÇÕES ARITMÉTICAS
#------------------------------------------------------------------------------
#----------------------------------------------------------------------------

#--------------------------------------------------------------
# 4.1) Calcule as Notas G1,G2  ==> Ti*0.2 + Pi*0.8
#--------------------------------------------------------------
dfGeral['G1']=dfGeral['P1']*0.8 + dfGeral[['T1A','T1B']].mean(axis='columns')*0.2
dfGeral['G2']=dfGeral['P2']*0.8 + dfGeral[['T2A','T2B']].mean(axis='columns')*0.2
print("\n###############################\n")
print("\n4.1) Resultado da G1,G2 \n Primeiros\n", dfGeral[['G1','G2']].head())
print("\n###############################\n")

#--------------------------------------------------------------
# 4.2) Calcule a Média Aritmética de cada aluno
dfGeral['Media']=dfGeral[['G1','G2']].mean(axis='columns')
#--------------------------------------------------------------

print("\n###############################\n")
print("\n4.2) Média dos alunos \n Primeiros\n", dfGeral[['G1','G2']].head())
print("\n###############################\n")

#--------------------------------------------------------------
# 4.3) Inclua uma coluna com a situação do Aluno: Ap ou G3
#  O aluno está aprovado, sem G3, se sua média>=5 e nenhum G inferior a 3
#--------------------------------------------------------------
def detSit(al):
    if al['Media']>=5 and al['G1']>=3 and al['G2']>=3:
        return 'AP'
    else:
        return 'G3'
dfGeral['Sit']=dfGeral.apply(detSit,axis='columns') 
print("\n###############################\n")
print("\n4.3) Situação Final\n",dfGeral[['Turma','P1','P2','G1','G2','Media','Turno','Sit']])# Inclua uma coluna com a  do Aluno: Ap ou G3
print("\n###############################\n")
#--------------------------------------------------------------
#--------------------------------------------------------------
# 4.4) exibir graficamente a quantidade de alunos em G3 x AP
#--------------------------------------------------------------
print("\n###############################\n")
print("\n 4.4) quantidade de alunos em G3 e quantidade de alunos AP \n")
print("\n###############################\n")
dfGeral['Sit'].value_counts().plot.pie(title="Situação",legend=True,autopct="%.1f")
plt.show()

#--------------------------------------------------------------


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#   5) FILTRO
#------------------------------------------------------------------------------
#----------------------------------------------------------------------------
#
# 5.0)  Alterar  a nota dos alunos cuja P1 > 10 para 10 -
#       Refazer  graus G1, G2 - Média e Sit do aluno
# 
print("\n###############################\n")
print("\n 5.0) dfGeral - Alunos com notas de P1 Correta \n")
print("\n###############################\n")
f=dfGeral['P1']>10
dfGeral.loc[f,'P1']=10
print(dfGeral)

# 5.1) Exibir Alunos Aprovados 
print("\n###############################\n")
print("\n 5.1) Alunos Aprovados \n")
print("\n###############################\n")

print(dfGeral.query('Sit=="AP"'))
# 5.2) Mostrar quantos alunos cuja G1>G2
#
print("\n###############################\n")
print("\n 5.2) Quantos alunos cuja G1>G2 \n")
print("\n###############################\n")
qt=dfGeral.query('G1>G2').shape[0]
print(qt)      
#
# 5.3) Exibir Alunos Cuja nota Ti > Pi
#
print("\n###############################\n")
print("\n 5.3) Alunos Cuja nota Ti > Pi \n")
print("\n###############################\n")
print(list(dfGeral.query('T1A>P1 or T2A>P1 or T2A>P2 or T2A>P2 ').index))

#
# 5.4) Exibir Alunos Cuja Média é >=5 mas estão em G3
#
print("\n###############################\n")
print("\n 5.4) DF dos Alunos Cuja Média é >=5 mas estão em G3 \n")
print("\n###############################\n")
print(dfGeral.query('Media>=5 and Sit=="G3"'))

#
# 5.5) Para os alunos em G3, qual a nota mínima para aprovação? Média Apr: 5
#
print("\n###############################\n")
print("\n 5.5) Alunos em G3, qual a nota mínima para aprovação\n")
print("\n###############################\n")
dfAux=dfGeral.query('Sit=="G3"')
print(10-dfAux['Media'])
#
# 5.6) Mostrar os alunos com maior número de créditos cursados que estão aprovados
#
print("\n###############################\n")
print("\n 5.6) DF dos Alunos com maior número de créditos cursados que estão aprovados \n")
print("\n###############################\n")
maior=dfGeral['CreditosCursados'].max()
print(dfGeral.query('Sit == "AP" and CreditosCursados =='+str(maior)))
#
# 5.7) Mostrar o nome dos alunos com faltas > média de faltas 
# 
print("\n###############################\n")
print("\n 5.7) Nome dos alunos com faltas > média de faltas \n")
print("\n###############################\n")
media=dfGeral['Faltas'].mean()
dfFaltosos=dfGeral.query('Faltas>='+str(media))
print(list(dfFaltosos.index))

#5.8) Criando uma cópia sem os alunos com faltas > 5. 
#  Lembre-se que o drop necessita de valores de index ou column
#
print("\n###############################\n")
print("\n 5.8) Alunos com até 5 faltas \n")
print("\n###############################\n")
df=dfGeral.copy()
f=dfGeral['Faltas']>5
df.drop(df.loc[f].index,inplace=True)
print(df)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#   6. AGRUPAMENTO, AGREGAÇÃO e CRUZAMENTOS DE DADOS
#------------------------------------------------------------------------------
#----------------------------------------------------------------------------
# 
# 6.1Exibir para cada turno:   
#     Média,Mediana, Menor Nota, Maior Nota, 
#     de P1, P2, G1, G2 e Média
#
#       (AGRUPAR POR TURNO)
gTurnos=dfGeral.groupby('Turno')
# constrói o Df de resumos
dfResumo=gTurnos.agg(['mean','median','min','max'])
dfResumo=dfResumo[['P1','P2','G1','G2']]
# renomeia as colunas
dfResumo.rename(columns={'mean':'Média','median':'Mediana','min':'Menor Nota','max':'Maior Nota'},inplace=True)
# Visualiza os resumos (transposto)

print("\n###############################\n")
print("\n 6.1) Resultados da disciplina POR TURNO\n")
print(dfResumo.T)
print("\n###############################\n")


# 6.2) Exibir para cada curso:   
#     Média,Menor Nota, Maior Nota, 
#     de P1, P2, G1, G2 e Média
#
#       (AGRUPAR POR CURSO)
gTurnos=dfGeral.groupby('Curso')
dfResumo=gTurnos[['P1','P2','G1','G2']].agg(['mean','median','min','max'])

print("\n###############################\n")
print("\n 6.2) Resultados da disciplina POR CURSO\n")
print(dfResumo.T)
print("\n###############################\n")

lNt=['P1','T1A','T1B','G1','P2','T2A','T2B','G2','Media']
lMed=['Média','Mediana','Mínimo','Máximo']

# 6.3) Agrupar por bloco 1(T1A,T1B,P1,G1), 
#                  bloco 2( T2A,T2B,P2,G2), 
#         
# Exibir os dados 
def getBloco(nome):
    if '1' in nome:
        return 'bloco 1'
    elif '2' in nome:
        return 'bloco 2'
    else:
        return None
    
gBlocos=dfGeral.groupby(by=getBloco,axis=1)

print("\n###############################\n")
print("\n 6.3) Resultados por bloco\n")
def exibe(g):
    print('----------------')
    print('Nome:\n',g.name)
    print(g)
    print('----------------')
    return
gBlocos.apply(exibe)
print("\n###############################\n")

# 6.4) a) Quantos alunos nas faixas: 
#             E-  0 a 3.0, 
#             D-3.1 a 5.0, 
#             C– 5.1 a 7, 
#             B – 7.1 a 9.0, 
#             A- 9.1 a 10.0?
# 
#
#   1º) criar as faixas  (pd.cut)
#   2º) criar tabela de frequência  (value_counts())
#
#
# b) Por turno x faixa? c) Por Cursoxfaixa? d) Por Curso/Turnoxfaixa? crosstab
# e) Qual a média mediana em cada turno x faixa
sFx=pd.cut(dfGeral['Media'],
          [0,3,5,7,9,10],
          labels=['E','D','C','B','A'],include_lowest=True)
tfFx=sFx.value_counts()
tfFx=tfFx.loc[['A','B','C','D','E']]

print("\n###############################\n")
print("\n6.4.a) Quantidade de alunos por faixa\n")
print(tfFx)
print("\n###############################\n")

#Por turnoxfaixa?
print("\n###############################\n")
print("\n6.4.b)Quantidade de alunos  por  turno x faixa\n")
print(pd.crosstab(sFx,dfGeral['Turno']))
print("\n###############################\n")

#Por cursoxfaixa?
print("\n###############################\n")
print("\n6.4.c)Quantidade de alunos  por  curso x faixa\n")
print(pd.crosstab(sFx,dfGeral['Curso']))
print("\n###############################\n")

#Por Curso/Turno x faixa?
print("\n###############################\n")
print("\n6.4.d)Quantidade de alunos  por  Curso/Turno x faixa\n")
print(pd.crosstab(sFx,[dfGeral['Curso'],dfGeral['Turno']])) #preciso separar o curso e turno, o crosstab só aceita arrays
print("\n###############################\n")

#Mediana Por Turno x faixa?
print("\n###############################\n")
print("\n6.4.e)Mediana por  Turno x faixa\n")
print(pd.crosstab(sFx,dfGeral['Turno'],rownames=['Faixa'],colnames=['Turnos'],values=dfGeral['Media'],aggfunc='median'))
print("\n###############################\n")

#6.5) Quantos alunos com faltas nas faixas 
#   A(ssíduo)-  0 a 3, 
#   M(édio) - 3 a 6, 
#   F(altosos) >6?
# Por turno? Por Curso? Por Curso/Turno?
# Qual a maior média por faixa de faltas/Curso/Turno? crosstab 
sFaltas=pd.cut(dfGeral['Faltas'],
          [0,3,6,dfGeral['Faltas'].max()],
          labels=['A','M','F'])

print(pd.crosstab(sFaltas,dfGeral['Turno']))
print("\n###############################\n")
print(pd.crosstab(sFaltas,dfGeral['Curso']))
print("\n###############################\n")
print(pd.crosstab(sFaltas,[dfGeral['Curso'],dfGeral['Turno']]))
print("\n###############################\n")
print(pd.crosstab(sFaltas,[dfGeral['Curso'],dfGeral['Turno']],values=dfGeral['Media'],aggfunc='max'))
#
# Qual a relação gráfica (scatter) entre os a média dos alunos em G3 e  faltas 
mediaG3=dfGeral.loc[dfGeral['Sit']=='G3']
dfAux=mediaG3[['Faltas','Media']]
dfAux.plot.scatter(x='Faltas',y='Media')
plt.show()
#


