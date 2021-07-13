#Daniel Stulberg Huf mat. 1920468
#Exercício 1
#a)

def trataUmGrupo(a):
    l_info=[]
    arq=open(a,'r')
    linha1=arq.readline()
    linha1=linha1.strip()
    for l in arq:
        l=l.strip()
        info=l.split(',')
        l_info.append(info)
    arq.close()
    n_efeitos=0
    n_pessoas=len(l_info)
    soma_tempos=0
    for el in l_info:
        soma_tempos+=int(el[0])
        if el[1]!='ausente':
            n_efeitos+=1
    tempo_cura=soma_tempos/n_pessoas
    return (linha1,tempo_cura,n_efeitos)
 
l_resp=[]
l_resp.append(trataUmGrupo('grupoa.txt'))
l_resp.append(trataUmGrupo('grupob.txt'))
l_resp.append(trataUmGrupo('grupoc.txt'))
l_resp.append(trataUmGrupo('grupod.txt'))

for el in l_resp:
    print('Nome da substância: %s \n Tempo de cura médio do grupo: %.1f \n Quantidade de indivíduos com efeitos colaterais: %d \n'%(el[0],el[1],el[2]))

#b)
def menorTempoMedio(lista):
    tMedMinimo=lista[0]
    for i in range(1,len(lista)):
        if lista[i][1]<tMedMinimo[1]:
            tMedMinimo=l_resp[i]
    return tMedMinimo

tupla_menor=menorTempoMedio(l_resp)
print('Substância com menor tempo médio de cura: %s \n Tempo médio: %.1f \n Quantidade de indivíduos com efeitos colaterais: %d \n'%(tupla_menor[0],tupla_menor[1],tupla_menor[2]))

#c)
def efeitosColateraisMaxMin(lista):
    efcMin=lista[0]
    efcMax=lista[0]
    for i in range(1,len(lista)):
        if lista[i][2]<efcMin[2]:
            efcMin=lista[i]
        if lista[i][2]>efcMax[2]:
            efcMax=lista[i]
    return (efcMin,efcMax)

(col_min,col_max)=efeitosColateraisMaxMin(l_resp)
print('Substância com maior número de efeitos colaterais: %s \n Tempo médio de cura: %.1f \n Quantidade de indivíduos com efeitos colaterais: %d \n \n Substância com menor número de efeitos colaterais: %s \n Tempo médio de cura: %.1f \n Quantidade de indivíduos com efeitos colaterais: %d \n'%(col_max[0],col_max[1],col_max[2],col_min[0],col_min[1],col_min[2]))

