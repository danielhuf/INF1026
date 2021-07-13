#Nome completo: Daniel Stulberg Huf
#Matrícula PUC-Rio: 1920468
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim,
#sem consultas a outros alunos, professores ou qualquer outra pessoa.

#Nessa primeira classe, a única coisa que não fiz foi colocar o :s dentro das primeiras chaves no __str__,
#sendo que isso não alterou em nada o programa e perdi 0.1 por isso.
class Servico:
    def __init__(self,d,v):
        self.descricao=d
        self.valorHora=v
        return
    
    def __str__(self):
        return '{}: R${:.2f} p/h'.format(self.descricao,self.valorHora)

    def __repr__(self):
        return '{}: R${:.2f} p/h'.format(self.descricao,self.valorHora)

#Da mesma maneira, nessa segunda classe só não coloquei o :s e também perdi 0.1 ponto.
class Fornecedor:
    def __init__(self,n,e):
        self.nome=n
        self.email=e
        return

    def __str__(self):
        return '{} ({})'.format(self.nome,self.email)

    def __repr__(self):
        return '{} ({})'.format(self.nome,self.email)

#Nessa classe Contato, em vez de criar o objeto Servico no construtor, eu o criei dentro do método __str_ e perdi 0.1 ponto.
#Não sei se é aceitável fazer dessa maneira, mas a execução do programa em si está igual ao gabarito.
class Contato(Fornecedor):
    def __init__(self,n,e,d,v):
        super().__init__(n,e)
        self.descricao=d
        self.valorHora=v
        return

    def __str__(self):
        return super().__str__() + ' - ' + Servico(self.descricao,self.valorHora).__str__() + '\n'

    def __repr__(self):
        return super().__str__() + ' - ' + Servico(self.descricao,self.valorHora).__str__() + '\n'

class Agenda:
    def __init__(self,dic={}):
        self.contatos=dic
        return

    def inclui(self,nome,email,descricao,valorHora):
        self.contatos[nome]=Contato(nome,email,descricao,valorHora)
        return

    def __str__(self):
        s=''
        for contato,dados in self.contatos.items():
            s+=dados.__str__()
        return s

    def __repr__(self):
        s=''
        for contato,dados in self.contatos.items():
            s+=dados.__str__()
        return s

print('----------Testando a classe Agenda----------\n')
agenda=Agenda()
agenda.inclui('Ze Eletricos','zeeletricos@email.com','Troca Lâmpadas',150.00)
agenda.inclui('LimpGlass','limpinho@servidor.com.br','Limpeza de vidros',30.00)
print(agenda)
