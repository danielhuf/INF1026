# -*- coding: utf-8 -*-
"""
CLASSE Triangulo
Created on Thu Sep 13 11:54:54 2018
@author: JOISA
"""

from ponto  import Ponto

class Triangulo:
    def __init__(self,nome,v1,v2,v3):
        self.nome = nome
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.lado1 = self.v1.distanciaEntrePontos(self.v2)
        self.lado2 = self.v2.distanciaEntrePontos(self.v3)
        self.lado3 = self.v3.distanciaEntrePontos(self.v1)
        
    def __str__(self):
        s=self.nome+" - V1:"+str(self.v1)+"- V2:"+str(self.v2)+"- V3:"+ str(self.v3)
        return s
    
    def __repr__(self):
        s="V1:"+str(self.v1)+"- V2:"+str(self.v2)+"- V3:"+ str(self.v3)
        return s
    
    def __gt__(self,outro):
        return self.area() > outro.area()
    
    def __lt__(self,outro):
        return self.area() < outro.area()
    
    def __eq__(self,outro):
        return self.area() == outro.area()
    
    def exibeLados(self):
        print("Lados: %.1f,%.1f,%.1f"%(self.lado1,self.lado2,self.lado3))
    
    def perimetro(self):
        return(self.lado1 + self.lado2 + self.lado3)
    
    def area(self):
        p = self.perimetro()/2
        area = (  p*(p-self.lado1)*(p-self.lado2)*(p-self.lado3) )**0.5
        return area
        
       

t1 = Triangulo("TriUm", Ponto(1,1), Ponto(3,1), Ponto(2,4)) 
print(t1) 
t1.exibeLados()
print(t1.area())
    
t2= Triangulo("TriDois", Ponto(4,3), Ponto(9,5), Ponto(6,11)) 
print(t2)
print(t2.area())

print(t1>t2)
print(t1<t2)
        
        
    
