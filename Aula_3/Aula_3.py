t=(1,[2],3,2)
t[1][0]=5
print(t)

tt=('a',13,[22,50],'ola',(10,25))
#Eu nao posso alterar os valores da tupla, mas posso alterar dentro da lista da tupla

a=(1,)
print(a)

tupla=(1,2,3,4)
for (i,el) in enumerate(tupla):
    print(el,'está na posição',i)
    
T1=(10,20,30)
T2=3*T1
print(T2)
print(T1[-1::-1])

def periodoEvento(tempohoras):
    dias=tempohoras//24
    h=tempohoras%24
    return (dias//7,dias%7,h)

(semana,dias,horas)=periodoEvento(458)
#ou iguala o de cima a uma letra e depois referencia letra[0], letra[1] etc...
print('O evento durou %d semanas, %d dias e %d horas.'%(semana,dias,horas))

n1=int(input('Valor 1? '))
n2=int(input('Valor 2? '))

if n1>n2:
    (n1,n2)=(n2,n1)

while n1<=n2:
    print('%d '%n1,end=' ')
    n1+=1

def divisaoInteira(dividendo,divisor):
    if dividendo==0 and divisor==0:
        return tuple()
    elif divisor==0:
        return None
    else:
        quociente=dividendo//divisor
        resto=dividendo%divisor
    return (quociente,resto)
    
val=float(input('Valor em bits? '))

nota_50=0
nota_10=0
nota_5=0
nota_1=0

nota_50=divisaoInteira(val,50)
if nota_50[1]!=0:
    nota_10=divisaoInteira(nota_50[1],10)
    if nota_10[1]!=0:
        nota_5=divisaoInteira(nota_10[1],5)
        if nota_5[1]!=0:
            nota_1=divisaoInteira(nota_5[1],1)
        else:
            nota_1=(0,0)
    else:
        nota_5=(0,0)
        nota_1=(0,0)
else:
    nota_10=(0,0)
    nota_5=(0,0)
    nota_1=(0,0)

print('Convertido para %d notas de 50, %d notas de 10, %d notas de 5 e %d notas de 1'%(nota_50[0],nota_10[0],nota_5[0],nota_1[0]))

def corrige(gabarito, lista):
    nota = 0
    l_questoes=[]
    arq=open('questoes.txt','r')
    for linha in arq:
        info=linha.strip()
        l_questoes.append(info)
    for i in range(10):
        for pos in range(7):
            print(l_questoes[pos])
            print(' ')
        del l_questoes[0:8]
        resp = input("Digite a resposta da questão %d: "%(i+1))
        if resp == gabarito[i]:
            nota+=1
            lista.append(True)
        else:
            lista.append(False)
    arq.close()
    return nota

def exibeCorrecao(matr,nota,Lista):
    print("%d - Sua nota é: %d\n"%(matr,nota))
    print(Lista)
    
gab = ['d','d','a','d','b','e','c','c','c','c']
matr = int(input("Sua matrícula? "))
while matr != 0:
    lCorrecao = []
    nota = corrige(gab, lCorrecao)
    exibeCorrecao(matr,nota,lCorrecao)
    matr = int(input("Sua matrícula? "))

perg=('Telefonou para a vítima? ','Esteve no local do crime? ','Mora perto da vítima? ','Devia para a vítima? ','Já trabalhou com a vítima? ')
positivo=0
for el in perg:
    resp=input(el)
    if resp=='Sim':
        positivo+=1
if positivo<2:
    pessoa='inocente'
elif positivo==2:
    pessoa='suspeita'
elif positivo<5:
    pessoa='cúmplice'
else:
    pessoa='assassina'
    
print(pessoa)