#Relações entre classes:

#uma classe TEM_UM (TEM_VARIOS) atributos (que são objetos) de outra classe

#uma classe USA_UM objeto de outra classe (dentro de um método)

#uma classe É_UM de outra classe

#classe Ponto
#CIRCULO TEM_UM centro (PONTO) e um raio
#retangulo pode ser formado pelo PONTO inferior esquerdo e PONTO superior direito

from ponto import Ponto

class Retangulo:
    def __init__(self,a=Ponto(),b=Ponto(1,1)):
        self.vert1=a
        self.vert3=b
        self.vert2=Ponto(self.vert3.x,self.vert1.y)
        self.vert4=Ponto(self.vert1.x,self.vert3.y)
        return

    def base(self):
        return self.vert1.distanciaEntrePontos(self.vert2)

    def altura(self):
        return self.vert1.distanciaEntrePontos(self.vert4)

    def area(self):
        return self.altura()*self.base()

    def __str__(self):
        return('Vértice Inf Esq: {}\nVértice Sup Dir: {}\nLargura: {}\nAltura: {}'.format(self.vert1,self.vert3,self.base(),self.altura()))

    def desenha(self):
        carrie=Turle()  #está usando outra classe

#class Pessoa
        #nome
        #idade
        #-apresentar
        #-fazerAniversario

#um EMPREGADO É_UMA PESSOA que, além de ter e fazer tudo o que uma pessoa
#tem e faz, tem também:
    #inscrição, salario, cargo,
    #informar seu cargo e salario, receber aumento

#=> HERANÇA - capacidade de se criar uma nova classe a partir de outra já existente
#O empregado É uma pessoa, ele não TEM uma pessoa (isso é herança)
#O retangulo TEM um ponto, (isso não é herança)

#EXEMPLO DE AGREGAÇÃO/COMPOSIÇÃO
#VER AS CLASSES PONTO E TRIANGULO CONTIDAS NA PASTA AULA_11
