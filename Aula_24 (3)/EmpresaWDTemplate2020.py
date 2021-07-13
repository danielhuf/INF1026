# -*- coding: utf-8 -*-
"""

O livro “Estatística Básica” de W. O. Bussab e P. A. Morettin traz no segundo capítulo um conjunto de dados hipotético de atributos de 36 funcionários da companhia “Milsa”
"""
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)   #Tirar os 3 pontinhos do pd
pd.set_option('display.max_rows', None)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#  Criando DataFrame a partir do  arquivo excel arquivo EmpregadosWD2020.xlsx que
#  contém dados dos funcionários de uma empresa
#     Todas as planilhas contém linhas de cabeçalho
#     Usar a 1ª coluna como indexador de linhas
#
#   dfDiurno: planilha Diurno 
#   dfNoturno: planilha Noturno
#   dfFilial: planilha Filial
#   
#------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

dfDiurno=pd.read_excel('EmpregadosWDFILIAL2020.xlsx',sheet_name='Diurno',decimal=',',header=0,index_col=0)
dfNoturno=pd.read_excel('EmpregadosWDFILIAL2020.xlsx',sheet_name='Noturno',decimal=',',header=0,index_col=0)
dfFilial=pd.read_excel('EmpregadosWDFILIAL2020.xlsx',sheet_name='Filial',decimal=',',header=0,index_col=0)

dfDiurno=pd.DataFrame(dfDiurno)# Só para o Spyder mostrar os parãmetros dos métodos
dfNoturno=pd.DataFrame(dfNoturno)
dfFilial=pd.DataFrame(dfFilial)
dfDiurno.sum()
l=['Estado Civil', 'Grau de Instrução', 'No de Filhos','Salário Mínimo', 'Região de Procedência']
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#  1)Concatenando os df
#  1.a) Somar 28 aos valores do index do dfNoturno para que não haja 2 funcionários com mesmo No
#      Possibilidade 1:
#        criar uma função que recebe o valor do index e retorna acrescido de 28
#        aplicar o método  .rename(mapper=função, axis= 0)
def soma28(x):
    return x+28
dfNoturno.rename(mapper=soma28,axis=0,inplace=True)
#      Possibilidade 2:
#        reseta o index, soma e seta o index novamente
#
#  1.b)Concatenar os funcionários dos dois turnos mantendo a informação de turno--> dfEmpreg
dfEmpreg=pd.concat({'diu':dfDiurno,'not':dfNoturno},sort=False)

#  1.c) Tornar a informação de turno uma coluna de dados ( .reset_index))
dfEmpreg.reset_index(level=0,inplace=True)
dfEmpreg.rename(columns={'level_0':'Turno'},inplace=True)

#  1.d)Concatenar o bairro da filial do dfFilial
#      CUIDADO: o index deste df é o número da filial
dfEmpreg.reset_index(inplace=True)
dfEmpreg.set_index('Num Filial',inplace=True)
dfEmpreg=pd.concat([dfEmpreg,dfFilial],axis=1,join='inner',sort=False)
dfEmpreg.reset_index(inplace=True)
dfEmpreg.set_index('No',inplace=True)

#  1.e)Eliminar o número da filial
dfEmpreg.drop('Num Filial',axis=1,inplace=True)
print(dfEmpreg.head(5))
print('------------------------------------------------------\n')
#  
#------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#  2)Rápida Exploração dos Dados
#     a.Analise seu DataFrame: nome e tipo das colunas, quais os indices, 
#                               5 primeiros e 5 ultimos registros
#     b.Visualizar resumo dos campos usando a função describe ()
#     c.Há valores ausentes? Observe pelo .info()
#     d.Visualizar os valores não numéricos pela tabela de frequência
#     e.Visualizar Estado Civil,Grau de Instrução, Salário Mínimo,Região de Procedência
#        do df ordenado pela região de procedência/valor do salário
#------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

print('\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
print('\n Rápida Exploração dos Dados \n')
print('\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')


print('2.a.1) Nome das colunas: ')
print(dfEmpreg.columns.name)
print('------------------------------------------------------\n')

print('2.a.2)Tipo das colunas: ')
print(dfEmpreg.columns.dtype)
print('------------------------------------------------------\n')

print('2.a.3) Nome dos Indices: ')
print(dfEmpreg.index.name)
print('------------------------------------------------------\n')

print('2.a.4) Primeiros')
print(dfEmpreg.head())
print('------------------------------------------------------\n')

print('2.a.5) Últimos')
print(dfEmpreg.tail())
print('------------------------------------------------------\n')

#b

print('\n2.b) Resumo dos campos com describe:')
print(dfEmpreg.describe())
print('------------------------------------------------------\n')

#c
print('\n2.c) Observando pelo .info:')
print(dfEmpreg.info())
print('------------------------------------------------------\n')

#d

print('\n2.d) Distribuição de frequência dos valores não numéricos:')
print(dfEmpreg['Turno'].value_counts())
print(dfEmpreg['Estado Civil'].value_counts())
print(dfEmpreg['Grau de Instrução'].value_counts())
print(dfEmpreg['Região de Procedência'].value_counts())
print(dfEmpreg['Bairro'].value_counts())
print('------------------------------------------------------\n')

#e

print('\n2.e) Ordenado por Região de Procedência/Salário:')
print(dfEmpreg.sort_values(by=['Região de Procedência','Salário Mínimo']))

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#  3)Renomeando valores e colunas
#     a. Aplique uma função sobre a coluna Estado Civil 
#        para que haja 3 estados civis: CASADO, SOLTEIRO,OUTROS
def estado(x):
    if x[0] in 'cC':
        return 'CASADO'
    elif x[0] in 'sS':
        return 'SOLTEIRO'
    return 'OUTROS'
dfEmpreg['Estado Civil']=dfEmpreg['Estado Civil'].apply(estado)

#     b.Renomeie as colunas para que os nomes não tenham espaços em branco (.rename)
#     Por exemplo:
#              'Id Anos':'IdAnos',
#             ' Estado Civil': 'EstCiv',
#              'No de Filhos':'NumFilhos',
#              'Grau de Instrução':'GInstr',
#              'Salário Mínimo':'SalMin', 
#              'Região de Procedência':'RegProc'
dfEmpreg.rename(columns={"Id Anos": "IdAnos", "Estado Civil": "EstCiv", "No de Filhos": "NumFilhos", "Grau de Instrução": "GInstr", "Salário Mínimo": "SalMin", "Região de Procedência": "RegProc"},inplace=True)

#     c. Exibir 5 primeiros e 5 últimos atualizados
print(dfEmpreg.head(5))
print(dfEmpreg.tail(5))
print('------------------------------------------------------\n')
#------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

print('\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
print('\n 3. Renomeando valores e colunas  \n')
print('\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')


print('\n3.c dfEmpreg atualizada:')

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#  4)Analisando os Dados e Consertando valores ausentes
#     a. obtenha e exiba numerica e graficamente a distribuição de frequência 
#        da variável grau instrução e também o percentual
print(dfEmpreg['GInstr'].value_counts())
print(dfEmpreg['GInstr'].value_counts()*100/dfEmpreg['GInstr'].value_counts().sum())
dfEmpreg['GInstr'].value_counts().plot.pie(autopct='%.2f',figsize=(8,8))
plt.show()
print('------------------------------------------------------\n')

#     b. preencha o número de filhos dos empregados solteiros com 0
f=dfEmpreg['EstCiv']=='SOLTEIRO'
s=dfEmpreg['NumFilhos'].loc[f]
s.fillna(0,inplace=True)
dfEmpreg['NumFilhos'].update(s)
print("\n4.b) preencha o número de filhos dos empregados solteiros com 0")
print(dfEmpreg.head(10))
print('------------------------------------------------------\n')

#     c. Preencher o número de filhos dos demais empregados com a moda (CUIDADO)
maisAcontece = dfEmpreg['NumFilhos'].drop(s.index).mode()  #Dei o drop para não pegar os solteiros
dfEmpreg['NumFilhos'].fillna(maisAcontece.iloc[0],inplace=True)
print("\n4.c) preencha o número de filhos dos demais empregados com a moda")
print(dfEmpreg.head(10))
print('------------------------------------------------------\n')

#     d. observe que alguns funcionários não preencheram o salário.
#        Quais os possíveis valores?  
#        Vamos preencher com  a média de seu Grau de instrução
#          Possibilidade 1) por meio do apply em cada grupo de grau de instrução
#
#                        i.definir uma função que recebe um grupo, 
#                            calcula a média, 
#                            preenche os ausentes com este valor
#                            retorna o grupo atualizado
#                        ii.agrupar por  grau de instrução
#                        iii.sCons<-aplicar a função em cada grupo, 
#                              sobre a coluna de salário mínimo
#                        iv.dfEmpreg['SalMin'].update(sCons) 
def consertaSalario(S):
    mediagrau=S.mean()
    S.fillna(mediagrau,inplace=True)
    return S

gGI=dfEmpreg.groupby('GInstr')
sCons=gGI['SalMin'].apply(consertaSalario)
dfEmpreg['SalMin'].update(sCons) 
print("\n4.d) preencha o salmin dos empregados com  a média de seu Grau de instrução")
print(dfEmpreg.head())
print('------------------------------------------------------\n')

#          Possibilidade 2) i. reindexa por Grau de instrução
#                           ii.sCons<-calcula a média de salário mínimo, (level=0)
#                           iii.dfEmpreg['SalMin'].fillna(sCons)
#                           iV. reindexa pelo nº do funcionário 
#       
#
#    e. obtenha e exiba graficamente a frequência  dos empregados por faixa de salário
#        Faixas de Salários
#        4,00 |--- 8,00
#        8,00 |--- 12,00
#        12,00 |--- 16,00
#        16,00 |--- 20,00
#        20,00 |--- 24,00
sFxSal=pd.cut(dfEmpreg['SalMin'],bins=[4,8,12,16,20,24],include_lowest=True)
sFxSal.value_counts().plot.bar()
plt.show()
print('------------------------------------------------------\n')

#
#   f. obtenha e a quantidade de funcionários por Bairro ( tabela de frequência)
tfB=dfEmpreg['Bairro'].value_counts()
print("\n4.f) Tabela de Frequência - Bairro")
print(tfB)
print('------------------------------------------------------\n')
# 
#   g. considere a seguinte series: 
sReaj=pd.Series([0.37,0.35,0.3],
                index=['Ensino fundamental','Ensino superior','Ensino médio'],
                name='reaj')
#      utilize-a para atualizar os salários
#      Dica: concatene a sReaj ao df (cuidado com os indices)
#            atualize a coluna de salário
#            elimine a coluna reaj
sReaj=1+sReaj
dfEmpreg.reset_index(inplace=True)
dfEmpreg.set_index('GInstr',inplace=True)
dfEmpreg=pd.concat([dfEmpreg,sReaj],axis=1,join='inner',sort=False)
dfEmpreg.index.name='GInstr'
dfEmpreg['SalMin']=dfEmpreg['SalMin'].mul(dfEmpreg['reaj'])
dfEmpreg.drop('reaj',axis=1,inplace=True)
dfEmpreg.reset_index(inplace=True)
dfEmpreg.set_index('No',inplace=True)

print("\n4.g) Salários atualizados")
print(dfEmpreg.head())
print('------------------------------------------------------\n')
#
#   h. Criar a coluna Idade: IdAnos + IdMeses/12
dfEmpreg['Idade']=dfEmpreg['IdAnos'].add(dfEmpreg['IdMeses'].div(12))
dfEmpreg.drop(['IdAnos','IdMeses'],axis=1,inplace=True)
print("\n4.h) Idade Atualizada")
print(dfEmpreg.head())
print('------------------------------------------------------\n')
#
#   i. Qual a idade média, mediana, mínima, máxima? E por Grau de Instrução?
print("\n4.i) idade média, mediana, mínima, máxima")
print(dfEmpreg['Idade'].mean(),dfEmpreg['Idade'].median(),dfEmpreg['Idade'].min(),dfEmpreg['Idade'].max())

print("\n4.i) idade média, mediana, mínima, máxima por grau de instrução")
g=dfEmpreg['Idade'].groupby(by=dfEmpreg['GInstr'])
print(g.agg(['mean','median','min','max']))
print('------------------------------------------------------\n')
#
#   j. Qual o maior salário? Exiba um funcionário que o receba.
print(dfEmpreg['SalMin'].max())
print(dfEmpreg['SalMin'].idxmax())
print('------------------------------------------------------\n')
#
#   k. Qual o total pago em salários? E por Bairro? E por Turno?
print(dfEmpreg['SalMin'].sum())
g=dfEmpreg['SalMin'].groupby(by=dfEmpreg['Bairro'])
print(g.agg('sum'))
g=dfEmpreg['SalMin'].groupby(by=dfEmpreg['Turno'])
print(g.agg('sum'))
print('------------------------------------------------------\n')
#  
#   l  Qual região de procedência tem maior média de número de filhos? Capital, Interior ou Outras?
g=dfEmpreg['Idade'].groupby(by=dfEmpreg['RegProc'])
s=g.agg('mean')
print("\n4.l) Região de procedência com maior número de filhos:")
print(s.idxmax())
#
#------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

# COMPLETAR O TEMPLATE
print('\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
print('\n 4. Analisando os Dados e Consertando valores ausentes  \n')
print('\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')

'''

As técnicas de análise de dados diferenciam três situações. Quando as variáveis 
são qualitativas, os dados são resumidos em tabelas de dupla entrada (ou
de contingência), onde aparecerão as frequências absolutas ou contagens de
indivíduos que pertencem simultaneamente a categorias de uma e outra variável;
quando as duas variáveis são quantitativas, as observações são provenientes de
mensurações e quando se tem uma variável qualitativa e outra quantitativa, em geral
analisa-se o que acontece com a variável quantitativa quando os dados são
categorizados de acordo com os diversos atributos da variável qualitativa

https://chrisalbon.com/python/pandas_crosstabs.html
pd.crosstab([df.company, df.experience], df.regiment,  margins=True)
'''

print('\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
print('\n Cruzamento de colunas \n')
print('\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')

'''
Analisando relações entre os valores das colunas: cruzamento de colunas ---> COMPLETAR MARCADOS
1 - Cruzamento  salário x o grau de instrução . Visualizar graficamente e via  gráfico de dispersão
2 - Cruzamento  salário x região de procedência------>  COMPLETAR
3 - Cruzamento  salário x idade - CUIDADO: Deve incluir os meses
4 - Cruzamento  grau de instrução x nº de filhos
5 - Cruzamento  grau de instrução x região de procedência----->  COMPLETAR
6 - Cruzamento  faixa salarial x grau de instrução. ----->  COMPLETAR
7 - Cruzamento  faixa salarial x grau de instrução/Número de Filhos. ----->  COMPLETAR
8-  Cruzamento  grau de instrução / estado civil  x região de procedência / faixa salarial----->  COMPLETAR

'''

'''
1 - Cruzamento  salário x grau de instrução
    a) Visualização tabular
    b) Gráfico de barras
    c) Gráfico de dispersão ( scatter)
'''
#a
dfSalInstr = pd.crosstab(index=dfEmpreg['SalMin'],columns=dfEmpreg['GInstr'])
print('\n1.a) - Cruzamento  salário x grau de instrução:\n')
print(dfSalInstr)

#b
dfSalInstr.plot.bar(title='1.b) salário x grau de instrução')
plt.show()

#c ---> Gráfico de dispersão (scatter)
#   Como a coluna grau de instrução é categórica--> transformar em numérica

def relacaoNumerica(grau):
    if 'fundamental' in grau:
        return 1
    elif 'médio' in grau:
        return 2
    else:
        return 3

print('\n1.c) - salário x  grau de instrução:\n')
dfAux=pd.DataFrame()
dfAux['Grau de Instrução']=dfEmpreg['GInstr'].apply(relacaoNumerica)
dfAux['Qt de Salários Mínimos']=dfEmpreg['SalMin']
dfAux.plot.scatter(x='Qt de Salários Mínimos', y='Grau de Instrução', title='1.c) - salário x  grau de instrução:')
plt.show()
'''
2 - Cruzamento  salário x região de procedência
'''


'''
3 - Cruzamento  salário x idade - CUIDADO: Deve incluir os meses
'''

'''
observa-se a necessidade de categorizar, isto é, criar faixas para a idade dos empregados
    a) Criar faixas de idade:  de 10 em 10 anos
    b) Fazer o cruzamento

'''

'''
4 - Cruzamento  grau de instrução x nº de filhos
'''



'''
5 -  Cruzamento  grau de instrução x região de procedência
'''



'''
6 -  Cruzamento da faixa salarial x  grau de instrução 

'''


'''
7 - Cruzamento  faixa salarial x grau de instrução/Número de Filhos. 
'''


'''
8 - Cruzamento  grau de instrução/estado civil x região de procedência /faixa salarial
'''


