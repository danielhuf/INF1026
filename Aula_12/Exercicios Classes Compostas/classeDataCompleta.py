from datetime import date

class Data:
    def __init__(self, dia=date.today().day,mes=date.today().month,ano=date.today().year):
        self.ano = ano
        self.mes = mes
        self.dia = dia
        if not self.isMesValido(mes) or not self.isDiaValido(dia):
            self.ano = 1
            self.mes = 1
            self.dia = 1
        self.djul=self.convDataDiaJuliano(self.dia,self.mes,self.ano)

    def __str__(self): 
        return "{:0>2d}/{:0>2d}/{:0>4d}".format(self.dia, self.mes,self.ano)
    
    def __repr__(self): 
        return "{:0>2d}/{:0>2d}/{:0>4d}".format(self.dia, self.mes,self.ano)

    def __sub__(self, outra): # dias entre duas datas
        djnovo=abs(self.djul-outra.djul)
        return (djnovo)
    
    def __add__(self,x=20): # data após/antes x dias
        djnovo=self.djul+x
        (d,m,a)=self.convDiaJulianoData(djnovo)
        return Data(d,m,a)    

    def __eq__(self,outra):
        return(self.djul==outra.djul)
    def __neq__(self,outra):
        return(self.djul!=outra.djul)
    def __lt__(self,outra):
        return(self.djul <outra.djul)
    def __gt__(self,outra):
        return(self.djul> outra.djul)


    def isBissexto(self):
        ano=self.ano
        return ano%4==0 and (ano%100!=0 or ano%400==0)

    def clone(self):
        return self.__init__(self.dia,self.mes,self.ano)

    def getMes(self):
        return self.mes
    def getAno(self):
        return self.ano
    def getDia(self):
        return self.dia
    def getMesExtenso(self):
        tMeses=('Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez')
        return tMeses(self.getMes()-1)
    
    def setMes(self, m):
        mes = self.mes
        if self.isMesValido(m):
            self.mes=m
            if not self.isDiaValido(self.dia): # mes tornou o dia invalido
                self.mes=mes
            else:
                self.djul=convDataDiaJuliano(self.dia,self.mes,self.ano)
        return
    
    def setAno(self,a):
        self.ano=a
        self.djul=convDataDiaJuliano(self.dia,self.mes,self.ano)
        return
    
    def setDia(self,d):
        if self.isDiaValido(d):
            self.dia=d
            self.djul=convDataDiaJuliano(self.dia,self.mes,self.ano)
        return 

    def detInterv(self,x=20):
        djnovo=self.djul+x
        (d,m,a)=self.convDiaJulianoData(djnovo)
        return Data(d,m,a)
    
    #AUXILARES
    def isMesValido(self,mes):
        return mes>0 and mes<13

    def isDiaValido(self,dia):
        tDias=(31,28,31,30,31,30,31,31,30,31,30,31)
        mes= self.getMes()
        if mes==2:
            if self.isBissexto():
                maior=28
            else:
                maior=29
        else:
            maior = tDias[mes-1]
        return dia>0 and dia<maior
    
    def convDataDiaJuliano(self,dia,mes,ano):
        if mes < 3:
            ano=ano+1
            mes=mes+12
        A=int(ano/100)
        B=int(A/4)
        C=2-A+B
        D = int(365.25 * (ano + 4716))
        E = int(30.6001 * (mes + 1))
        F = D + E + dia + 0.5 + C - 1524.5
        return int(F)

    def convDiaJulianoData(self,juliano):
        A = juliano
        if A > 2299160:
            B =int((A - 1867216.25) / 36524.25)
            C = A + 1 + B - int(B / 4)
        else:
            C = A
        D = C + 1524
        E = int((D - 122.1) / 365.25)
        F = int(E * 365.25)
        G = int((D - F) / 30.6001)
        H = D - F - int(G * 30.6001)
        if G < 14:
            I = G - 1
        else:
            I = G - 13
        if I > 2:
            J = E - 4716
        else:
            J = E - 4715
        if J > 0:
            K = J
        else:
            K = abs(J + 1)
        return(H,I,K)
 
