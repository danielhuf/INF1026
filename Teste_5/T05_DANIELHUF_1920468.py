#Nome completo: Daniel Stulberg Huf
#Matrícula PUC-Rio: 1920468
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, 
#sem consultas a outros alunos, professores ou qualquer outra pessoa.

import pandas as pd
import matplotlib.pyplot as plt

'''  
A Series srAleCurso foi criada lendo dados do arquivo alunosecursos.xlsx. 
Cada linha tem o nome do aluno e seu curso. 
'''
srAleCurso=pd.read_excel('alunosecursos.xlsx',index_col=0,header=None,squeeze=True)

print('******************************************************')
'''  EXIBIR a series criada  '''
print('Exibindo a series construida:\n')
print(srAleCurso)

'''  EXIBIR as 4 primeiras linhas da srAleCurso  '''
print('\nExibindo as 4 primeiras linhas da srAleCurso:\n')
print(srAleCurso.head(4))

'''  EXIBIR as 3 ultimas linhas da srAleCurso  '''
print('\n Exibindo as 3 ultimas linhas da srAleCurso:\n')
print(srAleCurso.tail(3))

print('\n******************************************************')
print('Indices, Valores, Numero de Linhas')

''' EXIBIR os indices da srAleCurso:   '''
print('\nExibindo os indices da srAleCurso:\n')
print(srAleCurso.index)

''' EXIBIR os valores da srAleCurso:   '''
print('\nExibindo os valores da srAleCurso:\n')
print(srAleCurso.values)

''' EXIBIR tamanho (numero de linhas) da series:   '''
print('\nExibindo o tamanho (numero de linhas) da series:\n')
print(srAleCurso.size)

print('\n******************************************************')

''' EXIBIR o curso do aluno de nome LINO :  '''
print('\nExibindo o curso do aluno de nome LINO:\n')
print(srAleCurso.loc['LINO'])

''' EXIBIR o curso do aluno de nome PEPA :  '''
print('\nExibindo o curso do aluno de nome PEPA:\n')
print(srAleCurso.loc['PEPA'])

print('\n******************************************************')
print('Eliminando: ')

''' ELIMINAR de srAleCurso linhas com curso nao preenchido: '''
print('\nEliminando de srAleCurso linhas com curso não preenchido:\n')
srAleCurso.dropna(inplace=True)

''' EXIBIR srAleCurso atualizada '''
print('Exibindo srAleCurso atualizada:\n')
print(srAleCurso)

''' CRIAR sCopia como sendo uma copia de srAleCurso '''
print('\nCriando sCopia como sendo uma copia de srAleCurso:\n')
sCopia=srAleCurso.copy()

''' ELIMINAR de sCopia os alunos VAVA, LUNA, DEDE em um comando  '''
print('Eliminando de sCopia os alunos VAVA, LUNA, DEDE em um comando:\n')
sCopia.drop(['VAVA','LUNA','DEDE'],inplace=True)

''' EXIBIR a sCopia depois das eliminacoes '''
print('Exibindo a sCopia depois das eliminacoes:\n')
print(sCopia)

''' EXIBIR o tamanho da sCopia depois das eliminacoes '''
print('\nExibindo o tamanho da sCopia depois das eliminacoes:\n')
print(sCopia.size)

print('\n******************************************************')

''' EXIBIR srAleCurso original novamente, continuaremos com ela '''
print('\nExibindo srAleCurso original novamente, continuaremos com ela:\n')
srAleCurso=pd.read_excel('alunosecursos.xlsx',index_col=0,header=None,squeeze=True)
print(srAleCurso)

print('\n******************************************************')
print('ORDENANDO:')

''' Exibir srAleCurso ordenada por indices  '''
print('\nExibindo srAleCurso ordenada por indices:\n')
print(srAleCurso.sort_index())

''' Exibir srAleCurso ordenada pelos valores  '''
print('\nExibindo srAleCurso ordenada pelos valores:\n')
print(srAleCurso.sort_values())

print('\n******************************************************')
'''  
A Series srNotas foi criada lendo dados do arquivo NotasCurso.xlsx. 
Cada linha tem o nome do aluno e sua nota. 
'''
srNotas = pd.read_excel('NotasCurso.xlsx', squeeze=True, header=None, index_col=0)

''' INCLUIR o aluno JOCA com nota 7.1'''
print('\nIncluindo o aluno JOCA com nota 7.1:')
srNotas.loc['JOCA']=7.1

''' EXIBIR a srNotas depois da inclusão'''
print('\nExibindo a srNotas depois da inclusão:\n')
print(srNotas)

''' EXIBIR a nota do 5o. colocado ao 10o. colocado com um unico comando. Considere como 
1o. colocado o com maior nota:  '''
print('\nExibindo  a nota do 5o. colocado ao 10o. colocado com um unico comando. Considere como 1o. colocado o com maior nota:\n')
print(srNotas.sort_values(ascending=False).iloc[4:9])

''' ALTERAR a nota dos 4 melhores alunos. A nova nota eh 10
      OU
    ALTERAR a nota dos 4 primeiros colocados. A nova nota eh 10.'''
print('\nAlterando a nota dos 4 melhores alunos. A nova nota é 10:\n')
srNotas.sort_values(ascending=False,inplace=True)
srNotas.iloc[0:4]=10

''' EXIBIR a srNotas depois da alteração'''
print('\nExibindo a srNotas depois da alteração:\n')
print(srNotas)

print('VISUALIZANDO:')

''' VISUALIZANDO como grafico de barras com o nome dos alunos em ordem alfabética'''
print('\nVisualizando como grafico de barras com o nome dos alunos em ordem alfabética:')
srNotas.sort_index().plot.bar(figsize=(8,8),title='Nota dos Alunos')
plt.show()

''' VISUALIZANDO como grafico de pizza com valores percentuais '''
print('\nVisualizando como grafico de pizza com valores percentuais:')
srNotas.sort_index().plot.pie(figsize=(8,8),autopct='%.1f')
plt.show()
