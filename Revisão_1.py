#1
def maiorElemento(lista):
    for el in lista:
        maiorEl=el
    for el in lista:
        if el>maiorEl:
            maiorEl=el
    return maiorEl

def somaElementos(lista):
    soma=0
    for el in lista:
        soma+=el
    return soma

def ocorrePrimeiro(lista):
    ocorrenciaPrimeiro=0  
    for el in lista:
        if el==lista[0]:
            ocorrenciaPrimeiro+=1
    return ocorrenciaPrimeiro

def mediaReal(lista):
    soma=somaElementos(lista)
    num=0
    for el in lista:
        num+=1
    media=soma/num
    return media

def valorProximo(lista):
    med=mediaReal(lista)
    for el in lista:
        val_mais_proximo=abs(el-med)
        item=el
    for el in lista:
        if abs(el-med)<val_mais_proximo:
            val_mais_proximo=abs(el-med)
            item=el
    return item

def somaNegativos(lista):
    soma=0
    for el in lista:
        if el<0:
            soma+=el
    return soma

def vizinhosIguais(lista):
    viz=0
    pos=0
    while pos<len(lista)-1:
        if lista[pos]==lista[pos+1]:
            viz+=1
        pos+=1
    return viz

print(vizinhosIguais([1,-2,-2,3,1,5,5,5]))

#2
def traduzir(lSecreta):
    string=' abcdefghijklmnopqrstuvwxyz'
    decod=''
    for el in lSecreta:
        decod+=string[el]
    return decod

l=[2,15,13,0,4,9,1]
t=traduzir(l)
print(t)

#3
def busca(valor,lista):
    for (pos,el) in enumerate(lista):
        if el[0]==valor:
            return pos
    return None
    
l_campeonato=[['Brasil','Italia',[10,9]],['Brasil','Espanha',[5,7]],['Italia','Espanha',[7,8]]]
total_faltas=0
for el in l_campeonato:
    falta=el[2][0]+el[2][1]
    total_faltas+=falta
print('Total de faltas do campeonato = %d'%total_faltas)

l_Faltas=[]
for jogo in l_campeonato:
    for i in range(2):
        pos=busca(jogo[i],l_Faltas)
        if pos==None:
            l_Faltas.append([jogo[i],jogo[2][i]])
        else:
            l_Faltas[pos][1]+=jogo[2][i]

maisfaltas=l_Faltas[0][1]
menosfaltas=l_Faltas[0][1]
time_mais=l_Faltas[0][0]
time_menos=l_Faltas[0][0]
for el in l_Faltas[1:]:    #nao preciso perguntar para o primeiro
    if el[1]>maisfaltas:
        maisfaltas=el[1]
        time_mais=el[0]
    elif el[1]<menosfaltas:
        menosfaltas=el[1]
        time_menos=el[0]

print('Time com mais faltas',time_mais)
print('Time com menos faltas',time_menos)

#4
def media(lista):
    soma=somaElementos(lista)
    num=0
    for el in lista:
        num+=1
    media=soma/num
    return media

lista=[2.5,7.5,10.0,4.0]
m=media(lista)
val_prox=abs(lista[0]-m)
num=lista[0]
for el in lista:
    dif_media=abs(el-m)
    if dif_media<val_prox:
        val_prox=dif_media
        num=el
        
print('Valor mais próximo da média:',num)

#5
def ocorrencia(lNumeros,valor):
    if lNumeros==[]:
        return -2
    else:
        for (pos,el) in enumerate(lNumeros):
            if type(el) is int or type(el) is float:
                if el==valor:
                    return pos
            elif type(el) is list:
                for i in el:
                    if i==valor:
                        return pos
        return -1
    
lista=[1,2,3,[1,3,4,4],5,6,4,7]
l=[]
val=10
print(ocorrencia(l,val))
            
#6
def megasena(result,l_dados):
    l_ganha=[]
    for el in l_dados:
        if el[1]==result:
            l_ganha.append(el[0])
    return l_ganha

lista=[[1,123],[7,978],[3,978]]
r=978
print(megasena(r,lista))

#7
def busca(valor,lista):
    for(pos,el) in enumerate(lista):
        if valor==el[0]:
            return pos
    return None

lIngr=[['Arroz',100,5.00],['Carne',100,16.00],['Batata Inglesa',250,3.50],['Cenoura',100,3.00],['Queijo Minas',150,12.00]]
lPratos=[['Muito Escondidinho',['Batata Inglesa',3],['Queijo Minas',1],['Cenoura',1]],['Pastelão de Vento',['Batata Inglesa',4],['Carne',1]]]
lConsumo=[['Muito Escondidinho',12],['Pastelão de Vento',30]]
l_preco_porc_ing=[]
l_mercado=[]

#primeiro, irei calcular o preço de cada porção dos ingredientes
for (pos,el) in enumerate(lIngr):
    custo_porc=((lIngr[pos][1])/1000)*lIngr[pos][2]
    l_preco_porc_ing.append([lIngr[pos][0],custo_porc])

maior_custo=-1
pratomaiscaro=''
for el in lPratos:
    nome_prato=el[0]
    custo=0
    for i in el[1:]:
        pos=busca(i[0],l_preco_porc_ing)
        custo+=i[1]*l_preco_porc_ing[pos][1]
    print('%s = R$%.2f'%(nome_prato,custo))
    if custo>maior_custo:
        maior_custo=custo
        pratomaiscaro=nome_prato
print('Prato mais caro:',pratomaiscaro)

#l_mercado é a lista com os produtos e o número de porções total
for el in lConsumo:
    pos=busca(el[0],lPratos)
    for i in lPratos[pos][1:]:
        produto=busca(i[0],l_mercado)
        if produto==None:
            l_mercado.append([i[0],i[1]*el[1]])
        else:
            l_mercado[produto][1]+=i[1]*el[1]

for el in l_mercado:
    pos=busca(el[0],lIngr)
    quant=lIngr[pos][1]*el[1]
    quant_kilo=quant/1000
    print('Quantidade de',el[0],'a ser comprada =',quant_kilo,'kg')
