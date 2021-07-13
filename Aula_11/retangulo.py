from ponto import Ponto

class Retangulo:
    def __init__(self,lado1=1,lado2=1):
        self.lado1 = lado1
        self.lado2 = lado2
        return
    
    def exibeMedidas(self):
        print('Alt: {} Compr: {}'.format(self.lado1,self.lado2))
        return

    def area(self):
        return self.lado1*self.lado2

    def perimetro(self):
        return 2*(self.lado1+self.lado2)
    
class Quadrado(Retangulo):
    def __init__(self,lado=1):
        super().__init__(lado,lado) 
        #o método da superclasse está sendo redefinido na classe derivada
        return
    
    def exibeMedidas(self):
        print('Lado: {}'.format(self.lado1))
        return

print('Peímetro do Retângulo: ', Retangulo(10,20).perimetro())
print('Perímetro do Quadrado: ', Quadrado(10).perimetro())
Retangulo(10,20).exibeMedidas()
Quadrado(10).exibeMedidas()

