# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 07:39:17 2020

@author: lcam
"""

class Ponto():
    # Construtor
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        return
    
    # Exibição via print e no interpretador
    def __str__(self):
         s= '({},{})'.format(self.getX(),self.getY())
         return s
    def __repr__(self):
         s= '({},{})'.format(self.getX(),self.getY())
         return s
    
    # Acesso aos atributos    
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    
    # Clonar 
    def clonar(self):
        c=Ponto(self.x,self.y)  # poderia ser self.getX(),self.getY()
        return c

    # Alteração dos Atributos
    def alteraCoordenada(self,eixo,valor):
        if eixo.upper()== 'X':
            self.x=valor
        else:
            self.y=valor
        return
    
    def alteraCoordenadas(self,valorX='',valorY=''):
        if valorX != '':
            self.x=valorX
        if valorY != '':
            self.y=valorY 
        return
    
    def setX(self,valor):
        self.x=valor
        return
    
    def setY(self,valor):
        self.y=valor
        return
    
    # Operadores Aritméticos definidos: + e -   
    def __add__(self,OutroPto):
        ''' construir um novo ponto 
        cujo x, y é a soma das coordenadas'''
        x=self.getX() + OutroPto.getX()
        y=self.getY() + OutroPto.getY()
        return Ponto(x,y)
    
    def __sub__(self,OutroPto):
        ''' construir um novo ponto 
        cujo x, y é a diferença das coordenadas'''
        x=self.getX() - OutroPto.getX()
        y=self.getY() - OutroPto.getY()
        return Ponto(x,y)
    
    # Operadores Relacionais definidos: ==, !=, < e > e -   
    def __eq__(self,OutroPto):
        return self.getX() == OutroPto.getX() and \
                self.getY() == OutroPto.getY()
                
    def __neq__(self,OutroPto):
        return self.getX() != OutroPto.getX() or  \
                self.getY() != OutroPto.getY()
                
    def __lt__(self,OutroPto):
        d1= self.distAOrigem()
        d2= OutroPto.distAOrigem()
        return d1<d2
    
    def __gt__(self,OutroPto):
        d1= self.distAOrigem()
        d2= OutroPto.distAOrigem()
        return d1>d2
    
    # Outros métodos
    def distAOrigem(self):
        d= (self.getX()**2 + self.getY()**2)**0.5
        return d   
    
    def distEntre2Pontos(self,OutroPto):
        d= ((self.getX()-OutroPto.getX())**2 + (self.getY()- OutroPto.getY())**2)**0.5
        return d
    
    def ptoMediano(self,OutroPto):
        x=(self.getX()+OutroPto.getX())/2
        y=(self.getY()+OutroPto.getY())/2
        return Ponto(x,y)
    
    def coefAngular(self,outro): 
        x1=self.getX()  #poderia ser também  x1=self.x
        x2=outro.getX()
        y1=self.getX()
        y2=outro.getY()
        m=(y2-y1)/(x2-x1)
        return abs(m)
     
    






