#Nome completo: Daniel Stulberg Huf
#Matrí­cula PUC-Rio: 1920468
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, 
#sem consultas a outros alunos, professores ou qualquer outra pessoa.

"""
O arquivo Excel RacasCaninas.xlsx possui dados de raças caninas . Há quatro planilhas:
•	dadosFinan: com o preço mínimo (PRMIN), o preço máximo (PRMAX) para comprar um animal 
da raça e o país de origem (ORIGEM ) da raça.
•	dadosBio: com os dados biométricos médios dos machos (ALTMACHO, PESOMACHO) e das 
fêmeas (ALTFEMEA, PESOFEMEA) da raça.
•	caracteristicas: com a posição no ranking de inteligência (RANKINTELIGENCIA) e uma nota entre 
1 e 6 para cada uma das seguintes características avaliadas: gosto por brincadeira (BRINCALHAO), 
amizade com cães, com estranhos e com outros animais (AMIZADE), proteção (PROTECAO), 
apego ao dono (APEGODONO), facilidade de treinamento (TREINAMENTO) e guarda (GUARDA).
•	categoria: com o nome da categoria (grupo) da raça de acordo com sua função, suas qualidades 
específicas, físicas e/ou comportamentais.
=>O DataFrame dfFinan já foi criado e se encontra no arquivo disponibilizado. O mesmo usou a 
planilha dadosFinan do arquivo, usando a primeira coluna (RACA) como índice e a primeira 
linha como nome das colunas.
=>O DataFrame dfBio já foi criado e se encontra no arquivo disponibilizado. O mesmo usou a 
planilha dadosBio do arquivo, usando a primeira coluna como índice (RACA) e a primeira 
linha como nome das colunas.
=>O DataFrame dfCarac já foi criado e se encontra no arquivo disponibilizado. O mesmo usou a 
planilha caracteristicas do arquivo, usando a primeira coluna como índice (RACA) e a primeira 
linha como nome das colunas.
=>A Series sCategoria já foi criada e se encontra no arquivo disponibilizado. A mesma usou a 
planilha categoria do arquivo, usando a primeira coluna como índice (RACA). 
"""
'''
ATENÇÃO: SUA SOLUÇÃO TEM QUE MANIPULAR AS ESTRUTURAS DA BIBLIOTECA PANDAS DENOMINADAS 
DATAFRAME OU SERIES E USAR OS MÉTODOS APRESENTADOS E TRABALHADOS NAS AULAS E NO MATERIAL 
DISPONIBILIZADO. NÃO É PERMITIDO TRANSFORMÁ-LAS EM OUTRAS ESTRUTURAS PARA OBTER A RESPOSTA 
PEDIDA.
'''

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

dfFinan = pd.read_excel('RacasCaninasSimplificada.xlsx',sheet_name='dadosFinan',index_col=0,header=0)
dfFinan = pd.DataFrame(dfFinan)
dfBio = pd.read_excel('RacasCaninasSimplificada.xlsx',sheet_name='dadosBio',index_col=0,header=0)
dfBio = pd.DataFrame(dfBio)
dfCarac = pd.read_excel('RacasCaninasSimplificada.xlsx',sheet_name='caracteristicas',index_col=0,header=0)
dfCarac = pd.DataFrame(dfCarac)
sCategoria = pd.read_excel('RacasCaninasSimplificada.xlsx',sheet_name='categoria',index_col=0,header=0,squeeze=True)
sCategoria = pd.Series(sCategoria)
''' Qualquer resposta que não condiz com o enunciado de algum item resulta em grau zero neste teste. '''

'''Parte I. Preparando e conhecendo as estruturas da biblioteca Pandas, criadas:'''
print('item 1: sCategoria-------------')
''' a.	Eliminar raças sem categoria: '''
sCategoria.dropna(inplace=True)
print(sCategoria)
print('-------------------------------------------------------')

''' Exibir a tabela de frequência de raças por categoria (quantidade de raças em cada categoria)'''
print('\n1.b.Tabela de frequencia de racas por categoria:')
print(sCategoria.value_counts())
print('-------------------------------------------------------')

print('\nitem 2: dfFinan -----------')
''' a.	Eliminar todas as raças cujo país de origem é desconhecido (está ausente).  '''
dfFinan.dropna(inplace=True)
print(dfFinan)
print('-------------------------------------------------------')

print('\n2.b Mostrar, por país de origem a quantidade de racas, preco min medio, preco max medio ',end='')
print('ordenado decrescentemente por quantidade, com um unico comando:')
print(dfFinan.reset_index().groupby('ORIGEM').agg({'RACA':'count','PRMIN':'mean','PRMAX':'mean'}).sort_values('RACA',ascending=False))
print('-------------------------------------------------------')

print('\n2.c. Mostrar, por país de origem o menor preco maximo e uma raca com este valor')
gPais=dfFinan.groupby('ORIGEM')
print(gPais['PRMAX'].agg(['min','idxmin']))
print('-------------------------------------------------------')

print('\n2.d. Uma das raças com a menor diferença entre o preço maximo e o minimo')
dfDif=dfFinan['PRMAX']-dfFinan['PRMIN']
print(dfDif.idxmin())
print('-------------------------------------------------------')

print('\nitem 3: dfBio ------------------')
''' a.	Eliminar todas as raças com qualquer valor ausente. '''
dfBio.dropna(inplace=True)
print(dfBio)
print('-------------------------------------------------------')

print('\n3.b.Racas cujas medidas (altura e peso médio) sao iguais no macho e na femea:')
print(list(dfBio.query('ALTMACHO==ALTFEMEA and PESOMACHO==PESOFEMEA').index.values))
print('-------------------------------------------------------')

print('\n3.c.Valores mais frequentes das medidas altura e peso médio do macho e da femea')
print(dfBio.mode())
print('-------------------------------------------------------')

''' Lembre-se: qualquer resposta que não condiz com o enunciado de algum item resulta em grau zero neste teste. '''
print('\nitem 4: dfCarac ----------')
''' a.	Preencher valores ausentes em qualquer uma das características avaliadas com o valor 1. '''
dfCarac.fillna(1,inplace=True)
print(dfCarac)
print('-------------------------------------------------------')

''' b.	Mostrar graficamente (scatter) a relação entre a posição no ranking de inteligência 
(RANKINTELIGENCIA) e a característica gosto por brincadeira (BRINCALHAO).'''
print('\n4.b.Graficamente (scatter) a relacao entre posicao no rank inteligencia  e gosto ', \
      'por brincadeira:')
dfCarac.plot.scatter(x='RANKINTELIGENCIA',y='BRINCALHAO',figsize=(10,4),title='Relação entre a posição no ranking de inteligência e a característica gosto por brincadeira')
plt.show()
print('-------------------------------------------------------')

''' c. Considerando as caracteristicas, exceto a RANKINTELIGENCIA responda: '''
print('\n4.c.i. Para cada raça, uma das caracteristica com menor nota ')
print(dfCarac.drop('RANKINTELIGENCIA',axis=1).idxmin(axis=1))
print('-------------------------------------------------------')

print('\n4.c.ii. Media das notas das caracteristicas (nota media), por raça')
print(dfCarac.drop('RANKINTELIGENCIA',axis=1).mean(axis=1))
print('-------------------------------------------------------')

print('\n4.c.iii.Raca ou racas com a menor media das caracteristicas')
dfMedias=dfCarac.drop('RANKINTELIGENCIA',axis=1).mean(axis=1)
print(list(dfMedias.loc[dfMedias==dfMedias.min()].index))
print('-------------------------------------------------------')

'''Parte II. Analisando os dados das raças em conjunto:'''
print('\nitem 5. ------------------')
print('\n5. Categoria e caracteristicas das 10 primeiras racas no rank inteligencia, :'\
      ' ordenadas pela posição no ranking.')
dfCaracCat=pd.concat([dfCarac,sCategoria],axis=1)
print(dfCaracCat.sort_values(by='RANKINTELIGENCIA').head(10))
print('-------------------------------------------------------')

print('\nitem 6. ------------------')
print('\n6. Tabela de frequencia da relacao entre categoria e caracteristicas: protecao e apego ao dono:')
print(pd.crosstab(dfCaracCat['CATEGORIA'],[dfCaracCat['PROTECAO'],dfCaracCat['APEGODONO']]))
print('-------------------------------------------------------')

'''Parte III.  Juntando os dados das raças:'''
print('\nitem 7. ------------------')
''' Criar o dfRacas juntando dfFinan, dfBio, dfCarac e sCategoria do modo mais apropriado.  Raças que 
não estejam em todas as estruturas devem ser eliminadas. '''
dfRacas=pd.concat([dfFinan,dfBio,dfCarac,sCategoria],axis=1)
dfRacas.dropna(inplace=True)

print('\n7. DataFrame dfRacas - 3 ultimas linhas:')
print(dfRacas.tail(3))
print('-------------------------------------------------------')

''' Lembre-se: qualquer resposta que não condiz com o enunciado de algum item resulta em grau zero neste teste. '''
'''No dfRacas:'''
print('\nitem 8. ------------------')
''' a.	classificar as raças considerando o preço mínimo nas seguintes faixas de preços (usar 
obrigatoriamente cut):
    •	até 2500 (inclusive) - NORMAL
    •	de 2500 (exclusive) a 4000 (inclusive) - ELEVADO
    •	acima de 4000 – CARO   '''
cFaixaP=pd.cut(dfRacas['PRMIN'],bins=[0,2500,4000,dfRacas['PRMIN'].max()],labels=['NORMAL','ELEVADO','CARO'],include_lowest=True)
print(cFaixaP)
print('-------------------------------------------------------')

print('\n8.b.Nota media da caracteristica apego ao dono (APEGODONO) por faixa de preco:')
gFaixas=dfRacas.groupby(cFaixaP)
print(gFaixas['APEGODONO'].agg('mean'))
print('-------------------------------------------------------')

''' c.	Considerando apenas as seguintes características:  APEGODONO, AMIZADE e BRINCALHAO 
inclua uma nova coluna para a nota da sociabilidade da raça, denominada SOCIAL, com um 
dos seguintes valores:
    •	AMOROSO – se essas 3 características têm nota >= 4,
    •	SOCIAVEL – se apenas a característica AMIZADE e a BRINCALHAO tem nota >= 4,
    •	INDETERMINADO – nos demais casos.  '''
    
def detSocial(dog):
    if dog['APEGODONO']>=4 and dog['AMIZADE']>=4 and dog['BRINCALHAO']>=4:
        return 'AMOROSO'
    elif dog['AMIZADE']>=4 and dog['BRINCALHAO']>=4:
        return 'SOCIAVEL'
    else:
        return 'INDETERMINADO'

dfRacas['SOCIAL']=dfRacas.apply(detSocial,axis=1) 

print('\n8.c.Tabela de frequencia das faixas de precos X sociabilidade:')
print(pd.crosstab(cFaixaP,dfRacas['SOCIAL']))
print('-------------------------------------------------------')

