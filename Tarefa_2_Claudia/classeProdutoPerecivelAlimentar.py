#Daniel Stulberg Huf - matricula 1920468
#Prof. Claudia - Turma 33C

from classeProdutoPerecivel import *

class ProdutoPerecivelAlimentar(Produto):
    def __init__(self,identificacao='Produto',codigoBarras='',dataFabricacao=Data(),preco=0,validade=7):
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
        if Data()-self.dtValidade()==1:
            self.reajuste(-50)
        return

    def getValidade(self):
        return self.validade

    def setValidade(self,valor):
        self.validade=valor
        return


