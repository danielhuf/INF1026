for i in range(5):
    print(i)
   
#1
def somaLidos():
    n_impar=0
    s_impar=0
    num=int(input('Escreva um número inteiro: '))
    while num>=0:
        if num%2 != 0:
            n_impar+=1
            s_impar+=num
        num=int(input('Escreva um número inteiro: '))
    print('Quantidade de números ímpares lidos:',n_impar)
    print('Soma dos números ímpares:',s_impar)
    return

somaLidos()

#2
def posicaoVogais(string):
    for (pos,el) in enumerate(string):
        if el in 'AEIOU':
            print(el+' na posiçâo '+str(pos))
    return

posicaoVogais('AmAo')

#3
def semVogais(string):
    nova=''
    for el in string:
        nova+=el.upper()
    result=''
    for el in nova:
        if el not in 'AEIOU':
            result+=el
    return result

s='oi tudo bemm?'
print(semVogais(s))

#4
def somaParesLista(lista):
    soma=0
    for el in lista:
        if type(el) is int and el%2 == 0:
            soma+=el
        elif type(el) is list:
            s=somaParesLista(el)
            soma+=s
    return soma

l=[1,6,[2,2],[1,3],4]
print(somaParesLista(l))

#5
def ocorrencias(string,letra):
    l=[]
    for (pos,el) in enumerate(string):
        if el==letra:
            l.append(pos)
    return l

print(ocorrencias('arara','a'))

#6
def copiaAmenosB(lista_1,lista_2):
    l=[]
    for el in lista_1:
        if el not in lista_2:
            l.append(el)
    return l

l1=[1,1,4,7,'s','i']
l2=[4,7,'s']

print(copiaAmenosB(l1,l2))

#7
def AmenosB (lista_1,lista_2):
    pos=0
    while pos<len(lista_1):
        if lista_1[pos] in lista_2:
            lista_1.remove(lista_1[pos])
            pos-=1
        pos+=1
    print(lista_1)
    print(lista_2)
    return

l1=[1,2,'i',4,4,5,['u',8]]
l2=[1,4,['u',8]]

AmenosB(l1,l2)

#8
def exibeResultanteOrdenada_1(lista_1,lista_2):
    nova=[]
    for el in lista_1:
        nova.append(el)
    for el in lista_2:
        nova.append(el)
    nova.sort()
    return nova

#A de baixo não está dando certo!
def exibeResultanteOrdenada_2(lista_1,lista_2):
    nova=[]
    for el in lista_1:
        nova.append(el)
    for el in lista_2:
        if el<nova[0]:
            nova.insert(0,el)
        if el>nova[len(nova)-1]:
            nova.insert(len(nova)-1,el)
        for (pos,i) in enumerate(nova):
            if el>=i and el<=nova[pos+1]:
                nova.insert(pos,el)   
    return nova

l1=[12,15,15,26,28,34,40]
l2=[10,20,26,30,32,38]

print(exibeResultanteOrdenada_2(l1,l2))
        
        
        
        
        
