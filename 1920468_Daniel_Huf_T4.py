#Daniel Stulberg Huf
#matr. 1920468
#Turma 33C, prof. Joísa

def precoTotal(lista,dic):
    v_mensal=0
    for el in lista:
        v_mensal+=dic.get(el,0.0)
        if el not in dic.keys():
            print('A atividade',el,'não existe')
    return v_mensal

dativ={'ioga':120.0,'spinning':100,'musculacao':150,
       'judo':150,'alongamento':120,'aerobica':120,
       'todas':420}

lativ=['ioga','judo','futebol','natacao']
p=precoTotal(lativ,dativ)
print('Valor Total Mensal: R$%.2f'%p)
        