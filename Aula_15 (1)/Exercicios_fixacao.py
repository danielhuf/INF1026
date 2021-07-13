import pandas as pd
import matplotlib.pyplot as plt

#As listas abaixo armazenam o nome e o número de  disciplinas cursadas pelos alunos do 3º período
#com os 6 melhores CRs de 5 Engenharias: 

lAlunos = ["AL0","AL10","AL16","AL19","AL23","AL2","AL3","AL4","AL8","AL12","AL13","AL14","AL15","AL17","AL18","AL20","AL24","AL25","AL1","AL5","AL6","AL7","AL9","AL21","AL22","AL26","AL27","AL29","AL11","AL28"]  
lNumDisc=[7,4,None,4,9,9,6,7,5,7,7,5,8,8,7,7,6,5,7,10,9,7,4,9,4,7,9,6,9,5]

#Organização destas listas:
#     1º ao  6º - Civil 
#     7º ao 12º - Mecânica
#    13º ao 18º - Química
#    19º ao 24º - Produção
#    25º ao 30º - Computação
lEng=['Civil']*6+['Mecânica']*6+['Química']*6+['Produção']*6+['Computação']*6   

#   Utilizar as listas para  criar a Series sQtA
#       índice: lAlunos
sQtA=pd.Series(lNumDisc,index=lAlunos)
sQtA=sQtA.apply('{:.0f}'.format)
sQtA=sQtA.sort_index()
print(sQtA)
print('--------------------')

#   Mostrar 20ºs elementos
print(sQtA.loc['AL20':'AL29'])
print('--------------------')

#   Observe: Todos os alunos têm valor?
#            O que o valor None provocou?
#     

# Mostre os valores, índices e tamanho da sQtA
print('***valores, índices e tamanho***')
print(sQtA.values)
print('--------------------')
print(sQtA.index)
print('--------------------')
print(sQtA.size)
print('--------------------')

# Mostrar 3º elemento
print("\n***3º elemento***")

# Mostrar o índice e o valor do 3º elemento
print("\n***o índice e o valor do 3º elemento***")
print(sQtA.index[2])
print(sQtA.iloc[2])
print('--------------------')

# Mostrar os 3 primeiros elementos
print("\n***3 primeiros elementos***")
print(sQtA.head(3))
print('--------------------')

# Mostrar o 1º e o 3º elementos
print("\n***1º e o 3º elementos***")
print(sQtA.iloc[[0,2]])
print('--------------------')

# Mostrar a quantidade de disciplinas do aluno AL16
print("\n***qt disc do  AL16***")
print(sQtA.loc['AL16'])
print('--------------------')

#  Mostrar a qt de disc  dos alunos A16,Al4 e AL12
print("\n***qt de disc dos alunos A16,Al4 e AL12***")
print(sQtA.loc[['AL16','AL14','AL12']])
print('--------------------')

# O que acontece se selecionar um valor de índice inexistente?

# Altere a quantidade de disciplinas do AL16 para 6
sQtA.loc['AL16']=6
print(sQtA)
print('--------------------')

# Construa as series:
#    sAlTur: índice lEng e valores: lAlunos
sAlTur=pd.Series(lAlunos,index=lEng)
print(sAlTur)
print('--------------------')

#    sQtTur: índice LEng e valores: lNumDisc
sQtTur=pd.Series(lNumDisc,index=lEng)
sQtTur=sQtTur.apply('{:.0f}'.format)
print(sQtTur)
print('--------------------')

#    sTurAl:índice lAl e valores: lTur
sTurAl=pd.Series(lEng,index=lAlunos)
print(sTurAl)
print('--------------------')

# Quais os alunos de 'Química'?
print(sAlTur.loc['Química'].values)
print('--------------------')

# Qual o curso do aluno AL16?
print(sTurAl.loc['AL16'])
print('--------------------')

# Inclua um novo aluno da Computação em sTurAl
sTurAl.loc['AL30']='Computação'


# Inclua em sTurAl os 3 alunos seguintes: 
sTurAl["AA1"]=None 
sTurAl["AA2"]=None 
sTurAl["AA3"]=None 

# exiba sTurAl e mostre a quantidade de elementos
print(sTurAl)
print('--------------------')
print(sTurAl.size)
print('--------------------')

# exiba sTurAl ordenada pelo index
print(sTurAl.sort_index())
print('--------------------')

# exiba sTurAl ordenada pelo values
print(sTurAl.sort_values())
print('--------------------')

# elimine os valores ausentes de sTurAl
sTurAl.dropna(inplace=True)
print(sTurAl)
print('--------------------')

#============================================
#       Responder as seguintes perguntas:
#============================================
# 
#   Qual o total de disciplinas cursadas?
print(sTurAl.unique().size)
print('--------------------')

# Qual a maior quantidade de disciplinas de um aluno? De quem? De qual Curso?
lAlunos = ["AL0","AL10","AL16","AL19","AL23","AL2","AL3","AL4","AL8","AL12","AL13","AL14","AL15","AL17","AL18","AL20","AL24","AL25","AL1","AL5","AL6","AL7","AL9","AL21","AL22","AL26","AL27","AL29","AL11","AL28"]  
lNumDisc=[7,4,None,4,9,9,6,7,5,7,7,5,8,8,7,7,6,5,7,10,9,7,4,9,4,7,9,6,9,5]
sQtA=pd.Series(lNumDisc,index=lAlunos)
print(sQtA.max())
print(sQtA.idxmax())
print(sTurAl.loc[sQtA.idxmax()])
print('--------------------')

#   Qual a quantidade média de disciplinas cursadas? 
print(sQtA.mean())
print('--------------------')

#   Qual a quantidade média de disciplinas cursadas em cada engenharia ?
sQtTur=pd.Series(lNumDisc,index=lEng)
gQtTur=sQtTur.groupby(level=0)
print(gQtTur.agg('mean'))
print('--------------------')

#   Qual  maior quantidade média de disciplinas cursadas? Em qual engenharia? Pense: e se houver empate?
print(gQtTur.agg('mean').max())
print('--------------------')

#   Qual a quantidade de disciplinas cursadas  mais frequente?
print(sQtA.mode())
print('--------------------')

#   Quantos alunos por quantidade de disciplinas cursadas- Utilizando o value_counts
print(sQtA.value_counts())
print('--------------------')

#   Qual a Engenharia com maior qt total de disciplinas cursadas?
print(gQtTur.agg('sum').idxmax())
print('--------------------')

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#============================================
#       Visualização Gráfica
#============================================
# 
#	Visualize (separadamente) as Series de forma gráfica (pizza com percentual)


# Exibir imediatamente o gráfico 
# Necessário usar o matplotlib:
#    import matplotlib.pyplot as plt
#    s.plot(...)  --> monta o gráfico
#    plt.show()   --> exibe o gráfico montado

# Exibir  mais de um gráfico simultaneamente:
    # Necessário usar definição do matplotlib de áreas de impressão:
#           import matplotlib.pyplot as plt
#    1) Criar janela para desenho de figura:
#           plt.figure(nº)
#    2) Dividir a janela de figura em áreas de impressão:
#            plt.subplots(nrows, ncols)
#       onde nrows and ncols são usados para dividir a figura em nrows * ncols eixos, 
#    3) Selecionar a área para plotar:
#            plt.subplot(nrows, ncols, plot_number)
#       onde nrows and ncols são usados para dividir a figura em nrows * ncols eixos, 
#       e plot_number ié usado para identificar em qual área (supblot) 
#       a função atual deve ser desenhada. plot_number inicia  em  1, 
#       incrementado primeiro pela linha
#  Exemplo Exibindo 2 gráficos um ao lado do outro:
#  import matplotlib.pyplot as plt
#  plt.figure(1)
#  plt.subplots(1,2)
#  plt.subplot(1,2,1)
#  s.plot.pie(figsize=(12,6),legend=True,autopct="%.1f")
#  plt.subplot(1,2,2)
#  s.plot.bar()
#  plt.show()

print("\nVisualizando % de disciplinas por Engenharia\n")
gQtTur.agg('sum').plot.bar(title = "Total para cada Engenharia")
plt.show()