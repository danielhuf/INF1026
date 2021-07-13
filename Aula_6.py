dictPortIngles={'um':'one','dois':'two','tres':'three'}

dicInscr={'1732282':['INF1111','MAT5555'],'1922929':['INF9888']}

print('um' in dictPortIngles)

print(dicInscr['1732282'])

dictPortIngles['amor']='love'

print(dictPortIngles)

dd={'a':'A','e':'E'}

print(dd.get('a','sem correspondente'))
print(dd.get('o','sem correspondente'))

#criei uma função que cria um dicionario de ocorrências
def ocorrencia(st):
    docor={}
    for c in st:
        docor[c]=docor.get(c,0)+1
    return docor

print(ocorrencia('banana'))

dic={'LALA':{'G1':5.6,'G2':8.4},
     'DUDU':{'G1':3.2,'G2':4.4},
     'PEPE':{'G1':8.3,'G2':7.4}
     }

print(dic)
print(dic['DUDU'])
print(dic['LALA']['G2'])

d1={'oi':'hello'}
d2={'oi':'olaa','tchau':'bye'}
d1.update(d2)
print(d1)

