import pandas as pd
import matplotlib.pyplot as plt

#1
dfPrHigMerc= pd.read_excel('PrecosProdutosMercadosGeral.xlsx',index_col=0,
                          sheet_name='ProdHigieneMerc', header=0, decimal='.')
print(dfPrHigMerc)
print('-------------------------------------------------------------')

#2
dfPrLimMerc= pd.read_excel('PrecosProdutosMercadosGeral.xlsx',index_col=0,
                          sheet_name='ProdLimpezaMerc', header=0, decimal='.')
print(dfPrLimMerc)
print('-------------------------------------------------------------')

#3 EXIBIR A TRANSPOSTA
print(dfPrHigMerc.T)
print('-------------------------------------------------------------')

#4
print(dfPrHigMerc.columns.values)
print(dfPrHigMerc.index.values)
print(dfPrHigMerc.shape)
print(dfPrHigMerc.index.name)
print(dfPrHigMerc.columns.name)
print('-------------------------------------------------------------')

#5
print(dfPrHigMerc['Descontão'])
print(dfPrHigMerc[['Descontão','SuperPrice']])
print(dfPrHigMerc.loc['Sabonete'])
print(dfPrHigMerc.loc['Creme Dental']['Pop'])
print(dfPrHigMerc.loc[['Repelente','Protetor FPS >= 30']][['Pop','Descontão']])
print(dfPrHigMerc.columns.name)
print('-------------------------------------------------------------')

#6
dfPrHigMerc['BigBaixo']=dfPrHigMerc['SuperPrice']-1
print(dfPrHigMerc)
print('-------------------------------------------------------------')

#7
dfPrHigMerc.loc['Desinfetante']=dfPrLimMerc.loc['Desinfetante']
print(dfPrHigMerc)
print('-------------------------------------------------------------')

#8
dfCestaBasica= pd.read_excel('PrecosProdutosMercadosGeral.xlsx',index_col=0,
                          sheet_name='Produtos', header=0, decimal='.')
dfPrHigMerc['Quantidade']=dfCestaBasica['Quantidade']
dfPrLimMerc['Quantidade']=dfCestaBasica['Quantidade']
print(dfPrHigMerc)
print(dfPrLimMerc)
print('-------------------------------------------------------------')

#9
print(dfPrHigMerc.drop('Quantidade',axis=1).mean(axis=1))
print('-------------------------------------------------------------')
print(dfPrHigMerc.drop('Quantidade',axis=1).sum())
print('-------------------------------------------------------------')
s=dfPrHigMerc.drop('Quantidade',axis=1).T*(list(dfPrHigMerc['Quantidade'].values))
print(s.T.sum())
#Há maneira mais fácil de fazer isso?
#MANEIRA DA PROFESSORA
dfSem=dfPrHigMerc.drop('Quantidade',axis=1)
s=dfPrHigMerc['Quantidade'].T
dfTot=dfSem.mul(s,axis='index')
print(dfTot.sum())
print('-------------------------------------------------------------')
print(dfPrHigMerc.drop('Quantidade',axis=1).max())
print('-------------------------------------------------------------')
print(dfPrHigMerc.drop('Quantidade',axis=1).idxmax())
print('-------------------------------------------------------------')
print(dfPrHigMerc.drop('Quantidade',axis=1).idxmin(axis=1))
print('-------------------------------------------------------------')
print(dfPrHigMerc.drop('Quantidade',axis=1).idxmin(axis=1).value_counts())
#o VALUE COUNTS NÃO PEGOU O MERCADO DE VALOR 0 
print('-------------------------------------------------------------')




