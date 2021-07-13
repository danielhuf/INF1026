#Daniel Huf
#mat. 1920468

def minmax(lista):
    menor_val=lista[0]
    maior_val=lista[0]
    cont_menor=0
    cont_maior=0
    for el in lista:
        if el<menor_val:
            menor_val=el
        if el>maior_val:
            maior_val=el
    for el in lista:
        if el==menor_val:
            cont_menor+=1
        if el==maior_val:
            cont_maior+=1
    return ((menor_val,cont_menor),(maior_val,cont_maior))

#OUTRA OPÇÃO MAIS EFICIENTE

def minMax(ls):
    minimo=maximo=ls[0]
    ocmin=ocmax=1
    for i in range (1,len(ls)):
        if ls[i]==minimo:
            ocmin+=1
        elif ls[i]<minimo:
            minimo=ls[i]
            ocmin=1
        elif ls[i]==maximo:
            ocmax+=1
        elif ls[i]>maximo:
            maximo=ls[i]
            ocmax=1
    return ((minimo,ocmin),(maximo,ocmax))

l=[3,8,10,8,10,1,2,1,1]
print(minMax(l))
