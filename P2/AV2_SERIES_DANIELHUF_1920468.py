# -*- coding: latin-1 -*-
# S92
###########################################################################################
#Nome completo: Daniel Stulberg Huf
#Matrícula PUC-Rio: 1920468
#Declaração de autoria: declaro que este documento foi produzido por mim em sua totalidade ,
#                 sem consultas a outros alunos, professores ou qualquer outra pessoa.
############################################################################################
import pandas as pd
import matplotlib.pyplot as plt
print('============================')
print('Trabalhando com SERIES')
print('============================')
sVal = pd.read_excel('Transacoes.xlsx', sheet_name='ValorTransacao', header=0,index_col=0, squeeze=True)
sTipo = pd.read_excel('Transacoes.xlsx',sheet_name='TipoTransacao', header=0,index_col=0, squeeze=True)
sDest = pd.read_excel('Transacoes.xlsx',sheet_name='DestinoTransacao', header=0,index_col=0, squeeze=True)
sBairroZona = pd.read_excel('Transacoes.xlsx',sheet_name='BairroZona', header=0,index_col=0, squeeze=True)
"""
**** Questão 1 ****
Exibir as Series criadas
"""
print('-----------------------------------')
print('1- 3 primeiros de sVal e de sTipo e 5 últimos de sDest e de sBairroZona')
print(sVal.head(3))
print('-----------------------------------')
print(sTipo.head(3))
print('-----------------------------------')
print(sDest.tail(5))
print('-----------------------------------')
print(sBairroZona.tail(5))
print('-----------------------------------')

"""
**** Questão 2 ****
Em alguns horários o tipo de transação (sTipo) está  sem valor.
Estes horários devem ser eliminados nas 3 Series (sVal, sTipo, sDest).
"""
print('-----------------------------------')
print('2- 5 primeiros de sDest e 5 últimos de sTipo sem tipo ausente')
aus=list(sTipo.loc[sTipo.isnull()].index)
sVal.drop(aus,inplace=True)
sTipo.drop(aus,inplace=True)
sDest.drop(aus,inplace=True)
print(sDest.head(5))
print('-----------------------------------')
print(sTipo.tail(5))
print('-----------------------------------')

"""
**** Questão 3 ****
Substituir os valores de transação ausentes pelo menor valor 
dos respectivos tipos da transação.
•	Por exemplo, o valor ausente em um aluguel de bicicleta,
     deve ser substituído pelo menor valor entre os de aluguel.
Caso vc não saiba resolver esta questão,substitua os valores ausentes de sVal por 999
"""
print('-----------------------------------')
def preencheAus(g):
    menor=g.min()
    g=g.fillna(menor)
    return g
sOi=pd.Series(sTipo.index,sTipo.values)
sAux1=pd.Series(sVal.values,sOi.index)
gTipo=sAux1.groupby(level=0)
sAux2=gTipo.transform(preencheAus)
sVal=pd.Series(sAux2.values,sVal.index)
print('3- 3 primeiros elementos de sVal')
print(sVal.head(3))
print('-----------------------------------')

"""
**** Questão 4 ****
Coloque as zonas de sBairroZona em letras maiúsculas.
"""
print('-----------------------------------')
print('4- sBairroZona em maiúsculo.')
sBairroZona=sBairroZona.str.upper()
print(sBairroZona)
print('-----------------------------------')

"""
**** Questão 5 ****
Qual o valor da menor transação? Em quais horários ocorreram?
"""
print('-----------------------------------')
print('5- Menor transação e horários em que ocorreram')
print(sVal.min())
print(list(sVal.loc[sVal==sVal.min()].index))
print('-----------------------------------')

"""
**** Questão 6 ****
Quantos bairros há em cada zona? 
"""
print('-----------------------------------')
print('6- Quantidade de bairros em cada zona')
sInv=pd.Series(sBairroZona.index,sBairroZona.values)
gZona=sInv.groupby(level=0)
print(gZona.agg('count'))
print('-----------------------------------')

"""
**** Questão 7 ****
Qual hora cheia teve o maior valor médio?
   hora cheia: desconsiderar os minutos do horário
"""
print('-----------------------------------')
print('7- Hora cheia com maior valor médio')
def hora(x):
    return x[:2]
gHora=sVal.groupby(hora)
print(gHora.agg('mean').idxmax())
print('-----------------------------------')

"""
**** Questão 8 ****
Qual o valor mediano das transações?
Qual o valor mediano por destino (bairro)?
Qual o valor mediano por hora cheia/tipo de transação/destino (bairro)?
"""
print('-----------------------------------')
print('8- Valor mediano das transações? E por tipo de transação? E por destino(bairro)/hora cheia/tipo de transação')
print(sVal.median())
print('-----------------------------------')
gBai=sVal.groupby(sDest)
print(gBai.agg('median'))
print('-----------------------------------')
gTudo=sVal.groupby([hora,sTipo,sDest])
print(gTudo.agg('median'))
print('-----------------------------------')

"""
**** Questão 9 ****
Considerando os bairros existentes na sBairroZona,
    liste o nome dos bairros em que não houve transação.
"""
print('-----------------------------------')
print('9- Bairros sem transações')
BairrosCom=list(sDest.unique())
print(list(sBairroZona.drop(BairrosCom).index))
print('-----------------------------------')

"""
**** Questão 10 ****
Liste os destinos, sem repetição, em que houve transações do tipo aluguel.
"""
print('-----------------------------------')
print('10- Bairros com aluguel de bicicleta')
horaAlug=list(sTipo.loc[sTipo=='Aluguel'].index)
destinos=sDest.loc[horaAlug]
print(list(destinos.unique()))
print('-----------------------------------')

"""
**** Questão 11 ****
Considerando os seguintes turnos:
    00:00 às 12:00 - manhã
    12:01 às 18:00 – tarde
    18:01 às 23:59 – noite
a) Construa a Series sTurno com o turno das transações
b) Mostre graficamente (pizza) a quantidade de transações em cada turno
"""
print('-----------------------------------')
print('11- Gráfico da quantidade de transações em cada turno')
sInv=pd.Series(sVal.index,sVal.values)
sAux=sInv.apply(hora)
sTurno=pd.cut(sInv,bins=['0','12','18','23'],labels=['manhã','tarde','noite'],include_lowest=True)
sTurno.value_counts().plot.pie(autopct='%.1f')
plt.show()
print('-----------------------------------')

"""
**** Questão 12 ****
Qual o valor total, mediano e máximo por tipo de transação em cada turno?
"""
print('-----------------------------------')
print('12- Valor total, mediano, máximo por tipo de transação x turno')
sInv=pd.Series(sTurno.index,sTurno.values)
gTurno=sInv.groupby(level=0)
print(gTurno.agg(['sum','median','max']))
print('-----------------------------------')

"""
**** Questão 13 ****
Construa a Series sZona.
Esta Series armazena a Zona de destino da bicicleta de cada transação.
Portanto, o index é o horário da transação e
          o valor é a Zona de destino considerando o destino(bairro).
"""
print('-----------------------------------')
print('13- Exibir os 5 primeiros e 5 últimos de sZona.')
def detZona(bairro,s):
    return s.loc[bairro]
sZona=sDest.apply(detZona,args=(sBairroZona,))
print(sZona.head(5))
print(sZona.tail(5))
print('-----------------------------------')

"""
**** Questão 14 ****
Mostre, por zona, o valor total recebido
por alugar as bicicletas e por vendê-las.
"""
print('-----------------------------------')
print('14- Total recebido em aluguel e total recebido em vendas, por zona')
gZonaTipo=sVal.groupby([sZona,sTipo])
print(gZonaTipo.agg('sum'))
print('-----------------------------------')

