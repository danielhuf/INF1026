# -*- coding: utf-8 -*-
import pandas as pd
sCr=pd.read_excel("CrUniv.xlsx",squeeze=True,
                  header=0,
                  usecols=[0,1,3],
                  index_col=[0,1])

# Medidas  'min','max','count','mean','median' por instituição

gInst=sCr.groupby(level=0)
sResI=gInst.agg('min')  # equivalente a sCr.min(level=0)
dResI=gInst.agg(['min','max','count','mean','median'])  


# Quantos Alunos por INSTITUIÇÂo têm média acima 
# da média nacional

def qtAcima(g,mediaNac):
    sfiltro= g>mediaNac     #Series com V/F como values
    return sfiltro.sum()
med=sCr.mean()
sAcimaI= gInst.apply(qtAcima,med)  #  equivalente a (sCr.loc[sCr==med]).sum()

# Alterar o CR dos alunos , acrescentando 10%
# do menor CR da INSTITUIÇÂO 


def alteraCr(g):
    medGrupo= g.min()
    sN= g + 0.1*medGrupo
    sN.loc[sN>10]=10 # alterar os  com nota > 10
    return sN
    
sCrAlt= gInst.apply(alteraCr)   

# outra solução equivalente
sMin= sCr.min(level=0)
sMin=sMin.mul(0.1,fill_value=0)
sCrAlt2=sCr+sMin
sCrAlt2.loc[sCrAlt2>10]=10
#####################################################

# Medidas  'min','max','count','mean','median' por Curso

gInst=sCr.groupby(level=1)
sResC=gInst.agg('min')  # equivalente a sCr.min(level=1)
dResC=gInst.agg(['min','max','count','mean','median'])



#####################################################

# Medidas para aluno do RJ x Não RJ

# Criar uma função para determinar o grupo

def RioNaoRio(x):
    if 'RJ' in x[0]:  # porque tem dois níveis de índice e RJ é do nível 0
        return "RJ"
    else:
        return "DEMAIS"
    
    
gRioFora= sCr.groupby(by=RioNaoRio)
sResRJ=gRioFora.agg('min')
dResRJ=gRioFora.agg(['min','max','count','mean','median'])

#####################################################

# Medidas para alunos com CR  0 a 5, 5 a 8, de 8 a 10

# Criar uma nova series categorizadora com estas classes
# Agrupar por esta series de classes

sClasses=pd.cut(sCr,bins=[0,5,8,10], labels=['reg','med','sup'])
gClasses= sCr.groupby(sClasses)
sResCl=gClasses.agg('min')
dResCl=gClasses.agg(['min','max','count','mean','median'])

#####################################################

# Medidas por Instituição para alunos com CR  0 a 5, 5 a 8, de 8 a 10

# 
# Agrupar por nível 0 e series categorizadora de classes


gInstClasses= sCr.groupby(by=[pd.Grouper(level=0),sClasses])
sResInstCl=gInstClasses.agg('min')
dResInstCl=gInstClasses.agg(['min','max','count','mean','median'])


#####################################################

# Medidas por Curso para alunos com CR  0 a 5, 5 a 8, de 8 a 10

# 
# Agrupar por nível 1 e series categorizadora de classes


gCurtClasses= sCr.groupby(by=[pd.Grouper(level=1),sClasses])
sCurInstCl=gInstClasses.agg('min')
dResCurCl=gCurtClasses.agg(['min','max','count','mean','median'])

#####################################################

