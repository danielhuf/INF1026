# -*- coding: utf-8 -*-
"""
Exercicio de Series: alunos e cursos
"""

import pandas as pd
import matplotlib.pyplot as plt

'''
CRIAR a series sAlCur, lendo dados do arquivo alunosecursos.xlsx
'''
sAlCur=pd.read_excel('alunosecursos.xlsx',sheet_name="Cursos",index_col=0,squeeze=True,
                         header=None, decimal='.')

sAlCR=pd.read_excel('alunosecursos.xlsx',sheet_name="CR",index_col=0,squeeze=True,
                         header=None, decimal='.')

'''
EXIBIR as series criadas
'''
print('\nsAlunos x Cursos:\n')
print(sAlCur)
print('\nsAlunos x CRs:\n')
print(sAlCR)
print('\n-----------------------------------------------------\n')

'''
EXIBIR as 4 primeiras linhas da sAlCur: usar head()
'''
print('\n4 Primeiras linhas:\n')
print(sAlCur.head(4))
print('\n-----------------------------------------------------\n')


'''
EXIBIR as 3 ultimas linhas da sAlCur: usar tail()
'''
print('\n3 Últimas linhas:\n')
print(sAlCur.tail(3))
print('\n-----------------------------------------------------\n')


'''
EXIBIR os indices  da sAlCur:  index
'''

print('\nÍndices:\n')
print(sAlCur.index)
print('\n-----------------------------------------------------\n')

'''
EXIBIR os valores  da sAlCur:  values
'''
print('\nValores:\n')
print(sAlCur.values)
print('\n-----------------------------------------------------\n')


'''
EXIBIR numero de linhas da series:  size
'''
print('\nNúmero de linhas da series:\n')
print(sAlCur.size)
print('\n-----------------------------------------------------\n')


'''
EXIBIR numero de linhas VALIDAS da series: count()
'''
print('\nNúmero de linhas Válidas da series:\n')
print(sAlCur.count())
print('\n-----------------------------------------------------\n')

'''
EXIBIR numero de linhas COM VALORES AUSENTES da series:
'''
qtAusentes= (sAlCur.isnull()).sum() # ou sAlCur.size-sAlCur.count()
print('\nNúmero de linhas com VAlores Ausentes da series:\n')
print(qtAusentes)
print('\n-----------------------------------------------------\n')


'''
CONSTRUINDO a TABELA DE FREQUENCIA: usar  value_counts()
        Curso - Qt de Ocorrências do curso
CRIAR a partir da sAlCur uma nova series (srCursos) 
onde os indices sao nomes de CURSO (uma vez cada)  
e os valores a quantidade  de vezes que cada curso ocorreu  na sAlCur:  
A  TABELA  DE FREQUÊNCIA É UMA SERIES???? ( verifique, use o type())
    
'''
srCursos=sAlCur.value_counts()
print(type(srCursos))
#Sim, é uma Series
print('\n-----------------------------------------------------\n')

'''
EXIBIR a series srCurso (que corresponde a tabela de frequencia)
Observe a ordenação da tabela de frequência 
'''
print(srCursos)
print('\n-----------------------------------------------------\n')

'''
VISUALIZANDO como grafico de barras: plot.bar(title='CURSOS')
A series original poderia ser visualizada graficamente ??? Porque?
'''
srCursos.plot.bar(title='CURSOS')
plt.show()
#Não, não há dados numéricos para plotar
print('\n-----------------------------------------------------\n')

'''
VISUALIZANDO como grafico pizza e percentuais:  plot.pie(title="CURSOS")
'''
srCursos.plot.pie(title='CURSOS',autopct='%.1f')
plt.show()
print('\n-----------------------------------------------------\n')

'''
CONSERTANDO ERROS:
ENGENHARIA DE COMPUTACAO foi lancada errada em alguns
casos como ENGENHARIA DE COMPUTADORES
ENGENHARIA AMBIENTAL com problema semelhante, 
lançada como ENGENHARIA DO AMBIENTE

POSSIBILIDADE DE SOLUCAO:
aplicar uma funcao que retorna o nome correto 
do valor (do curso). 
'''
'''
PRIMEIRO:
fazer a funcao que recebe o valor (no caso o curso) e retorna 
o nome do curso correto: cursoCerto(val)
DICA: Construa um dicionário interno à função, para o mapeamento
'''
def cursoCerto(v):
    d={'ENGENHARIA DE COMPUTADORES':'ENGENHARIA DE COMPUTACAO','ENGENHARIA DO AMBIENTE':'ENGENHARIA AMBIENTAL'}
    certo=d.get(v,v)
    return certo

'''
SEGUNDO:
aplicar essa funcao a todos os valores (cursos) da series: usar apply  .
Ao usar apply, nesse caso, basta passar a funcao a ser utilizada 
sobre cada um dos valores. O metodo apply se encarregara´ de chamar 
a funcao para cada um dos valores da series.
Retorna uma nova series (srCorrigida)
'''
srCorrigida=sAlCur.apply(cursoCerto)

'''
EXIBIR a series srCorrigida
'''
print(srCorrigida)
print('\n-----------------------------------------------------\n')

'''
TRABALHANDO AGORA com srCorrigida:
Fazer novamente a tabela de frequencia dos cursos, exibir, e visualizar como 
grafico de barras e grafico de pizza
'''
srCursos=srCorrigida.value_counts()
print(srCursos)
srCursos.plot.bar(title='CURSOS')
plt.show()
srCursos.plot.pie(title='CURSOS',autopct='%.1f')
plt.show()
print('\n-----------------------------------------------------\n')

'''
CONSERTANDO OUTROS ERROS:

TODOS OS caracteres DOS NOMES devem FICAR MAIÚSCULOS
    Aplicar o método str.upper()
    
PROBLEMA p/usar o apply: nomes são valores de índices
   
POSSIBILIDADE DE SOLUCAO: criar uma series invertida

'''

'''
CONSTRUIR A SERIE INVERSA: índice: cursos, valores: nome do aluno
'''
print('\n-----------------------------------------------------\n')
print('\nsSeries Invertida: Cursos x Alunos:\n')
sInv=pd.Series(srCorrigida.index,srCorrigida.values)
print(sInv)
print('\n-----------------------------------------------------\n')

'''
CORRIGIR OS NOMES --> tudo em maiúsculo gerando a series sInvCor
'''
sInvCor=sInv.str.upper()

'''
EXIBIR a series sInvCor corrigida
'''
print(sInvCor)
print('\n-----------------------------------------------------\n')

'''
TEM INDICES REPETIDOS: listar um indice uma unica vez (unique())
'''
print(list(sInvCor.index.unique()))
print('\n-----------------------------------------------------\n')

'''
MEDIDAS INTERESSANTES POR CURSO: CUIDADO--> dados textuais
    qt de alunos por curso, 
    curso(s) com menor quantidade de alunos, 
    curso(s) com maior quantidade de alunos,

'''
print(srCursos.loc[srCursos==srCursos.max()].index.values)
print(srCursos.loc[srCursos==srCursos.min()].index.values)
print('\n-----------------------------------------------------\n')

'''
GRUPOS E AGRUPAMENTOS
'''

'''
AGRUPANDO a serie sInvCor por Curso( curso<-->indices com repetição)
'''
gInvCor=sInvCor.groupby(level=0)

'''
EXIBIR o dicionário com as informações dos grupos formados ( groups)
'''
print(gInvCor.groups)
print('\n-----------------------------------------------------\n')

'''
EXIBIR o tamanho dos grupos formados --> que tipo de estrutura?
'''
print(gInvCor.agg('size'))
print('\n-----------------------------------------------------\n')

'''
EXIBIR os alunos por curso --> que tipo de estrutura?
'''
print(gInvCor.agg('unique'))
print('\n-----------------------------------------------------\n')

'''
EXIBIR os elementos do  grupo ENGENHARIA
'''
print(gInvCor.get_group('ENGENHARIA'))
print('\n-----------------------------------------------------\n')

'''
AGRUPANDO por TIPO DE CURSO (função para determinar o tipo de Curso):
   Grupo COMP : todos os cursos da computação
   Grupo IND: só 'ENGENHARIA'
   Grupo ENG: os demais cursos
'''

'''
PRIMEIRO:
fazer a funcao TipoCurso que 
        recebe o valor (no caso o curso) e
        retorna COMPUTACAO ou DEMAIS
'''
def TipoCurso(g):
    if g in ['ENGENHARIA DE COMPUTACAO','CIENCIA DA COMPUTACAO']:
        return 'COMP'
    elif g=='ENGENHARIA':
        return 'IND'
    return 'ENG'

'''
SEGUNDO:
usar esta funcao para o agrupamento
'''
gTipoCurso=sInvCor.groupby(by=TipoCurso)

'''
EXIBIR a quantidade de  alunos por grupo
'''
print(gTipoCurso.agg('size'))
print('\n-----------------------------------------------------\n')

'''
EXIBIR a quantidade de alunos com sobrenome SA e SO em cada grupo
 criar uma função que recebe o grupo, filtra SA e SO e retorna a quantidade
 Lembre-se que True tem valor 1 e False tem valor 0
'''
#DUVIDA -- Usar gTipoCurso
def sobrenome(g):
    filtro=g.str.contains('SA')|g.str.contains('SO')
    s=filtro.value_counts()
    s.plot.pie(figsize=(8,8),autopct='%.1f')
    plt.show()
    return filtro.sum()

print(gTipoCurso.agg(sobrenome))

'''
QUAL o % de alunos com sobrenome SA e SO por grupo
Exibir c/ percentual e gráfico de pizza
'''
#Já está inserido na função
#######################################################
#    Usando sAlCR
######################################################

'''
QUAL o CR médio?
'''
print(sAlCR.mean())
print('\n-----------------------------------------------------\n')

'''
Quais alunos tem o maior CR?
'''
print(sAlCR.loc[sAlCR==sAlCR.max()].index.values)
print('\n-----------------------------------------------------\n')

'''
AGRUPANDO por Curso ( usar a series sAlCur):
    Qual o menor cr o maior CR o CR mediano e o CR médio de cada curso?
    Quais alunos com maior CR por curso?
'''
gCR=sAlCR.groupby(by=sAlCur)
print(gCR.agg(['max','median','mean']))
print('\n-----------------------------------------------------\n')
    
print(gCR.agg('idxmax'))
#De outra maneira, poderia utilizar a mesma função da moda em grupos, só qu com o idxmax.

