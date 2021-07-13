#1
def contaVogal(texto):
    t=texto.upper()
    dicV={}
    for el in t:
        if el in 'AEIOU':
            dicV[el]=dicV.get(el,0)+1
    return dicV

text='Oi, tudo bem? Sou Daniel!'
print(contaVogal(text))

#2
dicA={}

nome=input('Nome do aluno? ')
while nome!='':
    n1=float(input('Primeira nota? '))
    n2=float(input('Segunda nota? '))
    dicA[nome]=(n1,n2)
    nome=input('Nome do aluno? ')

def media_aluno(nome):
    nota1=dicA[nome][0]
    nota2=dicA[nome][1]
    m=(nota1+nota2)/2
    return m

print(media_aluno('Leo'))

#3
dVogal={'@':'A','&':'E','%':'I','*':'O','$':'U'}

def decodifica(string,dic):
    decod=''
    for el in string:
        if el in '@&%*$':
            decod+=dic[el]
        else:
            decod+=el
    return decod

print(decodifica('B*N&C@',dVogal))

#4
def val_compras(lista,dic):
    valor=0
    for el in lista:
        valor+=dic.get(el,0)
    return valor

lista_de_compras=['biscoito','chocolate','farinha','nescau','farinha']
Supermercado={'amaciante':4.99,'arroz':10.90,'biscoito':1.69,
              'café':6.98,'chocolate':3.79,'farinha':2.99}

print(val_compras(lista_de_compras,Supermercado))

#5
def mutuo(dic):
    l_pares=[]
    for el in dic:
        correspondente=dic[el]
        if dic[correspondente]==el and (correspondente,el) not in l_pares:
            par=(el,correspondente)
            l_pares.append(par)
    return l_pares

dicA={'Leo':'Sofia','Marcos':'Andreia','Sofia':'Leo',
      'Alex':'Andreia','Andreia':'Marcos'}

print(mutuo(dicA))

#6
dicSignos={0:'Macaco',1:'Galo',2:'Cão',3:'Porco',4:'Rato',5:'Boi',6:'Tigre',
           7:'Coelho',8:'Dragão',9:'Serpente',10:'Cavalo',11:'Carneiro'}

dicDatas={'Daniel':'12/07/2002','Ilana':'24/12/1968','Flavio':'23/10/1968'}

def mostraSigno(dicS,dicD):
    for el in dicD:
        data=dicD[el]
        ano=int(data[6:])
        num=ano%12
        signo=dicSignos[num]
        print('%s - signo %s'%(el,signo))
    return

mostraSigno(dicSignos,dicDatas)
  
#7
telefones={}

def incluirNovoNome(nome,tel):
    if type(tel) is list:
        telefones[nome]=tel
    else:
        telefones[nome]=[tel]
    return

def incluirTelefone(nome,tel):
    if nome in telefones:
        telefones[nome].append(tel)
    else:
        resp=input('Você deseja incluir esse nome? ')
        if resp=='Sim':
            incluirNovoNome(nome,tel)
    return

def excluirTelefone(nome,tel):
    if len(telefones[nome])==1:
        del telefones[nome]
    else:
        telefones[nome].remove(tel)
    return

def excluirNome(nome):
    del telefones[nome]
    return

def consultarTelefone(nome):
    tel=telefones[nome]
    return tel

incluirNovoNome('Daniel',[7878,666])
incluirTelefone('Daniel',122)
incluirTelefone('Leo',44)
excluirNome('Leo')
print(telefones)
print(consultarTelefone('Daniel'))
tel2={'Daniel':[346,827],'Juan':[111]}

#Possibilidade 1
telefones.update(tel2)
print(telefones)

#Possibilidade 2
for el in tel2:
    if el in telefones:
        for numero in tel2[el]:
            telefones[el].append(numero)
    else:
        telefones[el]=tel2[el]
print(telefones)

#8
#Farei uma função que conta as ocorrencias e cria um dicionario
#retornarei a lista de chaves

def unicos(lista):
    dic={}
    nova=[]
    for el in lista:
        dic[el]=dic.get(el,0)+1
    for i in dic:
        nova.append(i)
    return nova

l=[1,1,2,4,5,2,1,2,2,100,80,100]
print(unicos(l))

#9
unidades={0:'',1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX'}
dezenas={0:'',1:'X',2:'XX',3:'XXX',4:'XL',5:'L',6:'LX',7:'LXX',8:'LXXX',9:'XC'}
centenas={0:'',1:'C',2:'CC',3:'CCC',4:'CD',5:'D',6:'DC',7:'DCC',8:'DCCC',9:'CM'}

def converte(n,dicU,dicD,dicC):
    centena=n//100
    dezena=(n%100)//10
    unidade=(n%100)%10
    romano=dicC[centena]+dicD[dezena]+dicU[unidade]
    return romano

print(converte(987,unidades,dezenas,centenas))

#10
dicPontos={}
dicDescri={}
placa=input('Placa do carro? ')
while placa!='':
    local=input('Local? ')
    grau=int(input('Grau da infração? '))
    descri=input('Descrição da infração? ')
    dicPontos[placa]=dicPontos.get(placa,0)+grau
    dicDescri[placa]=dicDescri.get(placa,[])+[descri]
    placa=input('Placa do carro? ')

for el in dicPontos:
    if dicPontos[el]>=20:
        print('Placa do carro - %s'%el)
        print('Infrações -',dicDescri[el])

#11
def freqPalavras(string):
    dicP={}
    lista=string.split()
    for el in lista:
        dicP[el]=dicP.get(el,0)+1
    return dicP

print(freqPalavras('dinheiro é dinheiro e vice versa'))

#12
#Está mal formulada

#13
def totalDaCompra(dicP,mercado,dicC):
    valor=0
    for el in dicC:
        valor+=dicP[mercado][el]*dicC[el]
    return valor

def criaDicMercadosDoProd(dicMercados):
    dicProdutos={}
    for mercado in dicMercados:
        for produto in dicMercados[mercado]:
            dicAuxiliar=dicProdutos.get(produto,{})
            dicAuxiliar[mercado]=float(dicMercados[mercado][produto])
            dicProdutos[produto]=dicAuxiliar
    return dicProdutos

dProdsDoMerc= {'Qbarato': {'biscoito': 4.3, 'leite': 3.2, 'suco': 7.1, 'chocolate': 6.4,
'detergente': 3.2, 'cerveja': 6.4, 'manteiga': 8.7},
               'UltraK': {'biscoito': 3.5, 'leite': 3.3, 'suco': 8.9, 'chocolate': 6.9,
'detergente': 4.2, 'cerveja': 6.4, 'manteiga': 8.7},
               'Market': {'biscoito': 4.5, 'leite': 3.2, 'suco': 7.5, 'chocolate': 6.6,
'detergente': 3.8, 'cerveja': 6.5, 'manteiga': 9.2},
               'Preferido':{'biscoito': 4.65, 'leite': 3.4, 'suco': 8.1, 'chocolate': 8.1,
'detergente': 3.3, 'cerveja': 6.5, 'manteiga': 8.9},
               'Escolhido': {'biscoito': 5.2, 'leite': 3.3, 'suco': 8.3, 'chocolate': 7.5,
                             'detergente': 3.9,'cerveja': 6.4, 'manteiga': 8.6}
                }


dCompras={'biscoito':2,'leite':6,'chocolate':1}

print(totalDaCompra(dProdsDoMerc,'Qbarato',dCompras))
print(criaDicMercadosDoProd(dProdsDoMerc))

#14
def alunos(dicC,dicA):
    for el in dicA:
        nome=el
        curso=dicA[el][0]
        dia=dicC[curso][0]
        posicao=dicA[el][1]
        vagas=dicC[curso][1]
        if posicao<=vagas/4:
            hora='8h às 11:30h'
        elif posicao<=vagas/2:
            hora='12h às 13:30h'
        elif posicao<=0.75*vagas:
            hora='14h às 15:30h'
        else:
            hora='16h às 17:30h'
        print('Nome: %s - Curso: %s - Dia: %s - Hora: %s'%(nome,curso,dia,hora))
    return

dicCursos={'Engenharia':['24/03',50],'Direito':['18/02',70]}
dicAprov={'Daniel':['Engenharia',7],'Leo':['Direito',68]}

alunos(dicCursos,dicAprov)

#15
#O mapa terá 10 linhas e 10 colunas
dEmbarc={'S':['submarino',3,30],'D':['detroyer',5,50],'C':['cruzador',7,100]}
dLoc={(2,2):'S',(2,3):'S',(2,4):'S',
      (5,5):'D',(5,6):'D',(5,7):'D',(5,8):'D',(5,9):'D',
      (3,1):'C',(4,1):'C',(5,1):'C',(6,1):'C',(7,1):'C',(8,1):'C',(9,1):'C'}

def batalhaNaval(dE,dL):
    pontos=0
    c=input('Coordenadas? ')
    lc=c.split(',')
    c1=int(lc[0])
    c2=int(lc[1])
    coord=(c1,c2)
    while coord!=(-1,-1):
        if coord in dLoc:
            letra=dLoc[coord]
            embarc=dEmbarc[letra][0]
            print('Acertou %s!\n'%embarc)
            del dLoc[coord]
            if letra not in dLoc.values():
                p=dEmbarc[letra][2]
                pontos+=p
                print('Embarcação destruída! %d pontos obtidos'%p)
        else:
            print('Água\n')
        if dLoc=={}:
            print('Você venceu! Pontuação: %d'%pontos)
            return
        c=input('Coordenadas? ')
        lc=c.split(',')
        c1=int(lc[0])
        c2=int(lc[1])
        coord=(c1,c2)
    print('Você desistiu! Pontuação: %d'%pontos)
    return

batalhaNaval(dEmbarc,dLoc)
    

