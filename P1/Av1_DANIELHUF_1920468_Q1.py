
#Nome completo: Daniel Stulberg Huf
#Matrícula PUC-Rio: 1920468
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim,
#sem consultas a outros alunos, professores ou qualquer outra pessoa.

#a)
def criaDicPaisComemoracao(tupla):
    novo={}
    for (pais,comemoracao,data) in tupla:
        dicAux=novo.get(pais,{})
        lAux=dicAux.get(data,[])
        lAux.append(comemoracao)
        dicAux[data]=lAux
        novo[pais]=dicAux
    return novo

#b)
def criaDicDataCome(dicPaises):
    inverso={}
    for pais,dicDatas in dicPaises.items():
        for data,l_comemoracao in dicDatas.items():
            for comemoracao in l_comemoracao:
                dicAux=inverso.get(data,{})
                lAux=dicAux.get(comemoracao,[])
                lAux.append(pais)
                dicAux[comemoracao]=lAux
                inverso[data]=dicAux
    return inverso

#c)
def obtemPaises(dicCome,data,comemoracao):
    d=dicCome.get(data,'Nenhuma comemoração nesta data')
    if type(d) is dict:
        d=d.get(comemoracao,'Nenhum país tem essa comemoração nesta data')
        if type(d) is list:
            d=len(d)
    print(d)
    return

#d)
print('----------Testando o programa----------')

tComemoracoes = (('Brasil', 'Dia do Amigo', '18/04'), ('Argentina', 'Dia da Primavera', '21/09'), ('Brasil', 'Dia dos Pais', '09/08'),
 ('Brasil', 'Dia da Primavera', '22/09'), ('Argentina', 'Dia do Amigo', '20/07'), ('Brasil', 'Dia das Crianças', '12/10'),
 ('Argentina', 'Dia das Mães', '18/10'), ('Argentina', 'Dia dos Pais', '21/06'), ('Argentina', 'Dia das Crianças', '09/08'),
 ('Argentina', 'Dia dos Namorados', '14/02'), ('Chile', 'Dia Internacional dos Povos Indígenas', '09/08'),
 ('Argentina', 'Dia dos Professores', '11/09'), ('Chile', 'Dia dos Namorados', '14/02'), ('Chile', 'Dia das Mães', '03/05'),
 ('Brasil', 'Dia Internacional dos Povos Indígenas', '09/08'), ('Brasil', 'Dia das Mães', '03/05'), ('Chile', 'Dia do Trabalho', '01/05'),
 ('Brasil', 'Dia do Trabalho', '01/05'), ('Brasil', 'Dia das Mães', '10/05'), ('Brasil', 'Dia Mundial do Radioamador', '18/04'),
 ('Argentina', 'Dia Mundial do Radioamador', '18/04'), ('Chile', 'Dia Mundial do Radioamador', '18/04'),
 ('Argentina', 'Dia Internacional dos Povos Indígenas', '09/08'),
 )

dicPaisComemoracao=criaDicPaisComemoracao(tComemoracoes)

dicDataCome=criaDicDataCome(dicPaisComemoracao)

data=input('Escreva uma data no formato ''dd/mm'': ')
com=input('Escreva o nome de uma comemoração: ')

obtemPaises(dicDataCome,data,com)




