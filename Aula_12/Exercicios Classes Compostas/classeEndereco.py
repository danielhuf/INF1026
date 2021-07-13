# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:06:00 2020

@author: cf
"""

class Endereco():

    def __init__(self,rua,num,cid,bairro='',ap='',cpl=''):
        self.rua=rua
        self.num=num
        self.ap=str(ap)
        self.co=complemento
        self.bairro= bairro
        self.cid = cid
        return

    def __str__(self):
        # Monta uma string com os dados existentes do endereço
        end='{}, {}'.format(self.rua,self.num)
        if len(self.apto) > 0:
            end = '{} ap {}'.format(end,self.apto)
        if len(self.compl)>0:
            end = '{}, {}'.format(end,self.compl)
        if len(self.bairro)>0:
            end = '{} - {}'.format(end,self.bairro)
        end='{}\n {}'.format(end,self.cid)
        
        return end

    def __repr__(self):
        # Monta a representação interna  com atributos válidos
        end='{}, {}'.format(self.rua,self.num)
        if len(self.apto) > 0:
            end = '{} ap {}'.format(end,self.apto)
        if len(self.compl)>0:
            end = '{}, {}'.format(end,self.compl)
        if len(self.bairro)>0:
            end = '{} - {}'.format(end,self.bairro)
        end='{}\n{}'.format(end,self.cid)
        
        return end

    
    def __eq__(self,outro):
        ''' recebe outro Endereco e retorna True se mesmos atributos'''
        
        return (self.rua==outro.rua and 
                self.num == outro.num and
                self.apto==outro.apto and
                self.compl==outro.compl and
                self.bairro== outro.bairro and
                self.cid == outro.cid)
    
    def getBairro(self):
        return self.bairro

    def getCidade(self):
        return self.cid
    
    def mesmoBairro(self,outro):
        return self.bairo == outro.bairro

    def mesmaCidade(self,outro):
        return self.cid == outro.cid

    def copiaValores(self,outro):
        ''' altera atributos com valores de outro'''
        self.rua=outro.rua
        self.num = outro.num
        self.apto=outro.apto
        self.compl=outro.compl
        self.bairro=outro.bairro
        self.cid = outro.cid
        return
