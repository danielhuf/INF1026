#Criando classes!

class Pessoa:
    respiracao='PULMONAR'   #atributo de classe
    #criei uma constante para todos o objetos
    #existe independentemente da existencia de objetos

    #o self é como uma auto referência
    
    def __init__(self,no,idad,nac='brasileira'):   
        #Primeiramente, há o método construtor
        #init é um método mágico
        #se a nacionalidade nao for fornecida, usa-se o valor default do atributo
        #VALORES DEFAULLT SEMPRE NO FINAL DO METODO
        self.nome=no
        self.idade=idad
        self.nacionalidade=nac
        return

    #os dois métodos abaixo sao métodos operacionais
    def apresentarSe(self):
        print('Sou',self.nome,'e tenho',self.idade,'anos')
        return

    def fazAniversario(self):
        self.idade+=1
        return
    
    #metodo magico (especial): __str__
    #metodo a ser chamado implicitamente ao se dar print
    def __str__(self):
        s='{} - {} anos - {}'.format(self.nome,self.idade,self.nacionalidade)
        #as chaves serão substituídas pelo formato
        return s
    
    #metodo para obter string que seja a 
    #representacao interna do objeto
    #trata-se de uma apresentação mais profunda do objeto
    def __repr__(self):
        s='{} - {} anos - {}'.format(self.nome,self.idade,self.nacionalidade)
        return s
    
    #metodo para testar se é maior do que
    #outra pessoa (um criterio deve ser adotado)
    #mais velho significa maior
    #gt=greater than
    def __gt__(self,outra):
        return self.idade>outra.idade

    #metodo para "somar duas pessoas: considerando que a "soma"
    #de duas pessoas crie uma pessoinha (um filhinho)
    #apenas para efeito didatico
    def __add__(self,outra):
        fi=Pessoa(self.nome[0:2]+outra.nome[2:4],0)
        #criei outra pessoa com o nome somado e 0 anos de idade
        return fi
#-------------------------------------------------------------------------  
            
pe1=Pessoa('BUBA',24)
pe2=Pessoa('NANA',18)

print(pe1.nome)
print(pe1.idade)

pe1.apresentarSe()
pe2.apresentarSe()

pe1.fazAniversario()
pe1.apresentarSe()

print(pe1)
print(pe2)

print(pe1>pe2)  #igual a pe1.__gt__(pe2) 
print(pe1.__gt__(pe2))
print(pe2>pe1) 
print(pe2<pe1)  

x=pe1+pe2
print(x)
print(pe1.__add__(pe2))

pe3=Pessoa('MIKE',43,'australiana')
print(pe3)

lpessoas=[pe1,pe2,pe3,Pessoa('GEGE',24,'francesa')]
#se não existisse o método repr, printaria os formatos originais dos objetos
print(lpessoas)

print(pe1.respiracao)
print(pe2.respiracao)

#----------------------------------------------------------------------------

class Usuario:
    def __init__(self,tip,log,sen):
        self.tipo=tip
        self.login=log
        self.senha=sen
        return
    def Autenticar(self):
        print(self.tipo,'de login',self.login,'entrou')
        return
