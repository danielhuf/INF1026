#1.
def tuplaDeQuesitos(lDesemp,lPeso):
    lTuplas=[]
    for pos,quesito in enumerate(lDesemp):
        lTuplas.append((quesito,lPeso[pos]))
    return tuple(lTuplas)

lq=['Pontos','NumeroDePartidas','Nivel','Vidas']
lp=[2, 10, 1000, 100]
t=tuplaDeQuesitos(lq,lp)

def desempenho(dicRes,tupla):
    novo={}
    for jogador,dicDados in dicRes.items():
        nota_final=0
        for el in tupla:
            nota_final+=el[1]*dicDados[el[0]]
        novo[jogador]=nota_final
    return novo

dicResultadosPorCompetidor = {
 'LALA': {'Pontos':2700,'NumeroDePartidas':20,'Nivel':1,'Vidas':5},
 'DEDE': {'Pontos':2200,'NumeroDePartidas':10,'Nivel':2,'Vidas':7},
 'LILI': {'Pontos':5000,'NumeroDePartidas':22,'Nivel':3,'Vidas':7},
 'LOLO': {'Pontos':4200,'NumeroDePartidas':17,'Nivel':3,'Vidas':4},
 'LULU': {'Pontos':3000,'NumeroDePartidas':17,'Nivel':2,'Vidas':7},
 'DUDU': {'Pontos':1500,'NumeroDePartidas':11,'Nivel':1,'Vidas':5},
 'KAKA': {'Pontos':7000,'NumeroDePartidas':22,'Nivel':4,'Vidas':2},
 'VAVA': {'Pontos':6800,'NumeroDePartidas':27,'Nivel':5,'Vidas':1},
}


dic=desempenho(dicResultadosPorCompetidor,t)
print(dic)

def criaDicInversoParcial(dicRes,lQues):
    novo={}
    for jogador,dicDados in dicRes.items():
        for quesito,pontos in dicDados.items():
            if quesito in lQues:
                dicAuxiliar=novo.get(quesito,{})
                dicAuxiliar[jogador]=pontos
                novo[quesito]=dicAuxiliar       
    return novo

quesitos=['Nível','Vidas','Pontos']
dicResPorQues=criaDicInversoParcial(dicResultadosPorCompetidor,quesitos)
print(dicResPorQues)

def obtemCampeoesDoQuesito(dicRPQ,quesito):
    vencedores=[]
    maior_ponto=-1
    for jogadores,pontos in dicRPQ[quesito].items():
        if pontos>maior_ponto:
            maior_ponto=pontos
    for jogadores,pontos in dicRPQ[quesito].items():
        if pontos==maior_ponto:
            vencedores.append(jogadores)
    return vencedores

print(obtemCampeoesDoQuesito(dicResPorQues,'Vidas'))

def exibePontosCampeoesDoQuesito(dicRes,tupla,quesito):
    lCampeoesQuesito=obtemCampeoesDoQuesito(criaDicInversoParcial(dicRes,quesito),quesito)
    dicPontos=desempenho(dicRes,tupla)
    for jogador in lCampeoesQuesito:
        print('Competidor: %s Nota Final: %d'%(jogador,dicPontos[jogador]))
    return

exibePontosCampeoesDoQuesito(dicResultadosPorCompetidor,t,'Vidas')

#2.
class Data:
    def __init__(self,d,m,a):
        self.dia = d
        self.mes = m
        self.ano = a
        return

    def __str__(self):
        s='{}/{}/{}'.format(self.dia,self.mes,self.ano)
        return s

    def __repr__(self):
        s='{}/{}/{}'.format(self.dia,self.mes,self.ano)
        return s

    # metodo para testar dt1 == dt2: __eq__
    def __eq__(self,outraData):
        return self.ano == outraData.ano and \
        self.mes == outraData.mes and \
        self.dia == outraData.dia

class Pedido:
    def __init__(self,numPedido,nomeCli,lprod,valor):
        self.numeroPed= numPedido
        self.cliente = nomeCli
        self.produtos=lprod
        self.valor = valor
        return
    def __str__(self):
        s= 'PED: %d - CLIENTE: %s - VALOR:%.2f '\
        %(self.numeroPed,self.cliente,self.valor)
        return s
    def __repr__(self):
        s= 'PED: %d - CLIENTE: %s - VALOR:%.2f '\
        %(self.numeroPed,self.cliente,self.valor)
        return s

    def valorASerPago(self):
        if self.valor > 300:
            vp = self.valor - 0.1*self.valor
        else:
            vp = self.valor
        return vp

    def exibeValorASerPago(self):
        s= 'PED:%d - Valor a ser pago:%.2f'\
        %(self.numeroPed,self.valorASerPago())
        print(s)
        return

class PedidoEntregaMarcada(Pedido):
    def __init__(self,numPedido,nomeCli,lprod,valor,dt,tx=15):
        super().__init__(numPedido,nomeCli,lprod,valor)
        self.data=dt
        self.taxa=tx
        return

    def __str__(self):
        return super().__str__() + 'no dia {}'.format(self.data)

    def __repr__(self):
        return super().__str__() + 'no dia {}'.format(self.data)

    def valorASerPago(self):
        return super().valorASerPago() + self.taxa

    def exibeValorASerPago(self):
        s= 'PED:%d - Valor a ser pago:%.2f'\
        %(self.numeroPed,self.valorASerPago())
        print(s)
        return

    def mesmaDataDeEntrega(self,outro):
        if self.data==outro.data:
            print('Pedidos com mesma data: {}'.format(self.data))
            print(self)
            print(outro)
        else:
            print('Pedidos com datas de entrega diferentes.')

pem1= PedidoEntregaMarcada(2222,'vik',[34,12,67],326.90, Data(12,5,2019), 20.10)
print(pem1)
pem1.exibeValorASerPago()
pem2=PedidoEntregaMarcada(8888,'bob',[20,12],230.90, Data(12,5,2019))
print(pem2)
pem2.exibeValorASerPago()
pem3=PedidoEntregaMarcada(5555,'zoe',[23,44,67,57],510.90, Data(29,4,2019),30.70)
print(pem3)
print('\n')
pem1.mesmaDataDeEntrega(pem2)
pem1.mesmaDataDeEntrega(pem3)

    
        
        
    
    

        
