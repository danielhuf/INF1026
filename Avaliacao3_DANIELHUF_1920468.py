#Nome completo: Daniel Stulberg Huf
#Matrícula PUC-Rio: 1920468
#Declaração de autoria: Declaro que este documento foi produzido em sua totalidade por mim,
#sem consultas a outros alunos, professores ou qualquer outra pessoa.

#1)
#a)

def criaDicUnidadeENutriente(dicNutri):
    dicUni={}
    for nutriente,unidade in dicNutri.items():
        lAux=dicUni.get(unidade,[])
        lAux.append(nutriente)
        dicUni[unidade]=lAux
    print(dicUni)
    return dicUni

#b)
def exibeNutrientes(alimento,nutriente,dicAlim,dicNutri):
    quant_nutri=dicAlim[alimento][nutriente]
    unidade=dicNutri[nutriente]
    print('%s - %s: %.1f %s'%(alimento,nutriente,quant_nutri,unidade))
    return

#c)
def pratoPronto(dicAlim,dicNutri,dicPrato):
    dicTotais={'CALORIAS':0,'PROTEINA':0,'CARBOIDRATO':0,'FIBRA':0,'FERRO':0,'SODIO':0}
    for alimento,porc in dicPrato.items():
        for nutriente,quant in dicAlim[alimento].items():
            dicTotais[nutriente]=dicTotais.get(nutriente)+porc*quant
    print('Nutrientes totais do prato:')
    for nutriente,quant in dicTotais.items():
        print('Total de %s: %.1f %s'%(nutriente,quant,dicNutri[nutriente]))
    return  
          
dNutrienteEUnidade={'CALORIAS': 'kcal', 'PROTEINA': 'g', 'CARBOIDRATO': 'g', 'FIBRA': 'g', 'FERRO': 'mg', 'SODIO': 'mg'}

dAlim = {'ARROZ': {'CALORIAS': 124.0, 'PROTEINA': 2.6, 'CARBOIDRATO': 25.8, 'FIBRA': 2.7, 'FERRO': 0.3, 'SODIO': 1.0},
 'ALFACE': {'CALORIAS': 14.0, 'PROTEINA': 1.7, 'CARBOIDRATO': 2.4, 'FIBRA': 2.3, 'FERRO': 0.6, 'SODIO': 4.0},
 'BATATA COZIDA': {'CALORIAS': 52.0, 'PROTEINA': 1.2, 'CARBOIDRATO': 11.9, 'FIBRA': 1.3, 'FERRO': 0.2, 'SODIO': 2.0},
 'BATATA FRITA': {'CALORIAS': 267.0, 'PROTEINA': 5.0, 'CARBOIDRATO': 35.6, 'FIBRA': 8.1, 'FERRO': 0.4, 'SODIO': 2.0},
 'CENOURA': {'CALORIAS': 34.0, 'PROTEINA': 1.3, 'CARBOIDRATO': 7.7, 'FIBRA': 3.2, 'FERRO': 0.2, 'SODIO': 3.0},
 'ESPINAFRE': {'CALORIAS': 67.0, 'PROTEINA': 2.7, 'CARBOIDRATO': 4.2, 'FIBRA': 2.5, 'FERRO': 0.6, 'SODIO': 47.0},
 'INHAME': {'CALORIAS': 97.0, 'PROTEINA': 2.1, 'CARBOIDRATO': 23.2, 'FIBRA': 1.7, 'FERRO': 0.4, 'SODIO': 0.0},
 'MANDIOCA FRITA': {'CALORIAS': 300.0, 'PROTEINA': 1.4, 'CARBOIDRATO': 50.3, 'FIBRA': 1.9, 'FERRO': 0.3, 'SODIO': 9.0},
 'REPOLHO': {'CALORIAS': 17.0, 'PROTEINA': 0.9, 'CARBOIDRATO': 3.9, 'FIBRA': 1.9, 'FERRO': 0.2, 'SODIO': 4.0},
 'RUCULA': {'CALORIAS': 13.0, 'PROTEINA': 1.8, 'CARBOIDRATO': 2.2, 'FIBRA': 1.7, 'FERRO': 0.9, 'SODIO': 9.0},
 'TOMATE': {'CALORIAS': 15.0, 'PROTEINA': 1.1, 'CARBOIDRATO': 3.1, 'FIBRA': 1.2, 'FERRO': 0.2, 'SODIO': 1.0},
 'PEIXE FRITO': {'CALORIAS': 154.0, 'PROTEINA': 28.6, 'CARBOIDRATO': 0.0, 'FIBRA': 0.0, 'FERRO': 0.3, 'SODIO': 115.0},
 'BIFE MILANESA': {'CALORIAS': 352.0, 'PROTEINA': 20.6, 'CARBOIDRATO': 12.2, 'FIBRA': 0.4, 'FERRO': 2.9, 'SODIO': 77.0},
 'CARNE ASSADA': {'CALORIAS': 241.0, 'PROTEINA': 31.9, 'CARBOIDRATO': 0.0, 'FIBRA': 0.0, 'FERRO': 3.2, 'SODIO': 52.0},
 'PEITO DE FRANGO': {'CALORIAS': 212.0, 'PROTEINA': 33.4, 'CARBOIDRATO': 0.0, 'FIBRA': 0.0, 'FERRO': 0.5, 'SODIO': 56.0},
 'PORCO ASSADO': {'CALORIAS': 262.0, 'PROTEINA': 32.1, 'CARBOIDRATO': 0.0, 'FIBRA': 0.0, 'FERRO': 1.3, 'SODIO': 62.0},
 'OVO FRITO': {'CALORIAS': 240.0, 'PROTEINA': 15.6, 'CARBOIDRATO': 1.2, 'FIBRA': 0.0, 'FERRO': 2.1, 'SODIO': 166.0},
 'FEIJAO': {'CALORIAS': 77.0, 'PROTEINA': 4.5, 'CARBOIDRATO': 14.0, 'FIBRA': 8.4, 'FERRO': 1.5, 'SODIO': 2.0}}

dPrato= {'FEIJAO':2, 'ARROZ':1, 'ESPINAFRE':2, 'CARNE ASSADA':1, 'TOMATE':1}

print('----------Testando a primeira função----------\n')
dUnidadeENutrientes=criaDicUnidadeENutriente(dNutrienteEUnidade)

print('\n----------Testando a segunda função----------\n')
exibeNutrientes('TOMATE','CARBOIDRATO',dAlim,dNutrienteEUnidade)

print('\n----------Testando a terceira função----------\n')
pratoPronto(dAlim,dNutrienteEUnidade,dPrato)
    

