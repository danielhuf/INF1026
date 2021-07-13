#Construí a classe círculo

from ClassePonto import Ponto

class Circulo:
    def __init__(self,c,r):
        self.centro=c
        self.raio=r
        return

    def __str__(self):
        return 'Centro do círculo: {} - Raio do círculo: {}'.format(self.centro,self.raio)

    def __repr__(self):
        return 'Centro do círculo: {} - Raio do círculo: {}'.format(self.centro,self.raio)

    def __eq__(self,outro):
        if self.centro==outro.centro and self.raio==outro.raio:
            return True
        else:
            return False

    def __ne__(self,outro):
        if self.centro==outro.centro and self.raio==outro.raio:
            return False
        else:
            return True

    def __gt__(self,outro):
        if self.raio>outro.raio:
            return True
        else:
            return False

    def __lt__(self,outro):
        if self.raio<outro.raio:
            return True
        else:
            return False

    def __add__(self,outro):
        c=self.centro.ptoMediano(outro.centro)
        r=self.raio+outro.raio
        novo=Circulo(c,r)
        return novo

    def __sub__(self,outro):
        c=self.centro.ptoMediano(outro.centro)
        r=abs(self.raio-outro.raio)
        novo=Circulo(c,r)
        return novo

    def __mul__(self,n):
        c=self.centro
        r=n*self.raio
        novo=Circulo(c,r)
        return novo

    def __truediv__(self,n):
        c=self.centro
        r=(self.raio)/n
        novo=Circulo(c,r)
        return novo

    def tipo(self,outro):
        d=self.centro.distEntre2Pontos(outro.centro)
        if d==self.raio+outro.raio:
            return 'Circunferências tangentes externas'
        elif d==self.raio-outro.raio:
            return 'Circunferências tangentes internas'
        elif d==0:
            return 'Circunferências concêntricas'
        elif d<self.raio+outro.raio:
            return 'Circunferências secantes'
        else:
            return 'Não encostam'

    def interior(self,ponto):
        if ponto.getX() >= self.raio*(-1) and ponto.getX() <= self.raio and ponto.getY() >= self.raio*(-1) and ponto.getY() <= self.raio:
            return True
        else:
            return False

#GABARITO
import math

class Circulo:

    def __init__(self,c=Ponto(0,0),r=1):
        self.centro=c
        self.raio=r
        return

    def __str__(self):
        # Monta uma string ==> centro:(x,y) -  raio: r
        return 'centro:{} - raio:{}'.format(self.centro,self.raio)

    def __repr__(self):
        # Monta a representação interna ==>  c:(x,y) -  r: r]
        return 'c:{} - r:{}'.format(self.centro,self.raio)

    
    def __eq__(self,outro):
        ''' recebe outro circulo e retorna True se mesmoas atributos, False cc'''
        return (self.centro==outro.centro and self.raio == outro.raio)
    
    def __neq__(self,outro):
       ''' recebe outro circulo e retorna True se atributos distintos, False cc'''
       return (self.centro!=outro.centro or self.raio != outro.raio)
    
    def __lt__(self,outro):
        ''' recebe outro circulo e retorna True, se menor raio'''
        return (self.getRaio()<outro.getRaio())
    
    def  __gt__(self,outro):
        ''' recebe outro circulo e retorna True, se maior raio'''
        return (self.raio>outro.raio)
    
     
    def __add__(self,outro):
        ''' recebe  como parâmetro um outro objeto da classe Círculo e 
        retorna um novo Círculo cujo centro é o ponto mediano entre os círculos 
                                  e o raio é a soma dos raios  '''
        centro=self.centro.PontoMedio(outro.getCentro())
        return Circulo(c=centro,r=self.raio+outro.raio)
    def __sub__(self,outro):
        ''' recebe  como parâmetro um outro objeto da classe Círculo e 
        retorna um novo Círculo cujo centro é o ponto mediano entre os círculos
                                            e o raio é a subtração dos raios  '''
        centro=self.centro.PontoMedio(outro.centro)
        return Circulo(c=centro,r=abs(self.raio-outro.raio))
    
    def __mul__(self,v):
        ''' recebe  como parâmetro um número e 
        retorna um novo círculo com mesmo centro e raio multiplicado pelo valor'''
        return Circulo(self.centro,self.raio*v)
    
    def __div__(self,v):
        ''' recebe  como parâmetro um número e 
        retorna um novo círculo com mesmo centro e raio dividido pelo valor'''
        return Circulo(self.centro,self.raio/v)
       
    def getCentro(self):
        ''' retorna o ponto do centro'''

    def getRaio(self):
        ''' retorna o valor do raio '''
        return self.raio
    
    def setCentro(self,pto):
        ''' recebe um pto que  torna-se o centro do circulo '''
        self.centro=pto
        return

    def setRaio(self,val):
        ''' recebe um valor que  torna-se o raio do círculo '''
        self.raio=val
        return



    def clonar(self):
        ''' cria um novo circulo com mesmas coordenadas de centro e mesmo raio'''
        c=self.centro.clonar()
        return Circulo(c,self.raio)
    
    def interior(self,pto):
        ''' True se ponto está dentro do círculo, False, cc '''
        dist= self.centro.distanciaEntrePontos(pto)
        return (dist<=self.raio)
    
    def tipo(self,outro):
        dOC= self.centro.distanciaEntrePontos(outro.centro)
        if dOC == 0:
            return 'Concêntricos'
        elif dOC == abs(self.raio+outro.raio):
            return 'Tangentes Externos'
        elif dOC == abs(self.raio-outro.raio):
            return 'Tangentes Internos'
        elif dOC < abs(self.raio+outro.raio):
            return 'Secantes'
        else:
            return 'Não encostam'
