#Nome completo: Daniel Stulberg Huf
#Matrí­cula PUC-Rio: 1920468
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, 
#sem consultas a outros alunos, professores ou qualquer outra pessoa.

'''
As olimpiadas de jogos online que está em andamento armazena no arquivo jogosonline.xlsx, 
os resultados dos 10 paises melhores colocados. Na primeira planilha deste arquivo está a 
quantidade de medalhas de ouro, prata e bronze conquistadas por esses paises. A segunda 
planilha contem o continente desses paises.
=>a planilha medalhas armazena o QUADRO GERAL DE MEDALHAS, isto é, a quantidade de medalhas 
de cada tipo de um país. A primeira linha contem as informações do primeiro colocado até o 
momento, e assim sucessivamente.
=>a planilha continente contém o nome do continente a que pertence um dado país.
As planilhas têm uma linha de cabeçalho, com os nomes das colunas.

Usaremos as seguintes estruturas que já foram criadas neste arquivo:
    •	dfMedalhas, um DataFrame, onde o índice é o nome do pais e as colunas OURO, PRATA e 
    BRONZE contem as quantidades de medalhas de cada tipo conquistadas
    •	srCont, uma Series, onde o índice é o nome do país e o valor, o CONTINENTE ao qual 
    pertence o país. 
'''

'''
ATENÇÃO: SUA SOLUÇÃO TEM QUE MANIPULAR AS ESTRUTURAS DA BIBLIOTECA PANDAS DENOMINADAS 
DATAFRAME OU SERIES E USAR OS MÉTODOS APRESENTADOS E TRABALHADOS NAS AULAS E NO MATERIAL 
DISPONIBILIZADO. NÃO É PERMITIDO TRANSFORMÁ-LAS EM OUTRAS ESTRUTURAS PARA OBTER A RESPOSTA 
PEDIDA.
'''

import pandas as pd

dfMedalhas = pd.read_excel('jogosonline.xlsx',index_col=0,header=0 )
srCont= pd.read_excel('jogosonline.xlsx', sheet_name='continente', squeeze=True, 
                      index_col=0, header=0 )
print('\n---------------------------------------------------')
''' Exibir o dataframe dfMedalhas criado, em ordem alfabética de nome dos países.  '''
print('1 - Dataframe de medalhas ordenado por nome dos Paises')
print(dfMedalhas.sort_index())
print('\n---------------------------------------------------')

''' Exibir os atributos solicitados para dfMedalhas  '''
print('\n2.1 - Indices de dfMedalhas')
print(dfMedalhas.index.values)
print('\n---------------------------------------------------')

print('\n2.2 - Colunas de dfMedalhas:')
print(dfMedalhas.columns.values)
print('\n---------------------------------------------------')

print('\n2.3 - Valores de dfMedalhas:')
print(dfMedalhas.values)
print('\n---------------------------------------------------')

print('\n2.4 - Shape: linhas X colunas : {}'.format(dfMedalhas.shape))
print('\nNum de Linhas: {}'.format(dfMedalhas.index.size))
print('\nNum de Colunas: {}'.format(dfMedalhas.columns.size))
print('\n---------------------------------------------------')

''' Exibir a quantidade de medalhas de cada tipo para o pais CANADA  '''
print('\n3 - Medalhas do CANADA:')
print(dfMedalhas.loc['CANADA'])
print('\n---------------------------------------------------')

''' Caso um paises não tenha conquistado medalhas de um determinado tipo a respectiva 
celula está vazia no arquivo jogosonline.xlsx. No Dataframe gerado a partir deste arquivo, 
substitua os valores ausentes por 0 (zero). Exiba-o. '''
print( '\n4 - dfMedalhas com quantidades atualizadas.')
dfMedalhas.fillna(0,inplace=True)
print(dfMedalhas)
print('\n---------------------------------------------------')

''' Exibir a quantidade de medalhas de OURO para o pais ALEMANHA  '''
print('\n5 - Medalhas de OURO da Alemanha:')
print(dfMedalhas.loc['ALEMANHA']['OURO'])
print('\n---------------------------------------------------')

''' Exibir a quantidade de medalhas de OURO e de PRATA conquistadas por cada pais  '''
print('\n6 - Medalhas de OURO e PRATA de cada pais')
print(dfMedalhas[['OURO','PRATA']])
print('\n---------------------------------------------------')

''' Exibir a quantidade de medalhas de OURO e de PRATA conquistadas pelos 3 primeiros 
colocados  '''
print('\n7 - Medalhas de OURO e PRATA dos 3 primeiros colocados')
print(dfMedalhas.iloc[0:3][['OURO','PRATA']])
print('\n---------------------------------------------------')

''' Exibir o total de medalhas de cada tipo (até o momento) '''
print('\n8 - Total de medalhas de cada tipo')
print(dfMedalhas.sum())
print('\n---------------------------------------------------')

''' Exibir o total de medalhas conquistadas pelos 10 paises até o momento  '''
print('\n9 - Total de medalhas até o momento' )
print(dfMedalhas.sum().sum())

''' Por um recurso, a ITALIA conquistou mais uma medalha de ouro. A srAcerto abaixo, 
contem a quantidade correta de medalhas conquistadas pela ITALIA '''
srAcerto = pd.Series([2,1,1],index=['OURO', 'PRATA' ,'BRONZE'])

print('\n---------------------------------------------------')
''' Atualizar dfMedalhas com srAcerto e exibir '''
print('\n10 - dfMedalhas com a quantidade correta de medalhas conquistadas pela ITALIA ')
dfMedalhas.loc['ITALIA']=srAcerto
print(dfMedalhas)
print('\n---------------------------------------------------')

''' Incluir a coluna TOTAL com a quantidade de medalhas conquistadas por cada PAIS 
(até o momento)  '''
print('\n11 - dfMedalhas com a coluna TOTAL')
dfMedalhas['TOTAL']=dfMedalhas.sum(axis=1)
print(dfMedalhas)
print('\n---------------------------------------------------')

''' Usando a Series srCont incluir, no dfMedalhas, a coluna CONT com o continente 
de cada PAIS '''
print('\n12 - dfMedalhas com a coluna CONT')
dfMedalhas['CONT']=srCont
print(dfMedalhas)
print('\n---------------------------------------------------')

''' Exibir quantos paises em cada continente conquistaram medalhas (tabela de frequencia) '''
print('\n13 - Quantidade de paises por continente com medalhas.' )
print(dfMedalhas['CONT'].value_counts())
print('\n---------------------------------------------------')

''' Exibir o nome de um país, com a menor quantidade total de medalhas, mesmo se há empate  '''
print('\n14 - Um pais com a menor quantidade total de medalhas?')
print(dfMedalhas['TOTAL'].idxmin())
print('\n---------------------------------------------------')

''' Exibir o nome de um país, com a maior quantidade de medalhas de OURO, mesmo se há 
empate  '''
print('\n15 - Um pais com a maior quantidade de medalhas de OURO?')
print(dfMedalhas['TOTAL'].idxmax())
print('\n---------------------------------------------------')

'''  Com a atualização de medalhas da ITALIA, (item 9) o DataFrame precisa ser reordenado. 
Organize de tal forma a ficar como todo quadro geral de medalhas, isto é, 
ordem decrescente da quantidade de medalhas de OURO/PRATA/BRONZE. Para mesma quantidade de 
um tipo, o desempate é na quantidade de medalhas do tipo seguinte. Atualize o dataframe 
e depois exiba-o.'''
print('\n16- dfMedalhas atualizado e ordenado como quadro de medalhas')
dfMedalhas.sort_values(by=['OURO','PRATA','BRONZE'],axis=0,ascending=False,inplace=True)
print(dfMedalhas)
print('\n---------------------------------------------------')
print('\n---------------------------------------------------')






