# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 11:09:20 2018

CLASSE Ponto
"""

class Ponto:
    def __init__ (self, x=0, y=0):
        self.x = x
        self.y = y
        return
        
    def __str__(self):
        s = "({:.1f},{:.1f})".format(self.x,self.y)
        return s
    
    def __repr__(self):
        s = "({:.2f},{:.2f})".format(self.x,self.y)
        return s

    def exibir(self):
        print('(%.2f,%.2f)'%(self.x,self.y))
    
    def distanciaAteOrigem(self):
        d = (self.x**2+ self.y**2)**0.5
        return d
    
    def distanciaEntrePontos(self,outro):
        d = ((self.x-outro.x)**2+ (self.y-outro.y)**2)**0.5
        return d

    def quadrante(self):
        if self.x>=0:
            if self.y>0:
                return 1
            elif self.y<0:
                return 4
            else:
                return 'origem'
        elif self.y>0:
            return 2
        else:
            return 3

    def desloca(self,n):
        self.x+=n
        self.y+=n
        return

    def __eq__(self,outro):
        return self==outro

a=Ponto(2,2)
print(a.x==a.y)

        
            






