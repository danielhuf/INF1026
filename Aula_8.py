#Dicionário de dicionários

dBio={'LALA':{'SEXO':'F','ALT':1.54,'PESO':40},
      'HUGUINHO':{'SEXO':'M','ALT':1.70,'PESO':68},
      'LELE':{'SEXO':'F','ALT':1.61,'PESO':55},
      'LALA':{'SEXO':'F','ALT':1.81,'PESO':88}
      }

print(dBio['LELE'])

print(dBio['HUGUINHO']['ALT'])

#construir e retornar um dicionário em que cada elemento é:
#FARMACIA: valor total da compra nessa farmacia

def constroiDicFarmaTotal(dfarm,lcomp):
    dFarmTotal={}
    for farmacia in dfarm:
        dFarmTotal[farmacia]=0
        for item in lcomp:
            dFarmTotal[farmacia]+=item[1]*dfarm[farmacia][item[0]]
    return dFarmTotal

dFarma={'FARMYY':{'asp':4.75,'tux':16.38,'aal':34.82,'dig':26.56},
        'QDroga':{'asp':3.75,'tux':12.24,'aal':42.57,'dig':28.45},
        'DODOI':{'asp':6.75,'tux':19.38,'aal':24.82,'dig':18.56},
        }

lcompras=[('asp',2),('dig',1)]

print(constroiDicFarmaTotal(dFarma,lcompras))
