import pandas as pd
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#  Criando DataFrame a partir do  arquivo excelo arquivo Alunos.xlsx contém dados dos alunos 
#     Todas as planilhas contém linhas de cabeçalho e 
#     a COLUNA 1 - Nome - deve ser utilizada como index
#
#   dfDad: planilha Dados
#   dfNtA: planilha A
#   dfNtA: planilha B
#   dfTes: planilha Testes
#
#   Planilha com dados da Turma, indexar pela coluna 0
#   dfTur: planilha Turma
#------------------------------------------------------------------------------
#-------------------------------------------------------------------------------


dfDad=pd.read_excel("Alunos.xlsx",sheet_name='Dados',decimal=',',header=0,index_col=1)
dfNtA=pd.read_excel("Alunos.xlsx",sheet_name='A',decimal=',',header=0,index_col=1)
dfNtB=pd.read_excel("Alunos.xlsx",sheet_name='B',decimal=',',header=0,index_col=1)
dfTes=pd.read_excel("Alunos.xlsx",sheet_name='Testes',decimal=',',header=0,index_col=1)
#   dfTur: planilha Tuma
dfTur=pd.read_excel("Alunos.xlsx",sheet_name='Turma',decimal=',',header=0,index_col=0)
dfTur=pd.DataFrame(dfTur) # para que o Spyder mostre os argumentos dos métodos

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#   INSERINDO/SELECIONANDO/ALTERANDO/DESCARTANDO/REARRUMANDO o dfNtA
#------------------------------------------------------------------------------
#----------------------------------------------------------------------------

#incluir no dfNtA, o número da turma: A (1ª coluna)
lIndiceNotas=list(dfNtA.columns)
lIndiceNotas.insert(0,'Turma') #['Turma','Matr','Faltas','P1','P2'] 
dfNtA['Turma']='A'
dfNtB['Turma']='B'
dfNtA=dfNtA[lIndiceNotas]
print("\n###############################\n")
print("\ndfNtA com a turma\n",dfNtA)
print("\n###############################\n")

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#   CONCATENANDO
#------------------------------------------------------------------------------
#----------------------------------------------------------------------------

#Concatenar  dfNtA e  dfNtB==> dfNt  com sort=False as colunas ficam na ordem original
# Execute com ignore_index = False(padrão)==> dfNt
#Solução em 2 passos
dfNt=pd.concat([dfNtA,dfNtB],sort=False)

#Concatenar  dfNtA e  dfNtB==> dfNt  com sort=True, as colunas ficam ordenadas pelos labels
print(pd.concat([dfNtA,dfNtB],sort=True))

print("\n###############################\n")
print("\n1.dfNt - Turmas concatenadas:\n Primeiros\n",dfNt.head(3),"\n Últimos\n",dfNt.tail(3))
print("\n###############################\n")

# Execute a concatenação com ignore_index =True ==>dfNtI

print('1a-ignore-index\n')
print(pd.concat([dfNtB,dfNtA],ignore_index=True))
#Execute com ignore_index =True, incluindo o nome ==>dfNtINome
print('1b- reset_index,ignore-index,\n')
d1=dfNtA.reset_index()  #Transforma indice em coluna
d2=dfNtB.reset_index()
print(pd.concat([d1,d2],ignore_index=True))
#d1.set_index('Matr') - A matricula virou index

print("\n###############################\n")
print("\n1.e) Relação gráficas das notas da P1 e da P2")
print("\n###############################\n")
dfNtA.plot.scatter(x='P1', y='P2')  
plt.show()  

#Concatenar   dfNt  com os testes (dfTes), gerando dfNotas
dfNotas=pd.concat([dfNt.drop('Matr',axis=1),dfTes],axis=1,sort=False) #dropei a matr em um df, pq matr se repete
dfNotas.rename_axis('Nome',axis=0,inplace=True)
#  Para alunos de mesmo nome (mesmo index), incluir as notas de teste ( eixo: columns)
#      Colunas de DfTes: ['Matr', 'T1A', 'T1B', 'T2A', 'T2B']
#      Colunas de dfNt: ['Turma', 'Matr', 'Faltas', 'P1', 'P2']
#  Para não duplicar a coluna Matr, excluir ANTES da concatenação uma das cols Matr
#  Renomear o index para 'Nome'
# Observar o que acontece com alunos (Pedrinho e Zezinho) do dfNt que não constam no dfTes

print("\n###############################\n")
print("\n2.dfNotas - Provas e Testes:")
print("\n###############################\n")

# substituir valores ausentes por 0
dfNotas.fillna(0,inplace=True)

# 3-  Acrescentar à P1, o acréscimo respectivo à turma do aluno ( A ou B )--> dfTur
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
#      1.5) Atualizar P1 de dfNotas e incluir Turno  --> dfGeral

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
# 1.1 - Construir dfAux indexado por turma
dfAux=dfNotas[['P1','Turma']]
dfAux.reset_index(inplace=True)
dfAux.set_index(keys=dfAux['Turma'], inplace=True)
# 1.2 - Concatenar dfTur à dfAux
dfAux=pd.concat([dfAux,dfTur], join='inner',axis=1,sort=False)
# 1.3 - Somar colunas P1 e Acr em dfAux
dfAux['P1']=dfAux['P1'].add(dfAux['Acr'])
# 1.4 - Indexar dfAux por nome
dfAux.set_index(keys=dfAux['Nome'],inplace=True)
# 1.5 - Criar dfGeral com P1 de dfNotas atualizada e incluir Turno
dfGeral=dfNotas.copy()
dfGeral[['P1','Turno']]=dfAux[['P1','Turno']]

dfAux.drop('Acr',axis=1,inplace=True)
f=dfAux['P1']>10
dfAux.loc[f,'P1']=10

print("\n###############################\n")
print("\n3.a)dfNotas com P1 ajustada e Turno (dfGeral):")
print("\n###############################\n")
#--------------------------------------------------------------

#--------------------------------------------------------------
# Estratégia  2:    MAIS COMPLEXA (NÃO FAZER)
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
#dfGeral=dfNotas.apply(Atualiza, args=(dfTur,), axis=1)

print("\n###############################\n")
print("\n3.b)dfGeral com P1 ajustada e Turno:")
print("\n###############################\n")
#--------------------------------------------------------------

#4-Concatenar   dfDad à dfGeral
#  Para alunos de mesmo nome (mesmo index), incluir o curso e os créditos cursados ( eixo columns)
#      Colunas de dfGeral: 
#        ['Turma', 'Matr', 'Faltas', 'P1', 'P2', 'T1A', 'T1B', 'T2A', 'T2B','Turno']
#      Colunas de dfDad: 
#         ['Matr', 'Curso', 'CreditosCursados']
#  Para não duplicar a coluna Matr, excluir ANTES da concatenação uma das cols Matr
# 
dfGeral=pd.concat([dfGeral,dfDad.drop('Matr',axis='columns')],axis=1)
print("\n###############################\n")
print("\n4)dfGeral com dados do curso:\n Primeiros \n",dfGeral.head(5),'\n  Últimos\n',dfGeral.tail(2))
print("\n###############################\n")

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#   5 - OPERAÇÕES ARITMÉTICAS
#------------------------------------------------------------------------------
#----------------------------------------------------------------------------

# a)Calcule as Notas G1,G2  ==> Ti*0.2 + Pi*0.8
dfGeral['G1']=dfGeral['P1']*0.8 + dfGeral[['T1A','T1B']].mean(axis='columns')*0.2
dfGeral['G2']=dfGeral['P2']*0.8 + dfGeral[['T2A','T2B']].mean(axis='columns')*0.2
print("\n###############################\n")
print("\n5.a) Resultado da G1,G2 \n Primeiros\n", dfGeral[['G1','G2']].head())
print("\n###############################\n")

# b) Calcule a Média Aritmética de cada aluno
dfGeral['Media']=dfGeral[['G1','G2']].mean(axis='columns')
print("\n###############################\n")
print("\n5.b) Média Aritmética de cada aluno \n Primeiros\n", dfGeral[['Media']].head())
print("\n###############################\n")

# c)Inclua uma coluna com a situação do Aluno: Ap ou G3
def detSit(al):
    if al['Media']>=5 and al['G1']>=3 and al['G2']>=3:
        return 'AP'
    else:
        return 'G3'
dfGeral['Sit']=dfGeral.apply(detSit,axis='columns') 
print("\n###############################\n")
print("\n5.c)Situação Final\n",dfGeral[['Turma','Turno','Faltas','P1','P2','G1','G2','Media','Sit']])# Inclua uma coluna com a  do Aluno: Ap ou G3
print("\n###############################\n")

# d)exibir graficamente a quantidade de alunos em G3 x AP 
print("\n###############################\n")
print("\n 5.d)quantidade de alunos em G3 e AP \n")
dfGeral['Sit'].value_counts().plot.pie(title="Situação",legend=True,autopct="%.1f")
plt.show()
print("\n###############################\n")

# Qual a relação gráfica (scatter) entre os  alunos em G3 e    faltas 
#
d=dfGeral.copy()
f=d['Sit']!='G3'
d['Sit'].loc[f]=0
f=d['Sit']=='G3'
d['Sit'].loc[f]=1
d.plot.scatter(y='Sit',x='Faltas')