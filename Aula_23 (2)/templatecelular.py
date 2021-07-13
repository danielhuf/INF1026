"""    EX: CELULAR     """

'''
No arquivo CelularNoBoaCompra.xlsx ha´ 3 planilhas com dados sobre um mesmo grupo de celulares.
Na planilha caracteristicas estao caracteristicas dos aparelhos.
Na planilha precos estao os precos dos aparelhos em alguns sites.
Na planilha avaliacao estao as notas dadas pelos usuarios aos aparelhos nos quesitos tela, camera e desempenho.
'''

import pandas as pd
import matplotlib.pyplot as plt


'''
1- Crie o dataframe dfCaracCel a partir da planilha caracteristicas do arquivo CelularGeral.xlsx,
considerando o nome do celular como indice. A primeira linha do arquivo contem o nome das colunas
'''
dfCaracCel=pd.read_excel('CelularGeral.xlsx',sheet_name='caracteristicas',header=0,index_col=0,decimal=',')
print('\n1-O dfCaracCel')
print(dfCaracCel)
print('------------------------------------------------------------\n')

print('\n2-Exiba as informacoes do dfCelular')
print(dfCaracCel.info())
print('------------------------------------------------------------\n')

print('\n3-Exiba a coluna fabricante')
print(dfCaracCel['fabricante'].values)
print('------------------------------------------------------------\n')

print('\n4.A-Renomeie as colunas sistema operacional(SO) e tamanho tela (tela). Exiba')
dfCaracCel.rename(columns={"sistema operacional": "SO", "tamanho tela": "tela"},inplace=True)
print(dfCaracCel)
print('------------------------------------------------------------\n')

print('\n4.B-Renomeie as colunas bateria ligado (bateria) e bateria repouso (autonomia). Exiba')
dfCaracCel.rename(columns={"bateria ligado": "bateria", "bateria repouso": "autonomia"},inplace=True)
print(dfCaracCel)
print('------------------------------------------------------------\n')

print('\n5-Crie e exiba um DF (dfCel1) so com as colunas tela,SO,fabricante')
dfCel1=dfCaracCel[['tela','SO','fabricante']]
print(dfCel1)
print('------------------------------------------------------------\n')

print('\n6-Alterar ordem das colunas: SO,fabricante,tela,camera,bateria,autonomia')
dfCaracCel=dfCaracCel[['SO','fabricante','tela','camera','bateria','autonomia']]
print(dfCaracCel)
print('------------------------------------------------------------\n')

print('\n7-Exibir ordenado descrescentemente por tela, fabricante')
dfCaracCel.sort_values(by=['tela','fabricante'],ascending=False,inplace=True)
print(dfCaracCel)
print('------------------------------------------------------------\n')

print('\n8-Tratando NaN nas  colunas bateria e autonomia')
print('\nNas colunas bateria e autonomia NaN deve ser substituido pelo valor minimo na coluna')
dfCaracCel.fillna(dfCaracCel.min(),inplace=True)
print(dfCaracCel)
print('------------------------------------------------------------\n')

'''
9- Crie o dataframe dfPrecosCel a partir da planilha precos do arquivo CelularGeral.xlsx,
considerando o nome do celular como indice. A primeira linha do arquivo contem o nome das colunas.
Exiba
'''
dfPrecosCel=pd.read_excel('CelularGeral.xlsx',sheet_name='precos',header=0,index_col=0)
print('\n9-O dfPrecosCel')
print(dfPrecosCel)
print('------------------------------------------------------------\n')

print('\n10-Exiba as informacoes do dfPrecosCel')
print(dfPrecosCel.info())
print('------------------------------------------------------------\n')

print('\n11-Tratando NaN: colunas com preco NaN devem ser descartadas. Exiba')
dfPrecosCel.dropna(axis=1,inplace=True)
print(dfPrecosCel)
print('------------------------------------------------------------\n')

'''
12- Crie o dataframe dfNotasCel a partir da planilha avaliacao do arquivo CelularGeral.xlsx,
considerando o nome do celular como indice. A primeira linha do arquivo contem o nome das colunas.Exiba.
'''
dfNotasCel=pd.read_excel('CelularGeral.xlsx',sheet_name='avaliacao',header=0,index_col=0,decimal='.')
print('\n12-O dfNotasCel')
print(dfNotasCel)
print('------------------------------------------------------------\n')

print('\n13-Exiba as informacoes do dfNotasCel')
print(dfNotasCel.info())
print('------------------------------------------------------------\n')

print('\n14-Renomeie Nota Tela (NTT), Nota Camera(NCC), Nota Desempenho (NTD)')
dfNotasCel.rename(columns={"Nota Tela": "NTT", "Nota Camera": "NCC", "Nota Desempenho": "NTD"},inplace=True)
print(dfNotasCel)
print('------------------------------------------------------------\n')

print('\n15- Concatene os 3 dataframes, criando o dfCelular. Exiba')
dfCelular=pd.concat([dfCaracCel,dfPrecosCel,dfNotasCel],axis=1)
print(dfCelular)
print('------------------------------------------------------------\n')

print('\n16- Incluindo Preco Medio (PrecoMed). Exiba' )
med=dfPrecosCel.mean(axis=1)
dfCelular['PrecoMed']=med
print(dfCelular)
print('------------------------------------------------------------\n')

print('\n17- Incluindo Nota Global(NTG) = 1XTela+1XCamera+2XDesempenho. Exiba' )
nota=dfNotasCel['NTT']*1+dfNotasCel['NCC']*1+dfNotasCel['NTD']*2
dfCelular['NTG']=nota
print(dfCelular)
print('------------------------------------------------------------\n')

print('\n----------------------------------------------------------------')
print('\n18-Graficamente (barras juntas) precos no CasaTecno e no TemTudo' )
dfPrecosCel.plot.scatter(x='CasaTecno',y='TemTudo',legend=True)
plt.show()
print('\n----------------------------------------------------------------')
'''
USE dataframe.plot.scatter(x='NomeDaColuna1', y='NomeDaColuna2') 
'''
print('\n19- Graficamente: PrecoMedio X Nota Global')
dfCelular.plot.scatter(x='PrecoMed',y='NTG',legend=True)
plt.show()










