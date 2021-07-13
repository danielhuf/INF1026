import pandas as pd
import matplotlib.pyplot as plt

sIdade=pd.Series([40,45,57,37,21,19,30,20,20,40],index=['a','b','c','d','e','f','g','h','i','j'])
sNota=pd.Series([10,3,6,6,10,9,7,8,5,7],index=['a','b','c','d','e','f','g','h','i','j'])
sSexo=pd.Series(['f','m','f','m','m','f','m','m','f','f'],index=['a','b','c','d','e','f','g','h','i','j'])

# Associa Faixas e Categorias ao valores sIdade
cFxI =pd.cut(sIdade, bins=3,labels=['inf','med','sup'])
cCatI=pd.cut(sIdade, bins=[0,21,50,sIdade.max()],labels=['jovem','adulto','idoso'])

# Usando as Categorias/Faixas para agrupar sIdade
gIdFx=sIdade.groupby(by=cFxI)
gIdCat=sIdade.groupby(by=cCatI)

# Mostrando resumos por grupos de Categorias e Faixas 
print('\n-----------------------------------------------------\n')
print("Resumos por categoria de Idade")
print(gIdCat.agg(['mean','median','min','max']))
print('\n-----------------------------------------------------\n')
print("Resumos por faixa de Idade")
print(gIdFx.agg(['mean','median','min','max']))
print('\n-----------------------------------------------------\n')

# Associa Faixas e Categorias ao valores de sNota
cFxN =pd.cut(sNota, bins=3,labels=['inf','med','sup'])
cCatN=pd.cut(sNota, bins=[0,6,8,sIdade.max()],labels=['bx','med','ot'])

# Usando as Categorias/Faixas para agrupar sNotas
gNtFx=sNota.groupby(by=cFxI)
gNtCat=sNota.groupby(by=cCatI)

print("Resumos for categoria de Nota")
print(gNtCat.agg(['mean','median','min','max']))
print('\n-----------------------------------------------------\n')

# Mostrando resumos por grupos de Categorias e Faixas 
print("Resumos por faixa de Nota")
print(gNtFx.agg(['mean','median','min','max']))
print('\n-----------------------------------------------------\n')

# Mostrando numericamente e graficamente o percentual de pessoas em cada grupo
s=gNtCat.agg('count')/sNota.size*100
print('Percentual de pessoas em cada grupo')
print(s)
print('\n-----------------------------------------------------\n')

# Mostrando graficamente o percentual de pessoas em cada grupo
gNtCat.agg('count').plot.pie(autopct='%.1f')
plt.show()

# Agrupando as notas por Categoria de Idade/Sexo 
gIdSx=sNota.groupby(by=[sSexo,cCatI])

# Mostrando resumos por Categoria de Idade/Sexo 
print("Resumos de Notas por Categoria de Sexo/Idade")
print(gIdSx.agg(['mean','median','min','max']))
print('\n-----------------------------------------------------\n')

#Grafico  %  de cada grupo sexo/idade
gIdSx.agg('count').plot.pie(autopct='%.1f')
plt.show()

#Tabela  %  de cada grupo sexo/idade
s=gIdSx.agg('count')/sNota.size*100
print('Percentual de pessoas em cada grupo')
print(s)
