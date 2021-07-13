#Daniel Stulberg Huf - matricula 1920468
#Prof. Claudia - Turma 33C

from classeProduto import *

class ProdutoPerecivel(Produto):
    def __init__(self,validade,identificacao='Produto',codigoBarras='',dataFabricacao=Data(),preco=0):
        super().__init__(identificacao,codigoBarras,dataFabricacao,preco)
        self.validade=validade
        return

    def __str__(self):
        return super().__str__() + ' - Data de validade: {}'.format(self.dtValidade())

    def __repr__(self):
        return super().__str__() + ' - Data de validade: {}'.format(self.dtValidade())

    def dtValidade(self):
        data=self.getDataFabricacao()+self.getValidade()
        return data

    def __lt__(self,outro):
        return self.dtValidade()<outro.dtValidade() or self.dtValidade()==outro.dtValidade() and self.getPreco()<outro.getPreco()

    def entraEmPromocao(self):
        if Data()-self.dtValidade()<=30:
            self.reajuste(-20)
        return

    def getValidade(self):
        return self.validade

    def setValidade(self,valor):
        self.validade=valor
        return







                    

    
        
                    
                
            


                             

    

    
        
        
        
    


        
