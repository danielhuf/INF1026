#Exercicios Mercados e Produtos
#NOME: Daniel Stulberg Huf
#TURMA: 33C
#PROFESSOR: Joísa

#EX1.A)
def criaDicProdsPorMercado(arquivo):
    dic={}
    arq=open(arquivo,'r')
    linha=arq.readline()
    l_produtos=(linha.strip().split(';'))
    for l in arq:
        dic_produtos={}
        li=l.strip().split(';')
        mercado=li[0]
        tam=len(li)
        for i in range(1,tam):
            dic_produtos[l_produtos[i]]=float(li[i])
        dic[mercado]=dic_produtos
    arq.close()
    return dic

#EX1.B)
def totalDaCompra(dicP,mercado,dicC):
    valor=0
    for el in dicC:
        valor+=dicP[mercado][el]*dicC[el]
    return valor

#EX 1.C)
def criaDTotalDaCompra(dicP,dicC):
    novo={}
    for mercado in dicP:
        total=totalDaCompra(dicP,mercado,dicC)
        novo[mercado]=total
    return novo

#EX 1.D)
def criaDicMercadosPorProd(dicMercados):
    dicProdutos={}
    for mercado,produto in dicMercados.items():
        for p in produto:
            dicAuxiliar=dicProdutos.get(p,{})
            dicAuxiliar[mercado]=float(produto[p])
            dicProdutos[p]=dicAuxiliar
    return dicProdutos

#EX 1.E)
def criaDicMinimo(dic):
    novo={}
    for produto,mercados in dic.items():
        l_mercados_min=[]
        l_precos=list(mercados.values())
        minimo=l_precos[0]
        for i in range(1,len(l_precos)):
            if l_precos[i]<minimo:
                minimo=l_precos[i]
        for mercado,preco in mercados.items():
            if preco==minimo:
                l_mercados_min.append(mercado)
        novo[produto]={minimo:l_mercados_min}
    return novo
    
print('\n------------- Teste do Ex A -------------------')
dpm = criaDicProdsPorMercado('MercadosProdutos.csv')
print(dpm)

dCompras={'biscoito':2, 'leite':6, 'chocolate':1}

print('\n------------- Teste do Ex B -------------------')
print('\nDicionario das compras')
print(dCompras)
print('\nTotal das compras no mercado Qbarato')
total = totalDaCompra(dpm,'Qbarato',dCompras)
print(total)

print('\n------------- Teste do Ex C -------------------')
d=criaDTotalDaCompra(dpm,dCompras)
print('\nDicionario com totais das compras nos mercados')
print(d)

print('\n------------- Teste do Ex D -------------------')
dmp= criaDicMercadosPorProd(dpm)
print(dmp)

print('\n------------- Teste do Ex E -------------------')
dmenor=criaDicMinimo(dmp)
print(dmenor)




