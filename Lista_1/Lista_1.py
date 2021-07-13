#1
'''
def presente (val_caixa,val_presente):
    if val_presente>0.8*val_caixa:
        parcela=5
        val_parcela=(1.1*val_presente)/5
    elif val_presente>0.5*val_caixa:
        parcela=3
        val_parcela=(1.08*val_presente)/3
    else:
        parcela=1
        val_parcela=0.95*val_presente
    return (parcela,val_parcela)

print(presente(510,1000))

#2
def ordena(a,b,c):
    l=[]
    l.append(a)
    l.append(b)
    l.append(c)
    l.sort()
    t=tuple(l)
    return t

def nota(a):
    l_dados=[]
    arq=open(a,'r')
    for linha in arq:
        linha=linha.strip()
        dados=linha.split(';')
        l_dados.append(dados)
    arq.close()
    for el in l_dados:
        el[1]=float(el[1])
        el[2]=float(el[2])
        el[3]=float(el[3])
        el[4]=float(el[4])
        el[5]=float(el[5])
        el[6]=float(el[6])
    for el in l_dados:
        original=ordena(el[1],el[2],el[3])
        beleza=ordena(el[4],el[5],el[6])
        nota=0.6*original[1]+0.4*beleza[1]
        print(el[0],'nota',nota)
    return

print(nota('fantasias.txt'))

#3
def convertesegundo(s):
    horas=s//3600
    minutos=(s%3600)//60
    segundos=(s%3600)%60
    return(horas,minutos,segundos)
    
def maratona(a):
    l_dados=[]
    arq=open(a,'r')
    for linha in arq:
        linha=linha.strip()
        dados=linha.split('\t')
        l_dados.append(dados)
    arq.close()
    for el in l_dados:
        el[1]=int(el[1])
        tempo=convertesegundo(el[1])
        print('%s - %dh %dm %ds'%(el[0],tempo[0],tempo[1],tempo[2]))
        if el[1]>36000:
            print('DESCLASSIFICADO')
    t_menor=l_dados[0][1]
    t_maior=l_dados[0][1]
    a_menor=l_dados[0][0]
    a_maior=l_dados[0][0]
    for el in l_dados:
        if el[1]<t_menor:
            t_menor=el[1]
            a_menor=el[0]
        if el[1]>t_maior:
            t_maior=el[1]
            a_maior=el[0]
    tempo_menor=convertesegundo(t_menor)
    tempo_maior=convertesegundo(t_maior)
    print('Menor tempo: %s com %dh %dm %ds'%(a_menor,tempo_menor[0],tempo_menor[1],tempo_menor[2]))
    print('Maior tempo: %s com %dh %dm %ds'%(a_maior,tempo_maior[0],tempo_maior[1],tempo_maior[2]))       
    return

print(maratona('maratona.txt'))

#4
def ehPerfeito(n):
    l_divisores=[]
    inicio=1
    while inicio<n:
        if n%inicio==0:
            l_divisores.append(inicio)
        inicio+=1
    soma_div=0
    for el in l_divisores:
        soma_div+=el
    if n==soma_div:
        perfeito=True
    else:
        perfeito=False
    return(perfeito,l_divisores)
    
def avaliaNumero(n):
    a=ehPerfeito(n)
    divisores=a[1]
    print('Número',n,'com divisores',divisores)
    if a[0]==True:
        print('É perfeito')
    else:
        print('Não é perfeito')
    return

avaliaNumero(28)

#5
def contaElementos(t):
    n=0
    for el in t:
        if type(el) is int:
            n+=1
        elif type(el) is list or type(el) is tuple:
            s=contaElementos(el)
            n+=s
    return n

tup=([1,2],'a',7.3,3,(10,20),[1,(2.3,5)])
print(contaElementos(tup))

#6
def testaContida(t):
    tem=0
    if type(t) is str:
        if 'oi' in t:
            tem+=1
    elif type(t) is list or type(t) is tuple:
        for el in t:
            s=testaContida(el)
            tem+=s
    if tem>0:
        return True
    else:
        return False
    
tup=([1,2,3],([9,'oi']))
print(testaContida(tup))

#7
def conta(t,string):
    cont=0
    for el in t:
        if type(el) is str:
            if string in el:
                cont+=1
        elif type(el) is list or type(el) is tuple:
            s=conta(el,string)
            cont+=s
    return cont

print(conta(('foi',[1,'oi'],9),'oi'))

#8
def temperatura(t):
    l_meses=['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    soma_t=0
    for el in t:
        soma_t+=el
    t_media=soma_t/len(t)
    menor_t=t[0]
    menor_mes=l_meses[0]
    maior_t=t[0]
    maior_mes=l_meses[0]
    for (pos,el) in enumerate(t):
        if el>t_media:
            print(l_meses[pos],'-',el,'graus')
        if el<menor_t:
            menor_t=el
            menor_mes=l_meses[pos]
        if el>maior_t:
            maior_t=el
            maior_mes=l_meses[pos]
    return ([menor_t,menor_mes],[maior_t,maior_mes])

tup=(23,24,25,32,29,30,39,17,18,20,22,28)
print(temperatura(tup))

#9
def organiza(t):
    dif=abs(t[0][1]-t[1][1])
    baixo=t[0][0]
    alto=t[1][0]
    if t[0][1]>t[1][1]:
        baixo=t[1][0]
        alto=t[0][0]
    return (dif,(alto,baixo))

print(organiza((('Zozó',100),('Zazá',190))))

primeiro_dia=[]
segundo_dia=[]
num=int(input('Informe o número da dupla: '))
while num!=0:
    int_1=input('Primeiro Integrante: ')
    alt_1=float(input('Altura do Integrante em cm: '))
    int_2=input('Segundo Integrante: ')
    alt_2=float(input('Altura do Integrante em cm: '))
    tupla=((int_1,alt_1),(int_2,alt_2))
    dados=organiza(tupla)
    if dados[0]<=15:
        primeiro_dia.append((num,dados[1][0],dados[1][1]))
    else:
        segundo_dia.append((num,dados[1][0],dados[1][1]))
    num=int(input('Informe o número da dupla: '))
        
lista_geral=[primeiro_dia,segundo_dia]
print(lista_geral)

#10
def um_sensor(a,num):
    l_dados=[]
    arq=open(a,'r')
    for linha in arq:
        linha=linha.strip()
        dados=linha.split(';')
        dados[0]=int(dados[0])
        if dados[0]==num:
            l_dados.append([int(dados[1]),float(dados[2]),float(dados[3])])
    arq.close()
    menor_t=l_dados[0][1]
    menor_hora_t=l_dados[0][0]
    menor_u=l_dados[0][2]
    menor_hora_u=l_dados[0][0]
    for el in l_dados:
        if el[1]<menor_t:
            menor_t=el[1]
            menor_hora_t=el[0]
        if el[2]<menor_u:
            menor_u=el[2]
            menor_hora_u=el[0]
    return (num,(menor_t,menor_hora_t),(menor_u,menor_hora_u))

sensor=1
while sensor<7:
    info=um_sensor('Registros.txt',sensor)
    print('Sensor %d - Temperatura Mínima %.2f graus Celsius às %dh e Umidade Mínima: %.2f%% às %dh'%(sensor,info[1][0],info[1][1],info[2][0],info[2][1]))
    sensor+=1
#Segunda parte mal formulada!!
'''
#11
#irei estabelecer m como 100 e n como 80

def sorteados(cartela):
    n=0
    for el in cartela:
        if el[1]==1:
            n+=1
    return n

def checa(lugar,cartela):
    for el in cartela:
        if el[0]==lugar and el[1]==0:
            return True
    return False

#não farei a do lateral
#nao farei a das linhas livres

def vencedor(jogo):
    l_jogadores_pontos=[]
    for el in jogo:
        pontos=0
        nome=el[0]
        for cartela in el[1]:
                pontos+=cartela[1]
        l_jogadores_pontos.append([nome,pontos])
    l_vencedores=[]
    maior_pontos=0
    for el in l_jogadores_pontos:
        if el[1]>maior_pontos:
            maior_pontos=el[1]
    for el in l_jogadores_pontos:
        if el[1]==maior_pontos:
            l_vencedores.append(el[0])
    return l_vencedores

exemplo=[('José',(((2,3,18),1),((4,1,27),0))),('Aron',(((6,3,60),0),((4,2,35),1)))]

print(vencedor(exemplo))
        

#12
#Igual à 10
    
