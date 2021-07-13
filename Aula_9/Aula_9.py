#Resolvendo o exercício "Matrículas e Disciplinas" do ead

#1
def criaItemAluno(dadosUmAluno):
    matAluno=dadosUmAluno[0]
    listaDisc=dadosUmAluno[1:]
    return (matAluno,listaDisc)

def criaDicDisciplinasDoAluno(nomeArq):
    arq=open(nomeArq,'r')
    dicDiscDoAluno={}
    for linha in arq:
        (mAluno,lDiscAluno)=criaItemAluno((linha.strip()).split(';'))
        dicDiscDoAluno[mAluno]=lDiscAluno
    arq.close()
    return dicDiscDoAluno

dic1=criaDicDisciplinasDoAluno('Inscritos.csv')
print('\n ALUNO: disciplinas em que está inscrito')
for aluno in dic1:
    print(aluno,':',dic1[aluno])

#2
def criaDicAlDaDisc(dDiscDoAl):
    dAlunosDaDisc={}
    for aluno in dDiscDoAl:
        for disc in dDiscDoAl[aluno]:
            lstAlunosDaDisc=dAlunosDaDisc.get(disc,[])
            lstAlunosDaDisc.append(aluno)
            dAlunosDaDisc[disc]=lstAlunosDaDisc
    return dAlunosDaDisc

dic2=criaDicAlDaDisc(dic1)
print('\n DISCIPLINA: alunos inscritos')
for disc in dic2:
    print(disc,':',dic2[disc])

#3
def criaItemAluno(dadosUmAluno):
    matAluno=dadosUmAluno[0]
    dDesemp={}
    tam=len(dadosUmAluno)
    for i in range(1,tam,2): #vai de 2 em 2
        dDesemp[dadosUmAluno[i]]=dadosUmAluno[i+1]
    return (matAluno,dDesemp)

def criaDicDisciplinasDoAluno(nomeArq):
    arq=open(nomeArq,'r')
    dHistoricos={}
    for linha in arq:
        l=linha.strip()
        li=l.split(';')
        (mAluno,dDesempAluno)=criaItemAluno(li)
        dHistoricos[mAluno]=dDesempAluno
    arq.close()
    return dHistoricos

dic1=criaDicDisciplinasDoAluno('HistoricoNotas.csv')
print('\n ALUNO e seu histórico')
for aluno in dic1:
    print(aluno,':',dic1[aluno])

#4        
#Primeira Solução (intuitiva)
def criaDicInverso(dHistorico):
    dDisc={}
    for al in dHistorico:   #essa estrutura dá no mesmo que usar o items
        for disc in dHistorico[al]:  
            if disc not in dDisc:
                dDisc[disc]={al:dHistorico[al][disc]}
            else:
                dDisc[disc].update({al:dHistorico[al][disc]})
    return dDisc

#Segunda solução (elegante)
def criaDicInverso2(dHistorico):
    dDisc={}
    for al,dDesemp in dHistorico.items():
        for disc in dDesemp:
            dAleNt=dDisc.get(disc,{})
            dAleNt[al]=dDesemp[disc]
            dDisc[disc]=dAleNt
    return dDisc

dic2=criaDicInverso2(dic1)
print('\n DISCIPLINA e seus alunos')
for disc in dic2:
      print(disc,':',dic2[disc])

