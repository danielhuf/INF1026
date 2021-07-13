class ContaBancaria():
    def __init__(self,numero, senha, nome, saldo=0.0):
        self.num=numero
        self.senha=senha
        self.nome=nome
        self.saldo=saldo
        return
    def __str__(self):
        return 'Cta: {} Titular: {} Saldo: {:.2f}'.format(self.num,self.nome,self.saldo)
    
    def __repr__(self):
        return 'Cta: {} Titular: {} Saldo: {:.2f}'.format(self.num,self.nome,self.saldo)
    
    def exibeSaldo(self,senha):
        if senha == self.senha:
            print(self)
        else:
            print("Senha Inválida")
    def deposito(self,valor):
        if valor>0:
            self.saldo+=valor
        return valor>0
    
    def saque(self,senha, valor):
        if senha == self.senha:
            if valor <= self.getSaldo():
                self.saldo-=valor
                return True
            else:
                print("Cta {} - SALDO INSUFICIENTE".format(self.num))
        return False
    
    def transferencia(self,ctaBanc, senha,valor):
        r=self.saque(senha,valor)
        if r:
            ctaBanc.deposito(valor)
        return r
    def getSaldo(self):
        return self.saldo
    
    def __lt__(self,outro):
        return self.getSaldo() < outro.getSaldo()

#Irei criar a conta corrente e a conta poupança, ambas sao contas bancarias.

class ContaCorrente(ContaBancaria):
    def __init__(self,num,nome,senha,saldo=0,tx=20):
    	#criar uma instância da classe do meu "pai" e 
        # ajustá-la p/minhas particularidades
        super().__init__(num,nome,senha,saldo)
        self.tx=tx
        return
    
    def __str__(self):
        dadosPai=super().__str__()
        meusDados=' Tx: {:.2f}'.format(self.tx)
        return dadosPai + meusDados
    
    def __repr__(self):
        dadosPai=super().__str__()
        meusDados=' Tx: {:.2f}'.format(self.tx)
        return dadosPai + meusDados

    #métodos que só dizem respeito a conta corrente
    def aplicaTaxa(self):
        self.saldo=self.getSaldo()-self.tx
        return 
    
    def setTaxa(self,tx):
        self.tx=tx
        return
    
    def getTaxa(self):
        return self.taxa

class ContaPoupanca(ContaBancaria):
    def __init__(self,num,nome,senha,saldo=0,tx=0.1):
    	#criar uma instância da classe do meu "pai" e 
        # ajustá-la p/minhas particularidades
        super().__init__(num,nome,senha,saldo)
        self.tx=tx
        return
    
    def __str__(self):
        dadosPai=super().__str__()
        meusDados=' Tx: {:.3f}%'.format(self.tx)
        return dadosPai + meusDados
    
    def __repr__(self):
        dadosPai=super().__str__()
        meusDados=' Tx: {:.3f}%'.format(self.tx)
        return dadosPai + meusDados
    
    def aplicaTaxa(self):
        self.saldo*=(1+self.tx/100)
        return 
    
    def setTaxa(self,tx):
        self.tx=tx
        return
    def getTaxa(self):
        return self.taxa

class ContaEspecial(ContaBancaria):
    def __init__(self,num,nome,senha,limite,saldo=0):
    	#criar uma instância da classe do meu "pai" e 
        # ajustá-la p/minhas particularidades
        super().__init__(num,senha,nome,saldo)
        self.limite=limite
        self.limiteUtilizado=0
        return
    
    def __str__(self):
        dadosPai=super().__str__()
        meusDados=' Limite Utilizado: {:.2f}'.format(self.limiteUtilizado)
        return dadosPai + meusDados
    
    def __repr__(self):
        dadosPai=super().__str__()
        meusDados=' Limite Utilizado: {:.2f}'.format(self.limiteUtilizado)
        return dadosPai + meusDados
    
    
    def setLimite(self,limite):
        self.limite=limite
        return
    
    def deposito(self,valor):
        if valor>0:
            sobra = valor - self.limiteUtilizado 
            if sobra > 0:
                self.limiteUtilizado=0
            else:
               self.limiteUtilizado=abs(sobra)
            self.saldo+=valor
        return valor>0
    
    def saque(self,senha, valor):
        if senha == self.senha:
            resta=self.limite-self.limiteUtilizado
            podetirar= self.saldo+resta
            if valor <= podetirar:
                if self.saldo < 0:
                    sai=valor
                else:
                    sai=valor-self.saldo
                self.limiteUtilizado=self.limiteUtilizado+ sai            
                self.saldo-=valor
                print(self)
                return True
            else:
                print("Cta {} - SALDO INSUFICIENTE".format(self.num))
        return False

cb=ContaCorrente(22,4585,'Daniel',400)
cp=ContaPoupanca(22,14,'Bia',500)
print(cp)
cp.aplicaTaxa()
print(cp)
