# -*- coding: utf-8 -*-
"""
Created on Tue May 19 21:43:55 2020

@author: lcam
"""

import pandas as pd
import numpy as np
 

d2={
    'Nome': ['Alisa', 'Bobby', 'Cathrine', 'Alisa', 'Bobby', 'Cathrine', 'Alisa', 'Bobby', 'Cathrine', 
             'Alisa', 'Bobby', 'Cathrine'], 
    'Período': ['Semestre 1', 'Semestre 1', 'Semestre 1', 'Semestre 1', 'Semestre 1', 'Semestre 1', 
                'Semestre 2', 'Semestre 2', 'Semestre 2', 'Semestre 2', 'Semestre 2', 'Semestre 2'], 
    'Matéria': ['Matemática', 'Matemática', 'Matemática', 'Ciência', 'Ciência', 'Ciência', 
                'Matemática', 'Matemática', 'Matemática', 'Ciência', 'Ciência', 'Ciência'], 
    'Média': [8, 7, 2, 6, 4, 8, 9, 4, 3, 7, 7, 4.4], 
    'Situação': ['AP', 'AP', 'RP', 'AP', 'RP', 'AP', 'AP', 'RP', 'RP', 'AP', 'AP', 'RP']}
 
sNom = pd.Series(d2['Nome'])
sPer = pd.Series(d2['Período'])
sDis = pd.Series(d2['Matéria'])
sMed = pd.Series(d2['Média'])
sSit = pd.Series(d2['Situação'])

# Quantos aprovados/reprovado por MatériaxPeríodo?

print(pd.crosstab(sDis,sSit,rownames=['Disc'],colnames=['Sit']))

# Quantos aprovados/reprovado por MatériaxPeríodo e respectivos totais?
print(pd.crosstab(sDis,sSit,rownames=['Disc'],colnames=['Sit'],margins=True,margins_name='Tot'))

# Qual o percentual de aprovados/reprovado por MatériaxPeríodo e respectivos totais?
print(pd.crosstab(sDis,sSit,rownames=['Disc'],colnames=['Sit'],margins=True,margins_name='Tot',normalize=True))

# Qual a nota média de aprovados/reprovado por MatériaxPeríodo e respectivos totais?
print(pd.crosstab(sDis,sSit,rownames=['Disc'],colnames=['Sit'],values=sMed,aggfunc='mean'))

#Quando quero mais de um indice
print(pd.crosstab(index=[sDis,sPer],columns=sSit,rownames=['Disc','Per'],colnames=['Sit'],values=sMed,aggfunc='mean'))
