from datetime import datetime

class Horario:
    def __init__(self, h='',m=0,s=0):
        if h=='':
            h=datetime.now().hour
            m=datetime.now().minute
            s=datetime.now().second
        self.hora = int(h)
        self.min = m
        self.seg = s
        self.tempo = self.hora*3600+self.min*60 + self.seg
        return
    def __str__(self): 
        return "{:0>2d}:{:0>2d}:{:0>2d}".format(self.hora, self.min,self.seg)
    def __repr__(self): 
        return "{:0>2d}:{:0>2d}:{:0>2d}".format(self.hora, self.min,self.seg)

  
    def __add__(self,outro):
        tot=abs(self.tempo+outro.tempo)
        return self.geraHorario(tot)
    def __sub__(self,outro):
        dif=abs(self.tempo-outro.tempo)
        return self.geraHorario(dif)
    def __eq__(self,outro):
        return(self.tempo==outro.tempo)
    def __ne__(self,outro):
        return(self.tempo != outro.tempo)
    def __lt__(self,outro):
        return(self.tempo<outro.tempo)
    def __gt__(self,outro):
        return(self.tempo>outro.tempo)
    
    def setSeg(self,s):
        self.seg=s
        self.tempo = self.hora*3600+self.min*60 + self.seg
    def setMin(self,m):
        self.min=m
        self.tempo = self.hora*3600+self.min*60 + self.seg
    def setHora(self,h):
        self.hora=h
        self.tempo = self.hora*3600+self.min*60 + self.seg
    def getSeg(self):
        return self.seg
    def getMin(self):
        return self.min
    def getHora(self):
        return self.hora
    
    # funções auxiliares
    def geraHorario(self,tempo):
        h=tempo//3600
        m=tempo%3600//60
        s=tempo%3600%60
        return Horario(h,m,s)
    def totSegundos(self):
        return self.tempo
    def totMinutos(self):
        return self.tempo/60
    def totHoras(self):
        return self.tempo/3600
