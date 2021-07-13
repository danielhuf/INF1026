import pandas as pd
import matplotlib.pyplot as plt
'''
1.	Construa o DataFrame  dfProdHigMerc onde em cada linha estão os dados de um produto de Higiene, indexados pelo seu nome.
'''
dfPrHigMerc= pd.read_excel('PrecosProdutosMercadosGeral.xlsx',index_col=0,
                          sheet_name='ProdHigieneMerc', header=0, decimal='.')
dfPrHigMerc.columns.name='Mercado'

print("\n-------------------------------------------------")
print("1-dfProdHigMer visualizado MercadoxProduto")
print(dfPrHigMerc.T)
print("-------------------------------------------------\n")
###################################################################
#
#   2- Visualizando Graficamente
#
#####################################################################
#
#2.a-Visualizando o df - Observe quem é o eixo x
#
print("\n-------------------------------------------------")
print("2.a-Visualizando o df - Observe quem é o eixo x")
dfPrHigMerc.plot.bar()
plt.show()
print("-------------------------------------------------\n")

#
#2.b-Visualizando cada coluna em  um gráfico
#
print("\n-------------------------------------------------")
print("2.b-Visualizando o df - cada coluna em  um gráfico")
dfPrHigMerc.plot.bar(subplots=True,figsize=(10,10))
plt.show()
print("-------------------------------------------------\n")

#
#
# Visualizando tendências
#
print("\n-------------------------------------------------")
print("2.c-Visualizando tendências/influências/relações")

dfPrHigMerc.plot.scatter(x='Pop',y='SuperPrice',legend=True)
plt.show()
print("-------------------------------------------------\n")

###################################################################
#
#   3-Excluindo e Tratando Ausentes
#
#####################################################################
## DESCARTANDO/ PREENCHENDO

#Qual o resultado das instruções a seguir?
# Executes-as uma a uma
dfC=dfPrHigMerc.copy()
print(dfC)

#Excluindo  colunas
print("\n-------------------------------------------------")
print("3.a-Excluindo  colunas")
dfC.drop(['Descontão','SuperPrice'],axis=1,inplace=True)
print(dfC)
print("-------------------------------------------------\n")

#Incluindo novas linhas
dfC.loc['aaa']=[10,10,10]
dfC.loc['bbb']=[None,10,20]

#incluindo nova coluna vazia
dfC['Ex']=pd.Series(index=dfC.index)

#dfC após inclusões
print("\n-------------------------------------------------")
print("3.b-dfC após inclusões de linhas e colunas")
print(dfC)
print("-------------------------------------------------\n")

#Excluindo  Ausentes
print("\n-------------------------------------------------")
print("3.c-Excluindo Ausentes: dropna()==>Como todas linhas/colunas tem NaN\n==>df resultante fica vazio\n")
print(dfC.dropna())
print("\n\ndfC continua com valores\n")
print(dfC)
print("-------------------------------------------------\n")

#   dfC.dropna(axis=0)  ou dfC.dropna(axis='index')
#  Especifica o eixo ao longo do qual os elementos serão eliminados. 
#  Dropna por axis=0 (que é o mesmo que axis='index') significa que vai
#  eliminar todas as linhas que tenham NaN. 
#  Como todas linhas tem NaN,   o df resultante é vazio

print("\n-------------------------------------------------")
print("3.d-Excluindo Linhas com valores ausentes: dropna(axis='index')\n==>Como todas linhas tem NaN, df resultante é vazio\n")
print(dfC.dropna(axis='index'))
print("-------------------------------------------------\n")

#   dfC.dropna(axis=1)  ou dfC.dropna(axis='columns')
#  Especifica o eixo ao longo do qual os elementos serão eliminados. 
#  Dropna por axis=1 (ou axis='columns') significa que vai
#  eliminar todas as colunas que tenham NaN. 
#  Como há colunas sem NaN,  o df resultante não é vazio

print("\n-------------------------------------------------")
print("3.d-Excluindo colunas com valores ausentes: dropna(axis=1)\n==> Como há colunas sem NaN, mostra o que sobrou\n")
print(dfC.dropna(axis='columns'))
print("\n-------------------------------------------------")

#Incluindo uma linha com todos os valores ausentes
dfC.loc['ccc']=None

#   Agora dfC tem:
#       a linha ccc (última) toda com NaN e 
#       a última coluna(Ex) tb toda com NaN
# 
print("\n=================================================================")
print("\n ENTENDENDO o how='all': \nsó elimina se TODOS no eixo são NaN")
print("=================================================================\n")
print(dfC)
print("\n-------------------------------------------------")
print("3.e-Excluindo linhas com todos valores ausentes: dropna(how='all')")
print("==>Sem última linha")
dfC.dropna(how='all',inplace=True)
print(dfC)
print("\n-------------------------------------------------")
print("\n-------------------------------------------------")
print("3.f-Excluindo colunas com todos valores ausentes: dropna(how='all',axis=1)")
print("==>Sem última coluna")
dfC.dropna(how='all',axis=1,inplace=True)
print(dfC)
print("\n-------------------------------------------------")

print("\n=================================================================")
print("\n ENTENDENDO o how='any': \nelimina se há UM elemento NaN no eixo")
print("=================================================================\n")

print("\n-------------------------------------------------")
print("3.g-Excluindo colunas com pelo menos um valor ausente: dropna(how='any',axis=1)")
print("==>Sai KiBarato e Mercadão\n")
print(dfC.dropna(how='any',axis='columns'))

print("\n-------------------------------------------------")
print(dfC)
print("\n3.g-Excluindo linhas com pelo menos um valor ausente: dropna(how='any')")
print("==>Sai bbb\n")

print(dfC.dropna(how='any'))

print("\n\nDropna: dfC.dropna(axis=0,how='any') sai linha 996,997\n",dfC.dropna(axis='index',how='any'))

###################################################################
#
#   4- Tratando Ausentes por coluna
#
#####################################################################

print("\n\nTrocando NaN por valor dependendo da coluna  Ex->-1, Pop->mínimo\n",dfC.fillna({'P1':0,'P2':-1,'P3':-2},inplace=True))