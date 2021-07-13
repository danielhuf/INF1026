#Daniel Stulberg Huf - matricula 1920468
#Prof. Claudia - Turma 33C

from classeData import *

class Produto:
    def __init__(self,identificacao='Produto',codigoBarras='',dataFabricacao=Data(),preco=0):
        self.identificacao=identificacao
        self.codigoBarras=codigoBarras
        self.dataFabricacao=dataFabricacao
        self.preco=preco
        return

    def __str__(self):
        return '\nIdentificação: {} - Código de barras: {} - Data de Fabricação: {} - Preço: R${:.2f}'.format(self.getIdentificacao(),self.getCodigoBarras(),self.getDataFabricacao(),self.getPreco())

    def __repr__(self):
        return '\nIdentificação: {} - Código de barras: {} - Data de Fabricação: {} - Preço: R${:.2f}'.format(self.getIdentificacao(),self.getCodigoBarras(),self.getDataFabricacao(),self.getPreco())

    def idade(self):
        return self.getDataFabricacao() - Data()
    
    def ehSemelhante(self,outro):
        return self.getIdentificacao()==outro.getIdentificacao()

    def reajuste(self,valor):
        self.setPreco(((100+valor)/100)*self.getPreco())
        return

    def getIdentificacao(self):
        return self.identificacao

    def getCodigoBarras(self):
        return self.codigoBarras

    def getDataFabricacao(self):
        return self.dataFabricacao

    def getPreco(self):
        return self.preco

    def setIdentificacao(self,valor):
        self.identificacao=valor
        return

    def setCodigoBarras(self,valor):
        self.codigoBarras=valor
        return

    def setDataFabricacao(self,valor):
        self.dataFabricacao=valor
        return

    def setPreco(self,valor):
        self.preco=valor
        return

    def __eq__(self,outro):
        return self.getIdentificacao()==outro.getIdentificacao() and self.getCodigoBarras()==outro.getCodigoBarras() and self.getDataFabricacao()==outro.getDataFabricacao() and self.getPreco()==outro.getPreco()

    def __lt__(self,outro):
        return self.getDataFabricacao()>outro.getDataFabricacao() or self.getDataFabricacao()==outro.getDataFabricacao() and self.getPreco()<outro.getPreco()



