#Daniel Stulberg Huf - matricula 1920468
#Prof. Joísa - turma 33C

class ContaBancaria:
    def __init__(self,num,sen,nom,sal=0.0):
        self.numero=num
        self.senha=sen
        self.nome=nom
        self.saldo=sal
        return

    def __str__(self):
        s='{}-{}-{}'.format(self.numero,self.nome,self.saldo)
        return s

    def exibeSaldo(self,senha):
        if self.senha==senha:
            print('SALDO EM CONTA: ',self.saldo)
        else:
            print('SENHA INCORRETA')
        return

    def deposito(self,valor):
        self.saldo+=valor
        return

    def saque(self,valor,senha):
        if self.senha != senha:
            print('SENHA INCORRETA')
            return False
        elif valor>self.saldo:
            print('SALDO INSUFICIENTE')
            return False
        else:
            self.saldo-=valor
            return True
        
        
        
