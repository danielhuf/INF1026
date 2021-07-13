# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 17:30:00 2020

@author: cf
"""
class AvaliacaoBio():

    def __init__(self,alt=0,massa=0):
        self.alt=alt
        self.massa=massa
        self.setIMC()
        
        return

    def __str__(self):
        '''Monta uma string exibição'''
        return '(alt={:.2f},massa={:.3f},imc={:.2f})'.format(self.alt,self.massa,self.imc)

    def __repr__(self):
        '''Monta a representação interna '''
        return '(alt={:.2f},massa={:.3f},imc={:.2f})'.format(self.alt,self.massa,self.imc)

    
    def __eq__(self,outro):
        ''' recebe outro avaliacaoBio e retorna True se mesmas atributos, False cc'''
        return (self.alt==outro.alt and self.massa == outro.massa)
    
    def __neq__(self,outro):
        ''' recebe outro avaliacaoBio e retorna True se  atributos distintos, False cc'''
        return (self.alt!=outro.alt or self.massa != outro.massa)
    
    def __lt__(self,outro):
         ''' recebe outro avaliacaoBio e retorna True se menor imc, False cc'''
         return (self.imc<outro.imc)
    def __gt__(self,outro):
        ''' recebe outro avaliacaoBio e retorna True se maoir imc, False cc'''
        return (self.imc>outro.imc)
    
     
    def getAlt(self):
        ''' retorna o valor do atributo altura'''
        return self.x

    def getMassa(self):
        ''' retorna o valor do atributo massa '''
        return self.y
    
    def getIMC(self):
        ''' retorna o valor do imc '''
        return self.imc
    
    def setAlt(self,val):
        ''' recebe um valor que  torna-se a altura.'''
        self.alt=val
        self.setImc()
        return

    def setMassa(self,val):
        ''' recebe um valor que  torna-se a massa '''
        self.massa=val
        self.setIMC()
        return
    def setIMC(self):
        if self.alt>0: 
            self.imc=self.massa/(self.alt**2)
        else:
            self.imc=0
        return
    def detAval(self):
       ''' retorna o grupo IMC '''
       if self.imc <18.5:
           return 'magreza'
       elif self.imc <25:
           return 'normal'
       elif self.imc <30:
           return 'sobrepeso'
       else:
           return 'obesidade'

