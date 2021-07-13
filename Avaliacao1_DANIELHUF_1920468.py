#Nome completo: Daniel Stulberg Huf
#Matrícula PUC-Rio: 1920468
#Declaração de autoria: Declaro que este documento foi produzido em sua totalidade por mim, sem consultas
#a outros alunos, professores ou qualquer outra pessoa.

#1a)
def entrevista(n):
    entrevistados=0
    n_mulheres=0
    mulheres_B=0
    n_homens=0
    homens_B=0
    while entrevistados<n:
        print('Bem vindo à pesquisa de mercado sobre os produtos A e B!')
        sexo=input('Digite ''F'' para sexo feminino e ''M'' para masculino: ')
        resposta=input('Qual produto você prefere: ''A'' ou ''B''? Digite sua resposta: ')
        print('Obrigada por participar!\n')
        if sexo=='F':
            n_mulheres+=1
            if resposta=='B':
                mulheres_B+=1
        else:
            n_homens+=1
            if resposta=='B':
                homens_B+=1
        entrevistados+=1
    return (n_mulheres,mulheres_B,n_homens,homens_B)

#1b)
def exibePesquisa(tupla):
    percent_mulheres=tupla[1]/tupla[0]
    percent_homens=tupla[3]/tupla[2]
    if percent_mulheres==percent_homens:
        print('Os homens entrevistados têm a mesma opinião que as mulheres')
    else:
        print('Os homens entrevistados não têm a mesma opinião que as mulheres')
    return

num=int(input('Entre com a quantidade de entrevistados: '))
t=entrevista(num)
exibePesquisa(t)
