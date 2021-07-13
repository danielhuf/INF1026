# -*- coding: utf-8 -*-
"""
NOME: Daniel Stulberg Huf
MAT: 1920468

Dicionario de INSCRITOS 
prof:JOISA
2020
Exercicio em aula 01/04/2020
"""


'''
Considere o dicionario com as inscricoes em disciplinas dos alunos 
de Engenharia em 2018-2, onde cada item do dicionario e:
  matricula : lista das disciplinas em que o aluno esta inscrito
'''

'''
A funcao criaDicInscricoes cria (por enumeracao) e retorna um dicionario 
como o descrito anteriormente
'''

def criaDicInscricoes():
    dicInscricoes={'172354881' : ['INF1111','MAT5555'] ,
              '162354884' : ['INF1711','MAT6655','FIS7676'] ,
              '182354672' : ['FIS7672','MAT3232'],
              '181354664' : ['INF1711','MAT5555'],
              '182654434' : ['INF1722','MAT6655','FIS7672'] ,
              }
    return dicInscricoes



dicInscr= criaDicInscricoes()

#Vou criar o dicionário inverso das incrições e disciplinas

dDiscAlunos={}
for al,ldisc in dicInscr.items():
    for disc in ldisc:
        lalunosDaDisc=dDiscAlunos.get(disc,[])
        lalunosDaDisc.append(al)
        dDiscAlunos[disc]=lalunosDaDisc

print(dDiscAlunos)

'''
EX 1- Exiba as matriculas dos inscritos
'''
print('\n----1----')
for el in dicInscr:
    print(el)
#também pode ser print(dicInscr.keys())
'''
EX 2 - Exiba o dicionario
'''
print('\n----2----')
print(dicInscr)
'''
EX 3 - Exiba os dados dos dicionarios no formato:
MATRICULA: xxxx - DISCIPLINAS: [aaa, bbb, ccc]
'''
print('\n----3----')
for mat in dicInscr:
    print('MATRICULA:',mat,'DISCIPLINAS:',dicInscr[el])
#ou faz for mat,ldisc in dicInscr.items():
    #print mat, ldisc
'''
EX 4- Leia do teclado uma matricula e verifique se ela esta entre 
os inscritos
'''
print('\n----4----')
mat=input('MATRICULA: ')
if mat in dicInscr:
    print('Está entre os inscritos')
else:
    print('Não está entre os inscritos')
'''
EX 5 - Leia do teclado uma matricula que OBRIGATORIAMENTE esta no 
dicionario e exiba as disciplinas em que o aluno esta inscrito
'''
print('\n----5----')
mat=input('MATRICULA: ')
print('DISCIPLINAS:',dicInscr[mat])
'''
EX 6 - Leia do teclado uma matricula (obrigatoriamente no dicionario)
 e uma disciplina e informe  se o aluno esta inscrito na disciplina
'''
print('\n----6----')
matDesejada='182354672'
discDesejada='MAT3232'
if discDesejada in dicInscr[matDesejada]:
    print('Está inscrito na matrícula')
else:
    print('Não está inscrito na matrícula')
'''
EX7 - Leia do teclado uma matricula e exiba suas disciplinas, se ela 
estiver no dicionário, ou a mensagem "nao consta". Atencao: nao pode 
testar com  in
'''
print('\n----7----')
matDesejada='111111'
ld=dicInscr.get(matDesejada,'não consta')
print(ld)
'''
EX8 - Visualize todas as chaves do dicionario
'''
print('\n----8----')
print(list(dicInscr.keys()))
'''
EX9 - Visualize todos os valores do dicionario
'''
print('\n----9----')
print(list(dicInscr.values()))
'''
EX10 - Visualize todos os itens(items) do dicionario
'''
print('\n----10----')
print(list(dicInscr.items()))
'''
EX11 - Inclua no dicionario a matricula 172111111 com as inscricoes 
em  FIS7672, MAT1414
'''
print('\n----11----')
dicInscr['172111111']=['FIS7672','MAT1414']
'''
EX12 - Leia uma matricula e uma disciplina. Caso a matricula ja exista 
a disciplina deve ser incluida na lista de disciplinas. Caso a matricula 
nao exista, deve ser incluido um novo item. Nao pode usar in.
'''
print('\n----12----')
disc='FIL1234'
mat1='172111111'
ld=dicInscr.get(mat1,[])
ld.append(disc)
dicInscr[mat1]=ld
mat2='172113333'
ld=dicInscr.get(mat2,[])
ld.append(disc)
dicInscr[mat2]=ld
#Funciona para quando existe e nao existe no dicionario
'''
EX13 - Leia uma matricula e retire-a do dicionario, exibindo o valor 
associado. Caso a matricula nao se encontre no dicionario, exiba a 
mensagem nao consta. Nao pode usar in
'''
print('\n----13----')
mat_1='172111111'
mat_2='888'
print(dicInscr.pop(mat_1,'não consta'))
print(dicInscr)
print(dicInscr.pop(mat_2,'não consta'))

#DICIONÁRIO INVERSO

dPortIng={'amor':'love','triste':'sad'}
dIngPort={}

for palport,paling in dPortIng.items():
    dIngPort[paling]=palport

print(dIngPort)

#Exercício do slide da aula
#a
def calculaIMC(peso,altura):
    imc=peso/(altura**2)
    return imc

dicdados={'Huguinho':[1.20,45],'Luisinho':[1.10,60],'Zezinho':[1.00,100],
          'Patinhas':[1.10,40],'Donald':[1.20,50]}

for el in dicdados:
    i=calculaIMC(dicdados[el][1],dicdados[el][0])
    print('Nome: %s - IMC: %.2f'%(el,i))
    
#b
l_chaves=list(dicdados.keys())
l_valores=list(dicdados.values())
print(l_chaves)
print(l_valores)

#c
soma_peso=0
for el in l_valores:
    soma_peso+=el[1]
peso_medio=soma_peso/len(l_valores)
print(peso_medio)

for el in dicdados:
    if 'u' in el or 'U' in el:
        dicdados[el][1]+=0.1*peso_medio

print(dicdados)

#d
dicdados['Clarabela']=[2.30,80]
dicdados['Peninha']=[1.20,60]
print(dicdados)

#e
dados_p=dicdados.pop('Peninha')
print('Altura: %.2f - Peso: %.2f'%(dados_p[0],dados_p[1]))

#f
dicdadosclone=dicdados.copy()
dicdadosclone['Donald']=[1.20,70]
print(dicdados)
print(dicdadosclone)

#a
dicmulheres={'Clarabela':[2.20,78],'Margarida':[1.10,40],'Vovó Donalda':[1.00,40]}
for el in dicmulheres:
    i=calculaIMC(dicmulheres[el][1],dicmulheres[el][0])
    print('Nome: %s - IMC: %.2f'%(el,i))

#b
dicdadosclone.update(dicmulheres)
print(dicdadosclone)

#c
excluir_chaves=[]
for el in dicdadosclone:
    if el in dicdados:
        excluir_chaves.append(el)
for c in excluir_chaves:
    del dicdadosclone[c]
print(dicdados)
print(dicdadosclone)

#d
dicdados.update(dicdadosclone)
print(dicdados)




