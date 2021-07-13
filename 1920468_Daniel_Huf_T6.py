#Daniel Stulberg Huf - 1920468
#prof. Joisa turma 33C

class Aluno:
    def __init__(self,mat,nom,no):
        self.nome=nom
        self.matricula=mat
        self.nota=no
        return

    def __str__(self):
        s='MAT:{} - NOME :{} - NOTA:{}'.format(self.matricula,self.nome,self.nota)
        return s

    def __gt__(self,outro):
        return self.nota>outro.nota

    def alterarNota(self,nova):
        self.nota=nova
        return

    def exibirSituacao(self):
        if self.nota>=5:
            s='aprovado'
        else:
            s='reprovado'
        print('Matrícula: %d - situação: %s'%(self.matricula,s))
        return

a1=Aluno(111,'NENA',7.5)
print(a1)
a1.alterarNota(8.3)
print(a1)
a1.exibirSituacao()

a2=Aluno(222,'PEPE',4.4)
print(a2)
a2.exibirSituacao()

if a1>a2:
    print(a1.nome,'melhor do que',a2.nome)
else:
    print(a1.nome,'NAO melhor do que',a2.nome)


        
