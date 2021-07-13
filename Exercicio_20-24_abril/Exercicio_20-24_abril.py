dCores={'P':'Preto','B':'Branco','C':'Creme','M':'Marrom',
        'G':'Cinza','A':'Malhado','N':'Pinhão'}

dResultPorComb={ ('M', 'C'): [270.6, 3, 90.2], ('B', 'P'): [150.3, 2, 75.15],
                 ('C', 'M'): [130.6, 2, 65.3], ('G', 'M'): [121.2, 2, 60.6], 
                 ('M', 'G'): [80.1, 1, 80.1], ('P', 'B'): [40.2, 1, 40.2],
                 ('B', 'C'): [102.3, 3, 34.1], ('A', 'N'): [10.9, 1, 10.9], 
                 ('C', 'P'): [342.3, 3, 114.1], ('N', 'A'): [32.7, 1, 32.7], 
                 ('C', 'B'): [100.9, 2, 50.45], ('G', 'B'): [121.1, 2, 60.55],
                 ('G', 'N'): [30.0, 1, 30.0], ('P', 'C'): [160.3, 2, 80.15], 
                 ('B', 'M'): [190.5, 2, 95.25], ('M', 'B'): [50.4, 1, 50.4], 
                 ('N', 'N'): [10.1, 1, 10.1], ('P', 'P'): [15.7, 1, 15.7] }

#3.A)
def descobre_maior_peso_medio(dRes,dCor):
    maior_peso=0
    for pais,lista in dRes.items():
        if lista[2]>maior_peso:
            maior_peso=lista[2]
            pai=pais[0]
            mae=pais[1]
    return ((dCor[pai],dCor[mae]),maior_peso)

tupla=descobre_maior_peso_medio(dResultPorComb,dCores)
print('Combinação de cores com o maior peso médio: PAI - %s e MÃE = %s \nMaior peso médio: %.1f'%(tupla[0][0],tupla[0][1],tupla[1]))

#3.B)    
def atualizaDicResultadoPorComb(dRes,dCor,nom_arq):
    l_dados=[]
    arq=open(nom_arq,'r')
    for linha in arq:
        l=linha.strip().split()
        l[2]=float(l[2])
        l=[(l[0],l[1]),l[2]]
        l_dados.append(l)
    arq.close()
    print(l_dados)
    for el in l_dados:
        chave=el[0]
        valor=dRes.get(chave)
        if valor!=None:
            dRes[chave][2]=el[1]
    return 

atualizado=atualizaDicResultadoPorComb(dResultPorComb,dCores,'ATUALIZACAO_FILIACAO_E_PESO.txt')
print(dResultPorComb)