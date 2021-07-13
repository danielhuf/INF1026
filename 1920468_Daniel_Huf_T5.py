#NOME: Daniel Stulberg Huf
#MAT: 1920468
#PROF: Joísa
#TURMA: 33C

#1.A)
def consulta(dic,nome):
    ano=dic[nome]
    print('Ano de nascimento: %d'%ano)
    return

#1.B)
def constroiDicAnoQtdAno(dic):
    novo={}
    for el,ano in dic.items():
        novo[ano]=novo.get(ano,0)+1
    return novo

#1.C)
def constroiDicAnoAlunos(dic):
    novo={}
    for el,ano in dic.items():
        lista_alunos=novo.get(ano,[])
        lista_alunos.append(el)
        novo[ano]=lista_alunos
    return novo

dicAlunosAnosN={'BUBA':1997,'PEPA':2001,'TATA':1998,'LALA':2001,
                'ZEZE':1998,'DUDU':1999,'DIDI':1995,'VAVA':1998,
                'KADU':1999,'DUDA':1998}

consulta(dicAlunosAnosN,'DUDU')
print(constroiDicAnoQtdAno(dicAlunosAnosN))
print(constroiDicAnoAlunos(dicAlunosAnosN))
