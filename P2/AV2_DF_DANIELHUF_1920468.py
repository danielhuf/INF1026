# -*- coding: latin-1 -*-
# D59
##########################################################################################
#Nome completo: Daniel Stulberg Huf
#Matrícula PUC-Rio: 1920468
#Declaração de autoria: declaro que este documento foi produzido por mim em sua totalidade,
#                 sem consultas a outros alunos, professores ou qualquer outra pessoa.
###########################################################################################
import pandas as pd
import matplotlib.pyplot as plt
print('============================')
print('Trabalhando com DATAFRAME e SERIES')
print('============================')
pd.set_option('display.max_columns', None)
dfPerfil = pd.read_excel('CompraOnline.xlsx', sheet_name='perfil', header=0,index_col=0)
dfComportamento = pd.read_excel('CompraOnline.xlsx',sheet_name='comportamento', header=0,index_col=0)
sPesos = pd.read_excel('CompraOnline.xlsx',sheet_name='pesos', header=0,index_col=0, squeeze=True)
"""
**** Questão 1 ****
Exibir DataFrames criados
dfPerfil: Exiba os 5 primeiros e os 3 últimos elementos
             ordenados crescentemente por IDADE/RENDA
"""
print('-----------------------------------')
print('1- dfPerfil ordenado')
print(dfPerfil.sort_values(by=['IDADE','RENDA']).head(5))
print(dfPerfil.sort_values(by=['IDADE','RENDA']).tail(3))
print('-----------------------------------')

"""
**** Questão 2 ****
dfPerfil: Mostre numericamente, com duas casas decimais,
             o percentual de entrevistados de cada estado
"""
print('-----------------------------------')
print('2- Percentual de entrevistados de cada estado')
gEst=dfPerfil.groupby('UF')
freq=gEst['GENERO'].agg('count')
percent=freq/freq.sum()
print(percent)
print('-----------------------------------')

"""
**** Questão 3 ****
dfPerfil: Mostre os valores mais frequentes de cada coluna,
             substituindo NaN por "-" 
"""
print('-----------------------------------')
print('3- Mais frequentes')
moda=dfPerfil.mode()
print(moda.fillna(value='-',axis=1))
print('-----------------------------------')

"""
**** Questão 4 ****
dfPerfil: Mostre, sem repetição, a UF dos entrevistados
             com maior grau de instrução.
"""
print('-----------------------------------')
print('4- UF dos entrevistados com maior grau de instrução')
maiorGrau=dfPerfil.loc[dfPerfil['GINSTR']==dfPerfil['GINSTR'].max()]
gGrau=maiorGrau.groupby('UF')
print(list(gGrau.agg('count').index))
print('-----------------------------------')

"""
**** Questão 5 ****
dfPerfil: para cada gênero (GENERO), mostre o menor valor, o maior valor,
             a média e a mediana das idades e rendas familiares
"""
print('-----------------------------------')
print('5- Menor valor, o maior valor, a média e a mediana para cada gênero')
gGen=dfPerfil.groupby('GENERO')
print(gGen[['IDADE','RENDA']].agg(['min','max','mean','median']))
print('-----------------------------------')

"""
**** Questão 6 ****
dfPerfil: Substitua a coluna RENDA pela coluna CLASSE com a respectiva classe social 
             de acordo com os critérios abaixo:
              •  A: renda familiar superior a 15 salários mínimos;
              •  B: renda familiar superior a 5 salários mínimos até 15 salários mínimos ;
              •  C: renda familiar superior a 3 salários mínimos até 5 salários mínimos;
              •  D: renda familiar superior a 1 salário mínimo até 3 salários mínimos;
              •  E: até 1 salário mínimo.
    Apresente graficamente a tabela de frequência percentual das classes sociais dos entrevistados.
    Obs: Escolha a representação gráfica mais adequada
"""
print('-----------------------------------')
print('6- Gráfico da tabela de frequência percentual das classes sociais')
classe=pd.cut(dfPerfil['RENDA'],bins=[0,1,3,5,15,dfPerfil['RENDA'].max()],labels=['E','D','C','B','A'],include_lowest=True)
dfPerfil['RENDA']=classe
dfPerfil.rename(columns={'RENDA':'CLASSE'},inplace=True)
freq=dfPerfil['CLASSE'].value_counts()
freq.plot.pie(autopct='%.1f',figsize=(5,5))
plt.show()
print('-----------------------------------')

"""
**** Questão 7 ****
dfPerfil: Exiba a relação entre classe social e grau de instrução (CLASSE X GINSTR),
             ou seja, a tabela de frequência da classe social por grau de instrução.
"""
print('-----------------------------------')
print('7- Tabela de frequência da classe social por grau de instrução.')
print(pd.crosstab(dfPerfil['CLASSE'],dfPerfil['GINSTR']))
print('-----------------------------------')

"""
**** Questão 8 ****
dfComportamento: Inclua a coluna COMP com o valor que resume o comportamento.
              Este valor é calculado, somando a multiplicação das respostas
              do questionário pelos respectivos pesos das perguntas.
              Os pesos de cada pergunta do questionário estão na sPesos.
       Exiba as informações dos entrevistados com os 10 maiores valores da coluna COMP, ordenados decrescentemente
"""
print('-----------------------------------')
print('8- 10 maiores valores da coluna COMP, ordenados decrescentemente')
mult=dfComportamento*sPesos
dfComportamento['COMP']=mult.sum(axis=1)
print(dfComportamento.sort_values('COMP',ascending=False).head(10))
print('-----------------------------------')

"""
**** Questão 9 ****
dfComportamento: Altere os nomes das colunas para que contenham no máximo 10 caracteres,
        sem espaços e os caracteres letras em maiúsculas.
        Os novos nomes devem continuar elucidativos.
"""
print('-----------------------------------')
print('9- Nomes das colunas do dfComportamento')
dfComportamento.rename(columns={'Frequencia Compra':'FREQCOMP','Preocupacao Privacidade':'PREOPRIV',
                                'Confidencialidade de Dados Pessoais':'CONFDADOS','Rejeicao por seguranca':'REJEISEG',
                                'Seguranca dados do pagamento':'SEGDADOSP','Compra com empresa desconhecida':'COMPEMPD',
                                'Compra com pessoa desconhecida':'COMPPESD'},inplace=True)
print(list(dfComportamento.columns))
print('-----------------------------------')

"""
**** Questão 10 ****
dfComportamento: Elimine os entrevistados que nunca compraram online,
       isto é, responderam 0 à pergunta 1 (Frequencia Compra).
"""
print('-----------------------------------')
print('10- 3 últimas linhas do dfComportamento sem entrevistados que nunca compraram online.')
dfComportamento=dfComportamento.loc[dfComportamento['FREQCOMP']!=0]
print(dfComportamento.tail(3))
print('-----------------------------------')

"""
**** Questão 11 ****
dfComportamento: Elimine os entrevistados com respostas inconsistentes, isto é,
       tenham atribuído um grau superior a 3 à pergunta 4 (Rejeicao por seguranca) e
       um grau superior a 3 às perguntas 6 ou 7 (Compra com empresa desconhecida ou Compra com pessoa desconhecida).
"""
print('-----------------------------------')
print('11- 3 primeiras linhas do dfComportamento sem inconsistentes.')
dfComportamento=dfComportamento.query('REJEISEG<=3 and COMPEMPD<=3 and COMPPESD<=3')
print(dfComportamento.head(3))
print('-----------------------------------')

"""
**** Questão 12 ****
dfComportamento: Mostre a nota mediana atribuída à pergunta 4 (Rejeicao por seguranca) dos entrevistados
      cuja frequência de compra é acima da frequência média
"""
print('-----------------------------------')
print('12- Nota mediana de Rejeicao por seguranca para frequência acima da média')
freqAcima=dfComportamento.loc[dfComportamento['FREQCOMP']>dfComportamento['FREQCOMP'].mean()]
print(freqAcima['REJEISEG'].median())
print('-----------------------------------')

"""
**** Questão 13 ****
dfComportamento: Quantos entrevistados atribuíram uma nota superior a 4
       a todas as perguntas?
"""
print('-----------------------------------')
print('13- Quantidade de entrevistados com todas notas superior a 4')
semComp=dfComportamento.drop('COMP',axis=1)
maior4=semComp.drop(semComp<=4,axis=1)
print(maior4.columns.size)
print('-----------------------------------')

"""
**** Questão 14 ****
dfComportamento: A partir dos valores da coluna COMP, crie e exiba a series srCategoria,
      que classifica o entrevistado como CONSERVADOR, NORMAL e DESTEMIDO.
            •	CONSERVADOR: valores negativos até 10(inclusive);
            •	NORMAL: valores de 11 até 30;
            •	DESTEMIDO: valores superiores a 30.
    Utilizando a srCategoria, mostre, a quantidade de entrevistados em cada categoria
"""
print('-----------------------------------')
print('14- Quantidade de entrevistados em cada categoria')
srCategoria=pd.cut(dfComportamento['COMP'],bins=[dfComportamento['COMP'].max()*(-1),10,30,1000],labels=['CONSERVADOR','NORMAL','DESTEMIDO'],include_lowest=True)
print(srCategoria.value_counts())
#OBS: Utilizei 10000 como valor superior porque o valor máximo de
#dfComportamento['COMP'], no meu caso, era menor do que 30,
#o que gerava uma incongruência
print('-----------------------------------')

"""
**** Questão 15 ****
Crie o DataFrame dfCompleto, concatenando apropriadamente
      dfPerfil, dfComportamento e srCategoria
"""
print('-----------------------------------')
print('15- 5 últimos elementos do dfCompleto')
srCategoria.name='NIVEL'
dfCompleto=pd.concat([dfPerfil,dfComportamento,srCategoria],axis=1).dropna()
print(dfCompleto.tail(5))
print('-----------------------------------')

"""
**** Questão 16 ****
dfCompleto: Mostre em um gráfico de barras horizontais
      as 7 respostas dos entrevistados de SP
"""
print('-----------------------------------')
print('16- Gráfico das 7 respostas dos entrevistados de SP')
dfSp=dfCompleto.loc[dfCompleto['UF']=='SP']
dfSp[['FREQCOMP','PREOPRIV','CONFDADOS','REJEISEG','SEGDADOSP','COMPEMPD','COMPPESD']].plot.barh()
plt.show()
print('-----------------------------------')

"""
**** Questão 17 ****
dfCompleto: Qual o maior valor que resume o comportamento (COMP)
      por gênero e em cada classe social e UF?
"""
print('-----------------------------------')
print('17- Maior valor de COMP por gênero e em cada classe social e UF')
print(pd.crosstab(index=dfCompleto['GENERO'],columns=[dfCompleto['CLASSE'],dfCompleto['UF']],values=dfCompleto['COMP'],aggfunc='max'))
print('-----------------------------------')

