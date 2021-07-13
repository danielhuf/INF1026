#2.1)
from classeAvaliacaoBio import AvaliacaoBio

class Candidato:
    def __init__(self,num,nom,ida,ava):
        self.inscr=num
        self.nome=nom
        self.idade=ida
        self.aval=ava
        return

    def __str__(self):
        return 'Nome:{} - Idade:{:3d} - Inscrição:{} - Avaliação Biométrica:{}'.format(self.nome,self.idade,self.inscr,self.aval)

    def getNotaBio(self):
        return self.aval.detAval()

#2.2)
class Concurso:
    def __init__(self,car,ima,imi,nb,can=[]):
        self.cargo=car
        self.idadeMaxima=ima
        self.idadeMinima=imi
        self.notaBiomedica=nb
        self.candidatos=can
        return

    def __str__(self):
        return 'Cargo: {} - Idade Maxima: {} - Idade Minima: {} - Nota Biomedica: {} - Candidatos: {}'.format(self.cargo,self.idadeMaxima,self.idadeMinima,self.notaBiomedica,self.candidatos)

    def getCargo(self):
        return self.cargo

    def getIdadeMaxima(self):
        return self.idadeMaxima

    def getIdadeMinima(self):
        return self.idadeMinima

    def getNotaBiomedica(self):
        return self.notaBiomedica

    def getCandidatos(self):
        return self.candidatos

    def setCargo(self,novo):
        self.cargo=novo
        return

    def setIdadeMaxima(self,novo):
        self.idadeMaxima=novo
        return

    def setIdadeMinima(self,novo):
        self.idadeMinima=novo
        return

    def setNotaBiomedica(self,tupla):
        self.notaBiomedica=tupla
        return

    def incluiCand(self,c):
        self.candidatos.append(c)
        return

    def mostraAptos(self):
        print('Candidatos aptos para o cargo:')
        for el in self.candidatos:
            if self.idadeMinima<=el.idade and el.idade<=self.idadeMaxima and el.getNotaBio() in self.notaBiomedica:
                print(el)
        return

#2.3)
#a)
concurso=Concurso('Comissário de bordo',40,21,('magreza','normal'))

#b)
lCand=[Candidato(111,"bia",27, AvaliacaoBio(1.80,40.0)),Candidato(222,"edu",37, AvaliacaoBio (1.80,86.0 )),Candidato(333,"leo",24, AvaliacaoBio (1.75,91.0 )),
       Candidato(666,"rui",53, AvaliacaoBio (1.90,70.0)),Candidato(555,"vik",18, AvaliacaoBio (1.50,150.0) ),Candidato(888,"ana",20, AvaliacaoBio (1.60,55.6)),
       Candidato(444,"teo",26, AvaliacaoBio (1.70,70.0 )),Candidato(777,"lia",18, AvaliacaoBio (1.65,105.4))]

for obj in lCand:
    concurso.incluiCand(obj)

#c)
resultado=concurso.mostraAptos()

#3)
class Livros:
    def __init__(self,n,a,l,isbn,d,num):
        self.nome=n
        self.assunto=a
        self.listaAutores=l
        self.ISBN=isbn
        self.dataPubli=d
        self.numPag=num
        return

    def __str__(self):
        return 'Nome: {} - Assunto: {} - lista de Autor(es): {} - ISBN: {} - data de publicação: {} - no. de páginas: {}'.format(self.nome,self.assunto,self.listaAutores,self.ISBN,self.dataPubli,self.numPag)

    def __eq__(self,outro):
        return self.ISBN==outro.ISBN

    def __ne__(self,outro):
        return self.ISBN!=outro.ISBN

    def __gt__(self,outro):   #se é mais recente, é maior
        ano_a=int(self.dataPubli[6:])
        ano_b=int(outro.dataPubli[6:])
        mes_a=int(self.dataPubli[3:5])
        mes_b=int(outro.dataPubli[3:5])
        dia_a=int(self.dataPubli[:2])
        dia_b=int(outro.dataPubli[:2])
        if ano_a>ano_b or ano_a==ano_b and mes_a>mes_b or ano_a==ano_b and mes_a==mes_b and dia_a>dia_b:
            return True
        else:
            return False

    def __lt__(self,outro):   #se é mais recente, é maior
        ano_a=int(self.dataPubli[6:])
        ano_b=int(outro.dataPubli[6:])
        mes_a=int(self.dataPubli[3:5])
        mes_b=int(outro.dataPubli[3:5])
        dia_a=int(self.dataPubli[:2])
        dia_b=int(outro.dataPubli[:2])
        if ano_a<ano_b or ano_a==ano_b and mes_a<mes_b or ano_a==ano_b and mes_a==mes_b and dia_a<dia_b:
            return True
        else:
            return False

    def getNome(self):
        return self.nome

    def getAssunto(self):
        return self.assunto

    def getListaAutores(self):
        return self.listaAutores

    def getISBN(self):
        return self.ISBN

    def getDataPubli(self):
        return self.dataPubli

    def getNumPag(self):
        return self.numPag

    def setNome(self,valor):
        self.nome=valor

    def setAssunto(self,valor):
        self.assunto=valor

    def setListaAutores(self,valor):
        self.listaAutores=valor

    def setISBN(self,valor):
        self.ISBN=valor

    def setDataPubli(self,valor):
        self.dataPubli=valor

    def setNumPag(self,valor):
        self.numPag=valor

    def clone(self):
        return (Livros(self.nome,self.assunto,self.listaAutores,self.ISBN,self.dataPubli,self.numPag))

livro1=Livros('A procura','Drama',['Daniel','Claudia'],2206,'08/02/2008',152)
livro2=Livros('A chegada','Drama',['Daniel','Claudia'],2402,'08/11/2008',200)
print(livro1)
print(livro2>livro1)
livro1.setNome('O sol')
print(livro1)

#4)
from classeHorario import Horario
from classeDataCompleta import Data

class EntradaEvento:
    def __init__(self,dt,hr,dr,sl,vl):
        self.dataDoEvento=dt
        self.horario=hr
        self.duracao=dr
        self.sala=sl
        self.valor=vl
        return

    def __str__(self):
        return 'Data do evento: {} - Horário: {} - Duração: {} minutos - Sala: {} - Valor do ingresso: R${:.2f}'.format(self.dataDoEvento,self.horario,self.duracao,self.sala,self.valor)
    
    def __repr__(self):
        return 'Data do evento: {} - Horário: {} - Duração: {} minutos - Sala: {} - Valor do ingresso: R${:.2f}'.format(self.dataDoEvento,self.horario,self.duracao,self.sala,self.valor)

    def __eq__(self,outro):
        return self.horario==outro.horario and self.sala==outro.sala

    def __ne__(self,outro):
        if self.horario==outro.horario and self.sala==outro.sala:
            return False
        return True

    def __gt__(self,outro):   #o self é maior se ele vier antes do outro
        if self.dataDoEvento==outro.dataDoEvento:
            return self.horario<outro.horario
        return self.dataDoEvento<outro.dataDoEvento

    def __lt__(self,outro):   #o self é menor se ele vier depois do outro
        if self.dataDoEvento==outro.dataDoEvento:
            return self.horario>outro.horario
        return self.dataDoEvento>outro.dataDoEvento

    def getDataDoEvento(self):
        return self.dataDoEvento

    def getHorario(self):
        return self.horario

    def getDuracao(self):
        return self.duracao

    def getSala(self):
        return self.sala

    def getValor(self):
        return self.valor

    def setDataDoEvento(self,valor):
        self.dataDoEvento=valor
        return

    def setHorario(self,valor):
        self.horario=valor
        return

    def setDuracao(self,valor):
        self.duracao=valor
        return

    def setSala(self,valor):
        self.sala=valor
        return

    def setValor(self,valor):
        self.valor=valor
        return

    def clone(self):
        return (EntradaEvento(self.dataDoEvento,self.horario,self.duracao,self.sala,self.valor))

    def comDesconto(self,n):
        return (((100-n)/100)*self.valor)

e1=EntradaEvento(Data(20,4,2020),Horario(16,30),90,'32F',30)
print(e1)
e2=EntradaEvento(Data(24,4,2020),Horario(16,30),90,'30F',30)
print(e1!=e2)
print(e2<e1)
print(e1.getHorario())
e1.setHorario(Horario(14))
print(e1.getHorario())
print(e1.comDesconto(25))
print(e1)

#5.1)
class Endereco():

    def __init__(self,rua,num,cid,bairro='',ap='',cpl=''):
        self.rua=rua
        self.num=num
        self.apto=str(ap)
        self.compl=cpl
        self.bairro= bairro
        self.cid = cid
        return

    def __str__(self):
        # Monta uma string com os dados existentes do endereço
        end='{}, {}'.format(self.rua,self.num)
        if len(self.apto) > 0:
            end = '{} ap {}'.format(end,self.apto)
        if len(self.compl)>0:
            end = '{}, {}'.format(end,self.compl)
        if len(self.bairro)>0:
            end = '{} - {}'.format(end,self.bairro)
        end='{}\n {}'.format(end,self.cid)
        
        return end

    def __repr__(self):
        # Monta a representação interna  com atributos válidos
        end='{}, {}'.format(self.rua,self.num)
        if len(self.apto) > 0:
            end = '{} ap {}'.format(end,self.apto)
        if len(self.compl)>0:
            end = '{}, {}'.format(end,self.compl)
        if len(self.bairro)>0:
            end = '{} - {}'.format(end,self.bairro)
        end='{}\n{}'.format(end,self.cid)
        
        return end

    
    def __eq__(self,outro):
        ''' recebe outro Endereco e retorna True se mesmos atributos'''
        
        return (self.rua==outro.rua and 
                self.num == outro.num and
                self.apto==outro.apto and
                self.compl==outro.compl and
                self.bairro== outro.bairro and
                self.cid == outro.cid)
    
    def getBairro(self):
        return self.bairro

    def getCidade(self):
        return self.cid

    def mesmoBairro(self,outro):
        return self.bairo == outro.bairro

    def mesmaCidade(self,outro):
        return self.cid == outro.cid

    def copiaValores(self,outro):
        ''' altera atributos com valores de outro'''
        self.rua=outro.rua
        self.num = outro.num
        self.apto=outro.apto
        self.compl=outro.compl
        self.bairro=outro.bairro
        self.cid = outro.cid
        return


class Imovel:
    def __init__(self,matr,end,area,pr,prop):
        self.matr=matr
        self.end=end
        self.area=area
        self.preco=pr
        self.prop=prop
        return

    def __str__(self):
        return 'Indentificação do imóvel: {} - Endereço do imóvel: {} - Área do imóvel: {} - Valor do imóvel: R${:.2f} - Nome do proprietário - {}'.format(self.matr,self.end,self.area,self.preco,self.prop)
    
    def __repr__(self):
        return 'Indentificação do imóvel: {} - Endereço do imóvel: {} - Área do imóvel: {} - Valor do imóvel: R${:.2f} - Nome do proprietário - {}'.format(self.matr,self.end,self.area,self.preco,self.prop)
    
    def __eq__(self,outro):
        return self.preco==outro.preco

    def __ne__(self,outro):
        return self.preco!=outro.preco

    def __lt__(self,outro):
        if self.area==outro.area:
            return self.preco<outro.preco
        return self.area<outro.area

    def __gt__(self,outro):
        if self.area==outro.area:
            return self.preco>outro.preco
        return self.area>outro.area

    def getMatr(self):
        return self.matr

    def getEnd(self):
        return self.end

    def getArea(self):
        return self.area

    def getPreco(self):
        return self.preco

    def getProp(self):
        return self.prop

    def setMatr(self,valor):
        self.matr=valor
        return

    def setEnd(self,valor):
        self.end=valor
        return

    def setArea(self,valor):
        self.area=valor
        return

    def setPreco(self,valor):
        self.preco=valor
        return

    def setProp(self,valor):
        self.prop=valor
        return

    def getLocal(self):
        return (self.end.bairro,self.end.cid)

    def mesmoLocal(self,outro):
        return self.getLocal()==outro.getLocal()

i1=Imovel(24,Endereco('Sorocaba',60,'RJ','Botafogo',180,'Bloco B'),500,400,'José')
print(i1)
i2=Imovel(24,Endereco('Redentor',60,'RJ','Botafogo',180,'Bloco B'),250,20,'Maria')
print(i2)
print(i1>i2)
print(i1.getPreco())
i1.setPreco(300)
print(i1.getPreco())
print(i1.getLocal())
print(i1.mesmoLocal(i2))

#5.2)
def exibeNoMesmoLocal(dicI,bairro,cidade):
    tupla=(bairro,cidade)
    for num,imovel in dicI.items():
        if imovel.getLocal()==tupla:
            print(imovel)
    return

def separaNoMesmoLocal(dicI,mat):
    lista=[]
    for num,imovel in dicI.items():
        if num!=mat:   #estou excluindo o prorpio imovel com o numero
            if imovel.getLocal()==dicI[mat].getLocal():
                lista.append(imovel)
    return lista

def separaMenoresNoMesmoLocal(dicI,mat):
    lista=[]
    for num,imovel in dicI.items():
        if num!=mat:
            if imovel.getLocal()==dicI[mat].getLocal() and imovel<dicI[mat]:
                lista.append(imovel)
    return lista
            
dImovel = {
10:Imovel(matr=10,area=178,pr=355853.00,prop='zezinho',end=Endereco(rua='Rua 2',num=253,ap='201',cpl='Bl2',bairro='Feio',cid='Rio')),
21:Imovel(matr=21,area=295,pr=381596.00,prop='luisinho',
end=Endereco(rua='Rua 3',num=108,ap='202',cpl='Bl2',bairro='Lindo',cid='Rio')),
34:Imovel(matr=34,area=32,pr=614578.00,prop='luisinho',
end=Endereco(rua='Rua 2',num=84,ap='101',cpl='',bairro='Belo',cid='Petrópolis')),
47:Imovel(matr=47,area=85,pr=597878.00,prop='luisinho',
end=Endereco(rua='Rua 3',num=708,ap='301',cpl='',bairro='Belo',cid='Niterói')),
56:Imovel(matr=56,area=299,pr=538577.00,prop='zezinho',
end=Endereco(rua='Rua 2',num=98,ap='201',cpl='Bl2',bairro='Lindo',cid='Petrópolis')),
61:Imovel(matr=61,area=32,pr=207581.00,prop='luisinho',
end=Endereco(rua='Rua 4',num=416,ap='302',cpl='Bl1',bairro='Belo',cid='Petrópolis')),
70:Imovel(matr=70,area=78,pr=256300.00,prop='luisinho',
end=Endereco(rua='Rua 2',num=792,ap='102',cpl='Bl2',bairro='Feio',cid='Petrópolis')),
82:Imovel(matr=82,area=170,pr=418803.00,prop='luisinho',
end=Endereco(rua='Rua 3',num=780,ap='301',cpl='',bairro='Belo',cid='Petrópolis')),
94:Imovel(matr=94,area=231,pr=785373.00,prop='huguinho',
end=Endereco(rua='Rua 3',num=444,ap='302',cpl='Bl1',bairro='Lindo',cid='Rio')),
102:Imovel(matr=102,area=258,pr=629655.00,prop='luisinho',
end=Endereco(rua='Rua 2',num=659,ap='',cpl='',bairro='Feio',cid='Rio')),
110:Imovel(matr=110,area=138,pr=632818.00,prop='zezinho',
end=Endereco(rua='Rua 4',num=96,ap='',cpl='',bairro='Feio',cid='Rio')),
121:Imovel(matr=121,area=187,pr=557090.00,prop='luisinho',
end=Endereco(rua='Rua 1',num=170,ap='101',cpl='Bl2',bairro='Belo',cid='Niterói')),
134:Imovel(matr=134,area=270,pr=100917.00,prop='huguinho',
end=Endereco(rua='Rua 2',num=642,ap='302',cpl='Bl1',bairro='Feio',cid='Niterói')),
143:Imovel(matr=143,area=342,pr=372894.00,prop='luisinho',
end=Endereco(rua='Rua 1',num=554,ap='102',cpl='Bl1',bairro='Belo',cid='Rio')),
158:Imovel(matr=158,area=56,pr=690446.00,prop='zezinho',
end=Endereco(rua='Rua 1',num=1,ap='301',cpl='',bairro='Lindo',cid='Rio')),
166:Imovel(matr=166,area=204,pr=270209.00,prop='luisinho',
end=Endereco(rua='Rua 2',num=70,ap='101',cpl='Bl2',bairro='Lindo',cid='Niterói')),
177:Imovel(matr=177,area=125,pr=560384.00,prop='luisinho',
end=Endereco(rua='Rua 4',num=610,ap='',cpl='',bairro='Lindo',cid='Niterói')),
189:Imovel(matr=189,area=18,pr=503935.00,prop='luisinho',
end=Endereco(rua='Rua 1',num=216,ap='201',cpl='Bl2',bairro='Belo',cid='Petrópolis')),
195:Imovel(matr=195,area=125,pr=344284.00,prop='luisinho',
end=Endereco(rua='Rua 2',num=167,ap='201',cpl='',bairro='Belo',cid='Niterói')),
209:Imovel(matr=209,area=96,pr=715545.00,prop='zezinho',
end=Endereco(rua='Rua 1',num=434,ap='302',cpl='Bl1',bairro='Feio',cid='Rio'))}

exibeNoMesmoLocal(dImovel,'Belo','Petrópolis')
print(separaNoMesmoLocal(dImovel,21))
print(separaMenoresNoMesmoLocal(dImovel,34))

        
        
