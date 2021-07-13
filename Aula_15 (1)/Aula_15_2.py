import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sGastosDia=pd.read_excel("gastosAlimPaiMae.xlsx", header=None, usecols=(1,2),
                      index_col=0,squeeze=True,decimal=',')

sGastosPMDia= pd.read_excel('gastosAlimPaiMae.xlsx',index_col=[0,1],header=0,squeeze=True)

#sGastosPMDia.sort_index(inplace=True)
#ORDENEI OS ÍNDICES E MUDEI A ESTRUTURA ORIGINAL (NÃO CRIEI UMA CÓPIA)

#A MAIORIA DOS MÉTODOS NÃO ALTERA A ESTRUTURA ORIGINAL DE UMA SERIES

#O REINDEX CRIA OUTRA SERIES NA ORDEM DE INDICES QUE EU ESCOLHER (NÃO PRECISO USAR TODOS OS ÍNDICES)

#ENTRE CADA GRÁFICO, COLOCAR PLT.SHOW()

##################################################################
#   Exibir Series
###################################################################

print('\n-----------------------------------------------------\n')
print('Gastos por dia:')
print(sGastosDia)
print('\n-----------------------------------------------------\n')
print('Exibindo cópia de sGastosDia após ordenar por índice')
sOrd=sGastosDia.sort_index()
print(sOrd)
print('\n-----------------------------------------------------\n')
print('Gastos por progenitor/dia:')
print(sGastosPMDia)
print('\n-----------------------------------------------------\n')
print('Exibindo cópia de sGastosPMDia após ordenar por índice')
sOrd=sGastosPMDia.sort_index()
print(sOrd)

##################################################################
#   Aplicar uma função de formatação sobre elementos da sGastos
###################################################################

print('\n-----------------------------------------------------\n')
print('Gastos por dia formatado:')
print (sGastosDia.apply('{:.2f}'.format))
print('\n-----------------------------------------------------\n')
print('Gastos por progenitor/dia formatado:')
print (sGastosPMDia.apply('{:.2f}'.format))

##################################################################
#   Aplicar uma função de reajuste sobre elementos da sGastos,alterando-os
#   Os valores superiores ao limite lim devem sofrer reajuste de perc%
###################################################################

def reajuste(x,lim,perc):
    if x>lim:
        return x*(1+perc/100)
    else:
        return x
    
sGastosDia=sGastosDia.apply(reajuste, args=(15,10))

print('\n-----------------------------------------------------\n')
print('Reajustados:')
print(sGastosDia.apply('{:.2f}'.format))

####################################################################
# Series sGastosDia -   índices com repetição
#   Criar uma cópia de sGastos
#   Alterar o gasto de 'Sab' para 1500
#   Alterar o gasto de 'Seg' para 9999 
#   Exibir #Observe os valores
#   Eliminar a 'Ter' na cópia sem inplace=True
#   Eliminar a 'Seg' na cópia com inplace=True

sC=sGastosDia.copy()
print('\n-----------------------------------------------------\n')
sC.loc['Sab']=1500
sC.loc['Seg']=9999
print('Cópia de sGastosDia modificada:')
print(sC.apply('{:.2f}'.format))  #Observe os valores ed seg e sab
print('\n-----------------------------------------------------\n')
sC.drop('Ter' )
print('Cópia de sGastosDia após drop na Ter sem inplace=True:')
print(sC.apply('{:.2f}'.format))  
print('\n-----------------------------------------------------\n')
sC.drop('Seg',inplace=True )
print('Cópia de sGastosDia após drop na Seg com inplace=True:')
print(sC.apply('{:.2f}'.format)) 
print('\n-----------------------------------------------------\n')

##################################################################
#   Visualização Gráfica
###################################################################
#
# Exibir graficamente 
#  Atributos comuns:
#    title="título", padrão ''
#    figsize=(a,l),  padrão None
#    legend=True/False  padrão False
#  Linha:
#     series.plot() ou series.plot.line()
#     Principais atributos ajustáveis:
#          color – a cor e pode ser r(red), b(blue), k(black)...
#          linestyle – o formato da linha. Para que a mesma não seja contínua define-se como '-'.
#          linewidth – espessura da linha.
#          marker – o formato dos pontos: 's' (square) - quadrados, '^'- triângulos, '*',etc.
#  Pizza:
#     series.plot.pie( autopct="%.1f")
#  Barra:
#     Vertical  : series.plot.bar()
#     Horizontal: series.plot.barh()
#     Principais atributos ajustáveis:
#           x - posição das barras no eixo X 
#           y - altura das barras no eixo Y 
#          width - espessura das barras
#         color -  cor

sGastosDia.plot.line(title="Gastos com o Pai",figsize=(6,6),	linestyle='--',linewidth=3.0, color='r', marker='s')
plt.show()
sGastosDia.plot.bar(title="Gastos com o Pai",	figsize=(6,6),color='y', width = 0.5)
plt.show()
sGastosDia.plot.barh(title="Gastos com o Pai", figsize=(6,6),color='g', width = 0.8)
plt.show()
sGastosDia.plot.pie(title="Gastos com o Pai", colors= ['c','m','r','b','k','g','y'],
			    legend = True, autopct="%.1f",figsize=(6,6)) 
plt.show()

#-----------------------------------------------------------------------------

# Exibir imediatamente o gráfico 
# Necessário usar o matplotlib:
#    import matplotlib.pyplot as plt
#    s.plot(...)  --> monta o gráfico
#    plt.show()   --> exibe imediatamente o gráfico montado

#-----------------------------------------------------------------------------
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

# Responder as seguintes perguntas sobre sGastosDias:
#    Quantos gastos ocorreram?
#    O gasto total? O gasto médio, mediana, moda?
#    Tabela de frequência dos valores gastos    
#    
#    Qual o menor valor gasto? Em qual dia?
#    Qual o maior valor gasto? Em qual dia?
#    
#    O gasto total por dia? O gasto médio por dia?
#    
#    Em qual dia gastou mais?
#    Em qual dia gastou menos?
# 

#-----------------------------------------------------------------------------
def resumos_sGastosDias(s):
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Resumos sGastosDias")
    print('\nQuantidade total:\n {}'.format(s.count()))
    print('\nValor Total:\n {}'.format(s.sum()))
    print('\nValor Médio:\n {}'.format(s.mean()))
    print('\nMediana:\n {}'.format(s.median()))
    print('\nModa:\n{}'.format(s.mode()))
    print("\nFrequencia dos valores\n{}".format(s.value_counts()))
    
    print('\nÍndice de um Maior: {:<s}'.format(s.idxmax()))
    print('Valor do Maior: {:.2f}'.format(s.max()))
    print('\nÍndice de um Menor: {:<s}'.format(s.idxmin()))
    print('Valor do Menor: {:.2f}'.format(s.min()))
    
    sDia=s.sum(level=0)
    print('\nGasto total por dia:\n{}'.format(sDia))
    print('\nGasto total por dia reindexado:\n{}'.format(sDia.reindex(['Seg','Ter','Qua','Qui','Sex','Sab','Dom'])))
    print('\nGasto médio por dia:\n{}'.format(s.mean(level=0)))
    print('\nValor do Maior Gasto no dia: {:.2f}'.format(sDia.max()))
    print('\nÍndice de um Maior: {:<s}'.format(sDia.idxmax()))
    print('\nÍndice de um Menor: {:<s}'.format(sDia.idxmin()))
    print('\n Valor do Menor: {:.2f}'.format(sDia.min()))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    return
resumos_sGastosDias(sGastosDia)

# Responder as seguintes perguntas sobre sGastosPMDia:
#   Geral:              
#       Exibir numericamente o número de entradas, o total, a média, mediana, moda, 
#       maior e menor valores e de quais índices - gerais
#       Exibir a frequência dos índices

#   Pelo dois níveis de índice: Progenitor/Dia da Semana  e Dia da Semana/Progenitor
#       Exibir numericamente o total , a média, mediana, 
#       maior e menor valores e um dos índices com tais valores
#       Exibir graficamente (por pizza) o total,  mediana 
#       Exibir graficamente (por linha) a média 
#       Exibir graficamente (por barra) maior e menor valores 

#  Separados: Progenitor  e Dia da Semana:
#       Exibir numericamente, o total, a média, mediana, 
#       maior e menor valores e um dos índices com tais valores 
#  

def resumos_sGastosPMDia(s):
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Resumos sGastosPMDias - Geral: ")
    print('\nQuantidade total:\n {}'.format(s.count()))
    print('\nValor Total:\n {}'.format(s.sum()))
    print('\nValor Médio:\n {}'.format(s.mean()))
    print('\nMediana:\n {}'.format(s.median()))
    print('\nModa:\n{}'.format(s.mode()))
    print("\nFrequencia dos Índices\n{}".format(s.index.value_counts()))
    
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Resumos sGastosPMDias - Por Dia: ")
    sDia=s.sum(level=1)
    print('\nGasto total por dia:\n{}'.format(sDia))
    print('\nGasto total por dia reindexado:\n{}'.format(sDia.reindex(['Seg','Ter','Qua','Qui','Sex','Sab','Dom'])))
    print('\nGasto médio por dia:\n{}'.format(s.mean(level=1)))
    print('\nValor do Maior Gasto por dia:\n{}'.format(s.max(level=1)))
   
    print('\n Valor do Menor por dia:\n{}'.format(s.min(level=1)))
    
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Resumos sGastosPMDias - Por Progenitor: ")
    sPro=s.sum(level=0)
    print('\nGasto total por prgenitor:\n{}'.format(sPro))
    print('\nGasto total por prgenitor reindexado:\n{}'.format(sPro.reindex(['Pai','Mae'])))
    print('\nGasto médio por prgenitor:\n{}'.format(s.mean(level=0)))
    print('\nValor do Maior Gasto por prgenitor: {}'.format(s.max(level=0)))
   
    print('\n Valor do Maior por progenitor:\n{}'.format(s.min(level=0)))
    print('\n Valor do Menor por progentior:\n{}'.format(s.min(level=0)))

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Resumos sGastosPMDias - Por Dia/Progenitor: ")
    sD=s.sum(level=[1,0])
    print('\nGasto total por Dia/Progenitor:\n{}'.format(sD.sort_index()))
    print('\nGasto médio por Dia/Progenitor:\n{}'.format(s.mean(level=[1,0])))
    print('\nValor do Maior Gasto por Dia/Progenitor: {}'.format(s.max(level=[1,0])))
    print('\nÍndice de um Maior Dia/Progenitor: {}'.format(s.idxmax()))
    print('\n Valor do Menor por Dia/Progenitor:\n{}'.format((s.min(level=[1,0]).sort_index())))
    print('\nÍndice de um Menor Dia/Progenitor: {}'.format(s.idxmin()))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    return
resumos_sGastosPMDia(sGastosPMDia)
