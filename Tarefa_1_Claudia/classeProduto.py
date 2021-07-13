#Daniel Stulberg Huf - matricula 1920468
#Prof. Claudia - Turma 33C

from classeDataCompleta import Data

class Produto:

    def __init__(self,ide='Produto',codb='',df=Data(),p=0):
        self.identificacao=ide
        self.codigoBarras=codb
        self.dataFabricacao=df
        self.preco=p
        return

    def __str__(self):
        return 'Identificação: {} - Código de barras: {} - Data de Fabricação: {} - Preço: R${:.2f}'.format(self.identificacao,self.codigoBarras,self.dataFabricacao,self.preco)

    def __repr__(self):
        return 'Identificação: {} - Código de barras: {} - Data de Fabricação: {} - Preço: R${:.2f}'.format(self.identificacao,self.codigoBarras,self.dataFabricacao,self.preco)

    def idade(self):
        return self.dataFabricacao - Data()
    
    def ehSemelhante(self,outro):
        return self.identificacao==outro.identificacao

    def reajuste(self,valor):
        self.preco+=(valor/100)*self.preco
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
        return self.identificacao==outro.identificacao and self.codigoBarras==outro.codigoBarras and self.dataFabricacao==outro.dataFabricacao and self.preco==outro.preco

    def __lt__(self,outro):
        if self.dataFabricacao!=outro.dataFabricacao:
            return self.dataFabricacao>outro.dataFabricacao
        return self.preco<outro.preco



    


