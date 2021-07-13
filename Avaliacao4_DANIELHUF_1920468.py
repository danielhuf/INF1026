#Nome completo: Daniel Stulberg Huf
#Matrícula PUC-Rio: 1920468
#Declaração de autoria: Declaro que este documento foi produzido em sua totalidade por mim,
#sem consultas a outros alunos, professores ou qualquer outra pessoa.

class Acao:
    def __init__(self,nome,codigo,valorUnit,quant,tamanho):
        self.nome=nome
        self.codigo=codigo
        self.valorUnit=valorUnit
        self.quant=quant
        if quant%tamanho!=0:
            self.quant-=quant%tamanho
        self.tamanho=tamanho
        return

    def __str__(self):
        return '{} ({}) R${:.2f} x {} = R${:.2f}'.format(self.nome,self.codigo,self.valorUnit,self.quant,self.valorUnit*self.quant)

    def __repr__(self):
        return '{} ({}) R${:.2f} x {} = R${:.2f}'.format(self.nome,self.codigo,self.valorUnit,self.quant,self.valorUnit*self.quant)

    def __add__(self,q):
        nova_quant=self.quant+q
        if nova_quant%self.tamanho!=0:
            nova_quant-=nova_quant%self.tamanho
        novo=Acao(self.nome,self.codigo,self.valorUnit,nova_quant,self.tamanho)
        return novo

print('----------Testando a classe Acao----------\n')
acao=Acao('Petrobras PN','PETR4',15.4,1550,100)
print('==>',acao)
acao=acao+257
print('==>',acao)
