class Cliente:
    def __init__(self, nome, idade, cpf):
        self.nome=nome
        self.idade = idade
        self.cpf = cpf
        self.valorTotalDeCompras=0.0
        
    def __str__(self):
        return ('{}-{}-{}-{}'.format(self.nome, self.idade,self.cpf,self.valorTotalDeCompras))
    
    def __repr__(self):
        return ('{}-{}-{}-{}'.format(self.nome, self.idade,self.cpf,self.valorTotalDeCompras))
    
    def novaCompra(self, valorCompra):
        self.valorTotalDeCompras+=valorCompra
        
    def informarValorTotalDeCompras(self):
        return self.valorTotalDeCompras
    
    def __lt__(self,outroCli):
        return self.nome < outroCli.nome

class Loja:
    def __init__(self,nome,gerente,cnpj):
        self.nome=nome
        self.gerente=gerente
        self.cnpj=cnpj
        self.listaClientes=[]
        return

    def incluiCliente(self,cliente):
        self.listaClientes.append(cliente)
        return

    def exibeClientes(self):
        for cliente in self.listaClientes:
            print(cliente)
        return

    def calculaValorTotal(self):
        valor=0
        for cliente in self.listaClientes:
            valor+=cliente.informarValorTotalDeCompras
        return valor

class ClientePreferencial(Cliente):
    def __init__(self,nome,idade,cpf,percentual):
        super().__init__(nome,idade,cpf)
        self.percentual=percentual
        return

    def __str__(self):
        return super().__str__() + '-{}%'.format(self.percentual)

    def __repr__(self):
        return super().__str__() + '-{}%'.format(self.percentual)

    def novaCompra(self,valorCompra):
        self.valorTotalDeCompras+=((100-self.percentual)/100)*valorCompra
        return
        
        
