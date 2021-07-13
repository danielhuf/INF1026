import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

dfCorredores = pd.read_excel('corredores.xlsx',index_col=0,header =0,decimal ='.') 
dfCorredores =pd.DataFrame(dfCorredores)


print('\n1- DataFrame dfCorredores')
print(dfCorredores)
print('----------------------------------------------------')

print('\n2-index renomeado para num')
dfCorredores.index.name='num'  #ou rename_axis
print(dfCorredores)
print('----------------------------------------------------')

print('\n3- Nome do(s) vencedor(es) da corrida e melhor tempo')
f=dfCorredores['corrida']==dfCorredores['corrida'].min()
print(dfCorredores.loc[f]['nome'].values)
print(dfCorredores['corrida'].min())
print('----------------------------------------------------')

print('\n4- Nomes dos corredores com melhor desempenho na corrida do que em algum treino')
f1=(dfCorredores['corrida']<dfCorredores['treino1']) | (dfCorredores['corrida']<dfCorredores['treino2']) | (dfCorredores['corrida']<dfCorredores['treino3'])
print(dfCorredores.loc[f1]['nome'].values)
print('----------------------------------------------------')

print('\n5- Nomes dos corredores com melhor desempenho na corrida do que no melhor treino e respectivos tempos')
sMenor=dfCorredores[['treino1','treino2','treino3']].min(axis=1)
f=dfCorredores['corrida']<sMenor
d=dfCorredores.loc[f][['nome','corrida']]
d['melhor treino']=sMenor
print(d)
print('----------------------------------------------------')

print('\n6-Dataframe so com os que tiveram desempenho na corrida pior ou igual a media dos treinos')
mediaTreinos=dfCorredores[['treino1','treino2','treino3']].mean(axis=1)
f2=dfCorredores['corrida']>=mediaTreinos
print(dfCorredores.loc[f2])
print('----------------------------------------------------')


print('\n7-Nome dos corredores que tiveram a maior diferenca absoluta entre o seu melhor treino e a corrida')
print('para mais ou para menos')
sDif=abs(sMenor-dfCorredores['corrida'])
maior=sDif.max()
print(dfCorredores.loc[maior==sDif]['nome'].values)
print('----------------------------------------------------')

print(('\n8-df dos corredores com tempo decrescente nos treinos'))
f5=dfCorredores.query('treino1>treino2>treino3')

print(('\n9-df dos corredores com melhor tempo de corrida que "KAKA"'))
tempo=int(dfCorredores.loc[dfCorredores['nome']=='KAKA']['corrida'].values)
#tbm poderia fazer filtro do kaka e dar iloc[0]['corrida] para pegar o número
f=dfCorredores['corrida']<tempo
print(dfCorredores.loc[f])
print('----------------------------------------------------')

print(('\n10-df dos corredores AMADORES com tempo melhor que a média dos PROFISSIONAIS'))
amadores=dfCorredores.loc[dfCorredores['categoria']=='amador']
profissionais=dfCorredores.loc[dfCorredores['categoria']=='profissional']
media=profissionais['corrida'].mean()
f=amadores['corrida']<media
print(amadores.loc[f])
#Ou poderia printar amadores.query('corrida<'+str(media))
print('----------------------------------------------------')