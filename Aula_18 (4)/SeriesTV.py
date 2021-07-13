import pandas as pd
import matplotlib.pyplot as plt

#a)
sTVS= pd.read_excel('PrecoTV.xlsx',index_col=0,header=None,squeeze=True)
print(sTVS.count())
print(sTVS.size-sTVS.count())
print(sTVS.dropna().values)
print('\n-----------------------------\n')

#b)
sTVS.dropna(inplace=True)
print(sTVS)
print('\n-----------------------------\n')

#c)
print(sTVS.max())
s=sTVS.loc[sTVS==sTVS.max()]
print(s.count())
print('\n-----------------------------\n')

#d)
print(sTVS.loc[sTVS==sTVS.min()])
print('\n-----------------------------\n')

#e)
sFaixaDePreco=pd.cut(sTVS,bins=[0.0,1500.0,2500.0,3500.0,sTVS.max()])
print(sFaixaDePreco)
print('\n-----------------------------\n')

#f)
sFreq=sFaixaDePreco.value_counts()
print(sFreq)
print('\n-----------------------------\n')

#h)
sJG=sTVS.index.str.match('JG')
sTVS.loc[sJG]=sTVS.loc[sJG]*1.1
print(sTVS)
print('\n-----------------------------\n')

#i)
sCopia=sTVS.copy()
print(sCopia)
fMenorMediana=sCopia<sCopia.median()
sCopia.drop(sCopia.index[fMenorMediana],inplace=True)
print(sCopia)
fMenorMedia=sCopia<sCopia.mean()
print(sCopia.loc[fMenorMedia].index)
print('\n-----------------------------\n')

#j)
def detTamTela(x):
    return int(x[2:4])
gTela=sTVS.groupby(by=detTamTela)
print(gTela.groups)
print(gTela.agg(['count','min','max','mean']))
print(gTela.indices)
tamTela=int(input('Tamanho de tela desejado? '))
while tamTela not in gTela.indices:
    print('Não possuimos este tamanho. Escolha outro tamanho. ')
    tamTela=int(input('Tamanho de tela desejado? '))
sTelaDesejada=gTela.get_group(tamTela)
print(sTelaDesejada.sort_values())
fMenorMedia=sTelaDesejada<sTelaDesejada.mean()
print(sTelaDesejada.loc[fMenorMedia].sort_values())
print('\n-----------------------------\n')


