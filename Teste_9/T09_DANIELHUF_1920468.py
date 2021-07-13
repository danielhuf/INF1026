#Nome completo: Daniel Stulberg Huf
#Matrí­cula PUC-Rio: 1920468
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, 
#sem consultas a outros alunos, professores ou qualquer outra pessoa.

"""
O arquivo NtBlocos contém informações sobre os alunos de uma turma organizadas em 4 planilhas, 
da seguinte forma: 
=> bloco1: notas para compor o grau G1, isto é, nota de uma prova e 3 notas de teste
=> bloco2: notas para compor o grau G2, isto é, nota de uma prova e 3 notas de teste
=> dados: sexo e idade 
=> faltas: numero de faltas
Todas as planilhas tem na primeira coluna os nomes dos alunos.
Para cada uma destas planilhas foi criada uma estrutura de dados da biblioteca Pandas.
Para as 3 primeiras planilhas os respectivos DataFrames: dfBloco1, dfBloco2 e dfDados.
Para a última planilha, a Series srFaltas.
O objetivo final é construir um DataFrame (dfFinal) contendo o grau1, grau2, grau final e a 
situação dos alunos. 
Preencha cada um dos itens solicitados.
"""

'''
ATENÇÃO: SUA SOLUÇÃO TEM QUE MANIPULAR AS ESTRUTURAS DA BIBLIOTECA PANDAS DENOMINADAS 
DATAFRAME OU SERIES E USAR OS MÉTODOS APRESENTADOS E TRABALHADOS NAS AULAS E NO MATERIAL 
DISPONIBILIZADO. NÃO É PERMITIDO TRANSFORMÁ-LAS EM OUTRAS ESTRUTURAS PARA OBTER A RESPOSTA 
PEDIDA.
'''

import pandas as pd
import matplotlib.pyplot as plt

''' Estruturas já criadas '''
dfBloco1= pd.read_excel('NtBlocos.xlsx',sheet_name='bloco1',index_col=0,header=0)
dfBloco1 = pd.DataFrame(dfBloco1)
dfBloco2= pd.read_excel('NtBlocos.xlsx',sheet_name='bloco2',index_col=0,header=0)
dfBloco2 = pd.DataFrame(dfBloco2)
dfDados= pd.read_excel('NtBlocos.xlsx',sheet_name='dados',index_col=0,header=0)
dfDados = pd.DataFrame(dfDados)
srFaltas= pd.read_excel('NtBlocos.xlsx',sheet_name='faltas',squeeze=True,index_col=0,header=0)

'''Exibir as 4 estruturas criadas '''
print('\n1 - dfBloco1')
print(dfBloco1)
print('---------------------------------------------------------------')

print('\n2 - dfBloco2')
print(dfBloco2)
print('---------------------------------------------------------------')

print('\n3 - dfDados')
print(dfDados)
print('---------------------------------------------------------------')

print('\n4 - srFaltas')
print(srFaltas)
print('---------------------------------------------------------------')

'''Renomear as colunas de dfBloco1 para que sejam P1, T1, T2 e T3'''
print('\n5 - dfBloco1 com colunas renomeadas' )
dfBloco1.rename(columns={'PROVA1':'P1','TESTE1':'T1','TESTE2':'T2','TESTE3':'T3'},inplace=True)
print(dfBloco1)
print('---------------------------------------------------------------')

'''Renomear as colunas de dfBloco2 para que sejam P2, T1, T2, T3'''
print('\n6 - dfBloco2 com colunas renomeadas' )
dfBloco2.rename(columns={'PROVA2':'P2','TESTE1':'T1','TESTE2':'T2','TESTE3':'T3'},inplace=True)
print(dfBloco2)
print('---------------------------------------------------------------')

''' Substituir no dfBloco1 e no dfBloco2 notas ausentes por 0 (zero)  '''
print('\n7 - dfBloco1 sem valores ausentes')
dfBloco1.fillna(value=0,inplace=True)
print(dfBloco1)
print('---------------------------------------------------------------')

print('\n8 - dfBloco2 sem valores ausentes')
dfBloco2.fillna(value=0,inplace=True)
print(dfBloco2)
print('---------------------------------------------------------------')

''' Incluir tanto em dfBloco1 como no dfBloco2 uma coluna denominada MTestes que contém a 
media aritmetica das 2 maiores notas de testes '''
print('\n9 - dfBloco1 com nova coluna MTestes ')
def geraMedia(x):
    menorTeste=x.idxmin(axis=1)
    semMenor=x.drop(menorTeste)
    return semMenor.mean()
testes1=dfBloco1[['T1','T2','T3']]
dfBloco1['MTestes']=testes1.T.apply(geraMedia)
print(dfBloco1)
print('---------------------------------------------------------------')

print('\n10 - dfBloco2 com nova coluna MTestes ')
testes2=dfBloco2[['T1','T2','T3']]
dfBloco2['MTestes']=testes2.T.apply(geraMedia)
print(dfBloco2)
print('---------------------------------------------------------------')

''' Incluir em dfBloco1 a coluna G1. Esta coluna armazena a nota da prova somada à 20% da media
 dos testes '''
print('\n11 - dfBloco1 com nova coluna G1 ')
g1=dfBloco1['P1']+dfBloco1['MTestes']*0.2
dfBloco1['G1']=g1
print(dfBloco1)
print('---------------------------------------------------------------')

''' Incluir em dfBloco2 a coluna G2. Esta coluna armazena a nota da prova somada à 20% da media
 dos testes '''
print('\n12 - dfBloco2 com nova coluna G2 ')
g2=dfBloco2['P2']+dfBloco2['MTestes']*0.2
dfBloco2['G2']=g2
print(dfBloco2)
print('---------------------------------------------------------------')

''' Criar dfGeral apenas com as colunas G1, G2 e FALTAS. Use o metodo concat da forma mais 
apropriada ''' 
print('\n13 - dfGeral ')
dfGeral=pd.concat([dfBloco1['G1'],dfBloco2['G2'],srFaltas],axis=1)
print(dfGeral)
print('---------------------------------------------------------------')

''' Incluir em dfGeral a coluna GParcial cujos valores são a media ponderada de G1 e G2, 
sendo G1 com peso 2 e G2 com peso 3  ''' 
print('\n14 - dfGeral com coluna GParcial')
dfGeral['GParcial']=(dfGeral['G1']*2+dfGeral['G2']*3)/5
print(dfGeral)
print('---------------------------------------------------------------')

''' Incluir em dfGeral a coluna SitParc com a situação de cada aluno:
    . FINAL se 0 <= grau parcial(GPARCIAL) <= 6.0
    . APV_REG se 6 < grau parcial(GPARCIAL) <= 8.0 
    . APV_MBOM se 8 < grau parcial(GPARCIAL) <= 10.0 '''
print('\n15 - dfGeral com coluna SitParc (Situacao Parcial)')
def detSit(al):
    if al['GParcial']>=0 and al['GParcial']<=6:
        return 'FINAL'
    elif al['GParcial']<=8:
        return 'APV_REG'
    else:
        return 'APV_MBOM'
dfGeral['SitParc']=dfGeral.apply(detSit,axis=1) 
print(dfGeral)
print('---------------------------------------------------------------')

'''
Exibir graficamente (barras) num único grafico apenas as notas de G1 e de G2  '''
print('\n16 - Grafico de barras de G1 e G2 ')
dfGeral[['G1','G2']].plot.bar(figsize=(7,5))
plt.show()

''' Incluir em dfGeral a coluna GFinal. O grau final (GFinal) dos aluno é calculado 
acrescentando no máximo 0.5 ao grau parcial de acordo com a frequencia. Tem direito 
a este acrescimo os alunos que tiveram até 2 faltas inclusive, desde que seu grau 
final não ultrapasse a nota 10 (nota maximo). Esta coluna tem que ser criada por 
meio de uma função e o método apply '''
def detFinal(al):
    if al['FALTAS']<=2:
        grau=al['GParcial']+0.5
        if grau>10:
            grau=10
    else:
        grau=al['GParcial']
    return grau
dfGeral['GFinal']=dfGeral.apply(detFinal,axis=1)

print('\n17 - dfGeral com coluna GFinal (Grau Final) ')
print(dfGeral)
print('---------------------------------------------------------------')

''' Exibir para cada aluno o valor do maior grau entre G1 e G2 ''' 
print('\n18 - Aluno e o valor do maior grau: G1 ou G2 ')
print(dfGeral[['G1','G2']].max(axis=1))
print('---------------------------------------------------------------')

''' Exibir a quantidade de alunos por idade (tabela de frequencia) '''
print('\n19 - Quantidade de alunos por idade ')
print(dfDados['IDADE'].value_counts())
print('---------------------------------------------------------------')

'''Exibir graficamente (pizza) o percentual de meninas e de meninos '''
print('\n20 - Graficamente o percentual de meninas e de meninos')
dfDados['SEXO'].value_counts().plot.pie(autopct='%.2f',figsize=(5,5))
plt.show()

''' Incluir em dfGeral a coluna SitFinal com a situação de cada aluno:
    . FINAL se 0 <= grau final(GFinal) <= 6.0
    . APV_REG se 6 < grau final(GFinal) <= 8.0 
    . APV_MBOM se 8 < grau final(GFinal) <= 10.0 '''
print('\n21 - dfGeral com coluna SitFinal (Situacao Final)')
def detgFinal(al):
    if al['GFinal']>=0 and al['GFinal']<=6:
        return 'FINAL'
    elif al['GFinal']<=8:
        return 'APV_REG'
    else:
        return 'APV_MBOM'
dfGeral['SitFinal']=dfGeral.apply(detgFinal,axis=1) 
print(dfGeral)
print('---------------------------------------------------------------')

''' Para observar o impacto da frequencia no grau do aluno exibir as colunas GParcial, 
SitParc, GFinal e SitFinal  do dfGeral '''
print('\n22 - Impacto da frequencia no grau do aluno')
print(dfGeral[['GParcial','SitParc','GFinal','SitFinal']])
print('---------------------------------------------------------------')

''' Elimine as colunas GParcial e SitParc. Exiba dfGeral atualizado  '''
print('\n23 - dfGeral final')
dfGeral.drop(['GParcial','SitParc'],axis=1,inplace=True)
print(dfGeral)
print('---------------------------------------------------------------')

