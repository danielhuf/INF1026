#1
def somaFracao(t1,t2):
    denominador=t1[1]*t2[1]
    return ((denominador/t1[1])*t1[0]+(denominador/t2[1])*t2[0],denominador)

print(somaFracao((2,3),(4,5)))

#2
def maiorDivComum(a,b):
    if a>b:
        b,a=a,b
    while b!=0:
        a,b=b,a%b
    return a

def simplificaFracao(t):
    mdc=maiorDivComum(t[0],t[1])
    return(int(t[0]/mdc),int(t[1]/mdc))

print(simplificaFracao((20,48)))

#3
def exibeNoFormatoFracao(fr):
    print('\nFração:%d/%d'%(fr[0],fr[1]))
    return

exibeNoFormatoFracao((3,5))
exibeNoFormatoFracao((7,8))

#4
def multiplos3e7(a,b):
    simult=0
    num_simult=[]
    inicio=a
    final=b
    if inicio>final:
        inicio=b
        final=a
    while inicio<=final:
        if inicio%21==0:
            simult+=1
            num_simult.append(inicio)
        inicio+=1
    t=tuple(num_simult)
    return (simult,t)

print(multiplos3e7(30,11))
print(multiplos3e7(10,50))

#5
def ImpostoPlus(val_compra,val_venda):
    lucro=val_venda-val_compra
    if lucro<0.1*val_compra:
        imposto=(2/100)*lucro
    elif lucro>=0.5*val_compra:
        imposto=0.4*lucro
    elif lucro>=0.3*val_compra:
        imposto=0.2*lucro
    elif lucro>=0.1*val_compra:
        imposto=(5/100)*lucro
        
    if imposto<500:
        parcela=1
    elif imposto<2000:
        parcela=2
    else:
        parcela=4
    val_parcela=imposto/parcela
    return (imposto,parcela,val_parcela)

print(ImpostoPlus(10,50))

#6
def antesDe(t1,t2):
    if t1[0]>t2[0]:
        return False
    elif t1[0]==t2[0]:
        if t1[1]>=t2[1]:
            return False
    return True

def depoisDe(t1,t2):
    if t1[0]<t2[0]:
        return False
    elif t1[0]==t2[0]:
        if t1[1]<=t2[1]:
            return False
    return True

print(antesDe((18,16),(16,16)))    
print(depoisDe((18,16),(16,16)))

#7    
def entradaNoIntervalo(t,inicio,fim):
    entraram=0
    l_placas=[]
    for el in t:
        if antesDe(inicio,el[1])==True and depoisDe(fim,el[1])==True:
            entraram+=1
            l_placas.append(el[0])
    tup=tuple(l_placas)
    return (entraram,tup)
    
tcarros=(('LCG1122', (13,45)),('XON2323', (15,45)),('LAB3456', (11,22)),('KRS3333', (21,10)),('OTV9876', (19,23)),('KTU1876', (16,30)),('LBZ4321', (12,14)),('KOX5656', (10,20)))
 
print(entradaNoIntervalo(tcarros,(13,30),(17,10)))