#Daniel Stulberg Huf - matricula 1920468
#Prof. Claudia - Turma 33C

from classeProdutoPerecivelAlimentar import *

class Armazem:
    def __init__(self,depositos={'Refrigerado':[],'Controlado':[],'Simples':[]}):
        self.depositos=depositos
        return

    def ordena(self):
        for deposito,lista in self.depositos.items():
            lista.sort()
        return

    def __str__(self):
        s='Depósito Refrigerado: '
        for produto in self.depositos['Refrigerado']:
            s+=produto.__str__()
        s+='\nDepósito Controlado: '
        for produto in self.depositos['Controlado']:
            s+=produto.__str__()
        s+='\nDepósito Simples: '
        for produto in self.depositos['Simples']:
            s+=produto.__str__()
        return s
        
    
    def __repr__(self):
        return 'Refrigerado:{}\nControlado:{}\nSimples:{}'.format(self.depositos['Refrigerado'],self.depositos['Controlado'],self.depositos['Simples'])

    def inclui(self,deposito,produto):
        self.depositos[deposito].append(produto)
        self.ordena()
        return

    def retira(self,identificacao,deposito):
        if deposito=='Simples':
            for produto in self.depositos['Simples'][::-1]:   #Para retirar dos produtos simples, tive que começar do fim da lista (mais velhos)
                if produto.getIdentificacao()==identificacao:
                    self.depositos['Simples'].remove(produto)
                    return
        else:
            for produto in self.depositos[deposito]:
                if produto.getIdentificacao()==identificacao:
                    self.depositos[deposito].remove(produto)
                    return

    def entraEmPromocao(self):
        for produto in self.depositos['Controlado']:
            produto.entraEmPromocao()
        for produto in self.depositos['Refrigerado']:
            produto.entraEmPromocao()
        return

    def aplicaReajuste(self,valor):
        for deposito,lista in self.depositos.items():
            for produto in lista:
                produto.reajuste(valor)
        return
            
print('----------Testando a classe Armazem----------')
a=Armazem()
print(a)
a.inclui('Simples',Produto('TV','BBB',Data(10,10,2019),1500))
print(a)
a.inclui('Simples',Produto('TV','AAA',Data(10,10,2019),1200))
print(a)
a.inclui('Simples',Produto('Lâmpada','ASD',Data(10,1,2019),20))
print(a)
a.inclui('Simples',Produto('TV','CCC',Data(30,8,2019),1000))
print(a)
a.inclui('Controlado',ProdutoPerecivel(180,'Água','bbb',Data(10,10,2019),7))
print(a)
a.inclui('Controlado',ProdutoPerecivel(100,'Água','ccc',Data(10,10,2019),9))
print(a)
a.inclui('Controlado',ProdutoPerecivel(90,'Pão','111',Data(23,4,2020),6))
print(a)
a.inclui('Controlado',ProdutoPerecivel(90,'Pão','111',Data(24,4,2020),6))
print(a)
a.inclui('Controlado',ProdutoPerecivel(90,'Pão','111',Data(25,4,2020),3))
print(a)
a.inclui('Refrigerado',ProdutoPerecivelAlimentar('Alface','111',Data(23,4,2020),4))
print(a)
a.inclui('Refrigerado',ProdutoPerecivelAlimentar('Manteiga','111',Data(23,4,2020),6))
print(a)
a.inclui('Refrigerado',ProdutoPerecivelAlimentar('Manteiga','111',Data(24,4,2020),6))
print(a)
a.inclui('Refrigerado',ProdutoPerecivelAlimentar('Manteiga','111',Data(25,4,2020),3))
print(a)
a.retira('TV','Simples')
a.retira('Pão','Controlado')
a.retira('Manteiga','Refrigerado')
print(a)
a.aplicaReajuste(10)
print(a)
a.entraEmPromocao()
print(a)

