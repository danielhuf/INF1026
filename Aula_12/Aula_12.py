#Exercicio de Acompanhamento
#Representando as datas

from datetime import date

class DataSimplificada:
    def __init__(self,dia=date.today().day,mes=date.today().month,ano=date.today().year):
        self.dia=int(dia)
        self.mes=int(mes)
        self.ano=int(ano)

    def __str__(self):
        return '{:0>2d}/{:0>2d}/{:4d}'.format(self.dia,self.mes,self.ano)

    def __repr__(self):
        return '{:0>2d}/{:0>2d}/{:4d}'.format(self.dia,self.mes,self.ano)

    def __eq__(self,dt):  #Verificar que as datas são as mesmas
        return(self.dia==dt.dia and self.mes==dt.mes and self.ano==dt.ano)

    def __lt__(self,dt):
        return (self.ano<dt.ano or self.ano==dt.ano and self.mes<dt.mes or self.ano==dt.ano and self.mes==dt.mes and self.dia<dt.dia)

    def clone(self): #Construir nova data com mesmos valores
        return (DataSimplificada(self.dia,self.mes,self.ano))

    def DataAposIntervDias(self,x=20): #Data após x dias
        dias=(31,28,31,30,31,30,31,31,30,31,30,31)
        d=self.dia+x
        m=self.mes
        a=self.ano
        if d>dias[m-1]:
            d-=dias[m-1]
            m+=1
        if m>12:
            m=1
            a+=1
        return DataSimplificada(d,m,a)

class ContaAPagar():
    def __init__(self,identif=' ',dtVenc=DataSimplificada(),valor=0):
        self.ident=identif
        self.dtVenc=dtVenc.clone()
        self.valor=valor
        return

    def __str__(self):
        return 'Conta:{} - Dt Vencimento:{} - Valor R${:.2f}'.format(self.ident,self.dtVenc,self.valor)

    def __repr__(self):
        return 'Conta:{} - Dt Vencimento:{} - Valor R${:.2f}'.format(self.ident,self.dtVenc,self.valor)

    def __eq__(self,cta):
        return (self.ident==cta.ident and self.dtVenc==cta.dtVenc and self.valor==cta.valor)

    def __lt__(self,cta):
        dt1=self.getDtVenc()
        dt2=cta.getDtVenc()
        return(dt1<dt2 or dt1==dt2 and self.getValor()<cta.getValor())   #se as datas forem iguais, considere o valor que for menor

    def estaVencida(self):
        hj=DataSimplificada()
        return hj>self.dtVenc

    def venceEmXDias(self,x=10):
        if self.estaVencida():
            return False
        dt=DataSimplificada().DataAposIntervDias(x)
        return self.dtVenc<dt or self.dtVenc==dt

    def setIdent(self,x):
        self.ident=x
        return

    def setDtVenc(self,dt):
        self.dtVenc=dt
        return

    def setValor(self,v):
        if v>0:
            self.valor=v
        return

    def getIdent(self):
        return self.ident


    def getdtVenc(self):
        return self.dtVenc


    def getValor(self):
        return self.valor

lContas=[ContaAPagar('Luz',DataSimplificada(10,5,2020)),ContaAPagar('Água',DataSimplificada(5,5,2020)),ContaAPagar('ParcelaAp',DataSimplificada(21,4,2020)),
         ContaAPagar('EntradaAp',DataSimplificada(5,12,2020)),ContaAPagar('Condomínio',DataSimplificada(21,4,2020))]

print('----------Exibindo todas as contas----------')
for obj in lContas:
    print(obj)

print('----------Exibindo as contas que vencem amanhã----------')
for obj in lContas:
    if obj.venceEmXDias(1):
        print(obj)


    
