# -*- coding: latin-1 -*-
# S92
###########################################################################################
#Nome completo: Daniel Stulberg Huf
#Matr�cula PUC-Rio: 1920468
#Declara��o de autoria: declaro que este documento foi produzido por mim em sua totalidade ,
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
**** Quest�o 1 ****
Exibir as Series criadas
"""
print('-----------------------------------')
print('1- 3 primeiros de sVal e de sTipo e 5 �ltimos de sDest e de sBairroZona')
print(sVal.head(3))
print('-----------------------------------')
print(sTipo.head(3))
print('-----------------------------------')
print(sDest.tail(5))
print('-----------------------------------')
print(sBairroZona.tail(5))
print('-----------------------------------')

"""
**** Quest�o 2 ****
Em alguns hor�rios o tipo de transa��o (sTipo) est�  sem valor.
Estes hor�rios devem ser eliminados nas 3 Series (sVal, sTipo, sDest).
"""
print('-----------------------------------')
print('2- 5 primeiros de sDest e 5 �ltimos de sTipo sem tipo ausente')
aus=list(sTipo.loc[sTipo.isnull()].index)
sVal.drop(aus,inplace=True)
sTipo.drop(aus,inplace=True)
sDest.drop(aus,inplace=True)
print(sDest.head(5))
print('-----------------------------------')
print(sTipo.tail(5))
print('-----------------------------------')

"""
**** Quest�o 3 ****
Substituir os valores de transa��o ausentes pelo menor valor 
dos respectivos tipos da transa��o.
�	Por exemplo, o valor ausente em um aluguel de bicicleta,
     deve ser substitu�do pelo menor valor entre os de aluguel.
Caso vc n�o saiba resolver esta quest�o,substitua os valores ausentes de sVal por 999
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
**** Quest�o 4 ****
Coloque as zonas de sBairroZona em letras mai�sculas.
"""
print('-----------------------------------')
print('4- sBairroZona em mai�sculo.')
sBairroZona=sBairroZona.str.upper()
print(sBairroZona)
print('-----------------------------------')

"""
**** Quest�o 5 ****
Qual o valor da menor transa��o? Em quais hor�rios ocorreram?
"""
print('-----------------------------------')
print('5- Menor transa��o e hor�rios em que ocorreram')
print(sVal.min())
print(list(sVal.loc[sVal==sVal.min()].index))
print('-----------------------------------')

"""
**** Quest�o 6 ****
Quantos bairros h� em cada zona? 
"""
print('-----------------------------------')
print('6- Quantidade de bairros em cada zona')
sInv=pd.Series(sBairroZona.index,sBairroZona.values)
gZona=sInv.groupby(level=0)
print(gZona.agg('count'))
print('-----------------------------------')

"""
**** Quest�o 7 ****
Qual hora cheia teve o maior valor m�dio?
   hora cheia: desconsiderar os minutos do hor�rio
"""
print('-----------------------------------')
print('7- Hora cheia com maior valor m�dio')
def hora(x):
    return x[:2]
gHora=sVal.groupby(hora)
print(gHora.agg('mean').idxmax())
print('-----------------------------------')

"""
**** Quest�o 8 ****
Qual o valor mediano das transa��es?
Qual o valor mediano por destino (bairro)?
Qual o valor mediano por hora cheia/tipo de transa��o/destino (bairro)?
"""
print('-----------------------------------')
print('8- Valor mediano das transa��es? E por tipo de transa��o? E por destino(bairro)/hora cheia/tipo de transa��o')
print(sVal.median())
print('-----------------------------------')
gBai=sVal.groupby(sDest)
print(gBai.agg('median'))
print('-----------------------------------')
gTudo=sVal.groupby([hora,sTipo,sDest])
print(gTudo.agg('median'))
print('-----------------------------------')

"""
**** Quest�o 9 ****
Considerando os bairros existentes na sBairroZona,
    liste o nome dos bairros em que n�o houve transa��o.
"""
print('-----------------------------------')
print('9- Bairros sem transa��es')
BairrosCom=list(sDest.unique())
print(list(sBairroZona.drop(BairrosCom).index))
print('-----------------------------------')

"""
**** Quest�o 10 ****
Liste os destinos, sem repeti��o, em que houve transa��es do tipo aluguel.
"""
print('-----------------------------------')
print('10- Bairros com aluguel de bicicleta')
horaAlug=list(sTipo.loc[sTipo=='Aluguel'].index)
destinos=sDest.loc[horaAlug]
print(list(destinos.unique()))
print('-----------------------------------')

"""
**** Quest�o 11 ****
Considerando os seguintes turnos:
    00:00 �s 12:00 - manh�
    12:01 �s 18:00 � tarde
    18:01 �s 23:59 � noite
a) Construa a Series sTurno com o turno das transa��es
b) Mostre graficamente (pizza) a quantidade de transa��es em cada turno
"""
print('-----------------------------------')
print('11- Gr�fico da quantidade de transa��es em cada turno')
sInv=pd.Series(sVal.index,sVal.values)
sAux=sInv.apply(hora)
sTurno=pd.cut(sInv,bins=['0','12','18','23'],labels=['manh�','tarde','noite'],include_lowest=True)
sTurno.value_counts().plot.pie(autopct='%.1f')
plt.show()
print('-----------------------------------')

"""
**** Quest�o 12 ****
Qual o valor total, mediano e m�ximo por tipo de transa��o em cada turno?
"""
print('-----------------------------------')
print('12- Valor total, mediano, m�ximo por tipo de transa��o x turno')
sInv=pd.Series(sTurno.index,sTurno.values)
gTurno=sInv.groupby(level=0)
print(gTurno.agg(['sum','median','max']))
print('-----------------------------------')

"""
**** Quest�o 13 ****
Construa a Series sZona.
Esta Series armazena a Zona de destino da bicicleta de cada transa��o.
Portanto, o index � o hor�rio da transa��o e
          o valor � a Zona de destino considerando o destino(bairro).
"""
print('-----------------------------------')
print('13- Exibir os 5 primeiros e 5 �ltimos de sZona.')
def detZona(bairro,s):
    return s.loc[bairro]
sZona=sDest.apply(detZona,args=(sBairroZona,))
print(sZona.head(5))
print(sZona.tail(5))
print('-----------------------------------')

"""
**** Quest�o 14 ****
Mostre, por zona, o valor total recebido
por alugar as bicicletas e por vend�-las.
"""
print('-----------------------------------')
print('14- Total recebido em aluguel e total recebido em vendas, por zona')
gZonaTipo=sVal.groupby([sZona,sTipo])
print(gZonaTipo.agg('sum'))
print('-----------------------------------')

