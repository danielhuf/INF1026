#1
def calculaPrecoFinal(p,d):
    final=((100-d)/100)*p
    return final

num=0
n=int(input('Número total de livros: '))
while num<n:
    nome=input('Titulo do livro: ')
    preco=float(input('Preço do livro: '))
    desc=float(input('Percentual de desconto: '))
    final=calculaPrecoFinal(preco,desc)
    print('Nome do livro: ',nome)
    print('Preço final: R$%.2f'%final)
    num+=1
#2
def livrosDaLista(lista):
    for el in lista:
        l=el.split()
        des=float(l[-1])
        prec=float(l[-2])
        tit=' '.join(l[:-2]).upper()
        f=calculaPrecoFinal(prec,des)
        print(tit.upper())
        print(f)
    return

lstLivros=['A Flor Oculta 40.8 5','NOITE E DIA SEM DORMIR 100.50 10','SONHOS 60 3.5','Espelho Velho 56 15']

livrosDaLista(lstLivros)

#3
def leLivrosArq(a):
    l=list()
    arq=open(a,'r')
    for linha in arq:
        info=linha.strip()
        l.append(info)
    arq.close()
    return l

print(leLivrosArq('livrosbase.txt'))
