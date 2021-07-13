from ClassePonto import Ponto
class Retangulo():
    def __init__(self,vIE=(0,0),vSD=(1,1)):
        self.vie=Ponto(vIE[0],vIE[1])
        self.vsd=Ponto(vSD[0],vSD[1])
        self.altura=self.vie.distEntre2Pontos(Ponto(vIE[0],vSD[1]))
        self.base=self.vie.distEntre2Pontos(Ponto(vSD[0],vIE[1]))
        return

    def __str__(self):
        return 'vie: {} vsd: {} alt: {:.2f} base: {:.2f}'.format(self.vie,self.vsd,self.altura,self.base)

    def __repr__(self):
        return 'vie: {} vsd: {} alt: {:.2f} base: {:.2f}'.format(self.vie,self.vsd,self.altura,self.base)

    def __lt__(self,outro):
        d1=self.vie.distAOrigem()
        d2=outro.vie.distAOrigem()
        a1=self.area()
        a2=outro.area()
        return d1<d2 or d1==d2 and a1<a2

    def area(self):
        return self.base*self.altura

class Quadrado(Retangulo):
    def __init__(self,vIE,vSD=(1,1)):
        super().__init__(vIE,vSD)
        if self.altura!=self.base:
            super().__init__()
        self.lado=self.base  #self.lado=super().base
        return

    def __str__(self):   #vou crirar outro str, já que estou mudando a estrutura do print
        return 'vie:{} vsd:{} lado{:.2f}'.format(self.vie,self.vsd,self.lado)

    def __repr__(self):
        return 'vie:{} vsd:{} lado{:.2f}'.format(self.vie,self.vsd,self.lado)   
    
