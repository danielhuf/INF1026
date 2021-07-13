#Relações entre classes:

#uma classe TEM_UM (TEM_VARIOS) atributos (que são objetos) de outra classe

#uma classe USA_UM objeto de outra classe (dentro de um método)

#uma classe É_UM de outra classe

#classe Ponto
#CIRCULO TEM_UM centro (PONTO) e um raio
#retangulo pode ser formado pelo PONTO inferior esquerdo e PONTO superior direito
'''
import Turtle

class Retangulo:
    def __init__(self,vinfesq,vsupdir):
        self.vie=vinfesq
        self.vsd=vsupdir
        return

    def desenha(self):
        carrie=Turle()  #está usando outra classe
'''
#um EMPREGADO É_UMA PESSOA que, além de ter e fazer tudo o que uma pessoa
#tem e faz, tem também:
    #inscrição, salario, cargo,
    #informar seu cargo e salario, receber aumento

#=> HERANÇA - capacidade de se criar uma nova classe a partir de outra já existente
#O empregado É uma pessoa, ele não TEM uma pessoa (isso é herança)
#O retangulo TEM um ponto, (isso não é herança)
        
#ABAIXO - exemplo de classe e superclasse
        
class Pessoa:
    def __init__(self,nome,telefone,email):
        self.nome=nome
        self.telefone=telefone
        self.email=email
        return
    
    def __str__(self):
        return 'Contatos de %s: tel.: %s, email: %s'%(self.nome,self.telefone,self.email)
    
class Estudante(Pessoa):
    disciplinas={}
    
    def __init__(self,nome,telefone,email,matricula,curso):
        super().__init__(nome,telefone,email) #o estudante herda essas caracteristicas
        self.matricula=matricula
        self.curso=curso
        return
    
    def fazDisciplina(self,codigo,media):
        self.disciplinas[codigo]=media
        return
    
    def retornaDisciplinas(self):
        return self.disciplinas
    
class Professor(Pessoa):
    def __init__(self,nome,telefone,email,formacao,areaInteresse):
        super().__init__(nome,telefone,email)
        self.formacao=formacao
        self.areaInteresse=areaInteresse
        return
    
    def retornaCurriculo(self):
        return super().__str__() + '\nformado em %s com interesse em %s'%(self.formacao,self.areaInteresse)

aluno = Estudante('Huguinho','555-8752','Huguinho@eng.puc-rio.br','20208752','Engenharia')

professor = Professor('Pardal','555-2578','pardal@puc-rio.br','Engenharia','Engenhocas')

aluno.fazDisciplina('INF1026',9.5) 
aluno.fazDisciplina('INF1025',7.0)
print(aluno.nome,'cursou',aluno.retornaDisciplinas())

print('Professor',professor.retornaCurriculo())    
