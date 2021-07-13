import pandas as pd 
'''Criando series com repetição de índices''' 
sR = pd.Series ([ 10 , 20 , 30 , 40 , 10 , 20 , 30 , 40 , 50 ], 
                  index =[ 'a1' , 'a2' , 'b1' , 'b2' , 'a1' , 'a2' , 'b1' , 'b2' , 'b1' ]) 

'''Criando uma series com as quantidades de dezenas''' 
sD = pd.Series ([ '1dez' , '2dez' , '3dez' , '4dez' , '1dez' , '2dez' , '3dez' , '4dez' , '5dez' ], 
                index =[ 'a1' , 'a2' , 'b1' , 'b2' , 'a1' , 'a2' , 'b1' , 'b2' , 'b1' ]) 

'''Criando series sem repetição de índices''' 
sS = pd.Series ([ 10 , 20 , 30 , 40 , 10 , 20 , 30 , 40 , 50 ], 
                  index =[ 'a10' , 'a20' , 'b10' , 'b20' , 'a11' , 'a21' , 'b11' , 'b21' , 'b13' ]) 



'''Associando uma categoria a cada valor de sR:     bx:(0, 25], md:(25, 45], al:(45, 50]''' 
cCatR = pd.cut ( sR , bins =[ 0 , 25 , 45 , sR.max ()], labels =[ 'baixo' , 'médio' , 'alto' ]) 

'''Associando uma categoria a cada valor de sS: sS: bx:(0, 25], md:(25, 45],al:(45, 50]''' 
cCatS = pd.cut ( sS , bins =[ 0 , 25 , 45 , sS.max ()], labels =[ 'baixo' , 'médio' , 'alto' ]) 


########################################################################## 
# 
# Agupando por nível de índice: 
#   índices iguais --> 1 grupo 
# Válido para Series com índices repetidos 
# 
########################################################################## 

print ( "\nI) ******Agupando por nível de índice******\n" ) 
gNivel = sR.groupby ( level = 0 ) 

'''observando o dicionário dos grupos criados:''' 
print ( "I.a)grupos\n" , gNivel.groups ) 

# ----------------------------------------------------------------------------
# agg --> resumos por grupo: aplica a(s) função(ões) para cada grupo. 
# Resultado: uma Series onde 
#           index: identificadores dos grupos e 
#           values: resultado da função p/grupo 
#------------------------------------------------------------
 
''' Usando funções de sumarização do Pandas''' 

sResUm = gNivel.agg ([ 'min' ]) 
dfResVarios = gNivel.agg ([ 'sum' , 'min' , 'max' , 'mean' , 'median' ]) 
print ( "\nI.b)Mínimo de cada grupo\n" , sResUm ) 
print ( "\nI.c)Medidas Descritivas de cada grupo\n" , dfResVarios ) 

'''Usando função construída pelo progamador''' 
def detDuzias( grupo ): 
    tot = grupo.sum () 
    dz = tot // 12 
    unid = tot % 12 
    t1 = 'dúzia' 
    t2 = 'unidade' 
    if dz > 1 : 
        t1 += 's' 
    if unid > 1 : 
        t2 += 's' 
    return "{} {} e {} {}".format ( dz , t1 , unid , t2 ) 

sResFunc = gNivel.agg (detDuzias) 
print ( "\nI.d)Qt dúzias de cada grupo\n{}".format ( sResFunc ) ) 

########################################################################## 
# 
# Agupando por função determinadora do grupo: 
#   índices que retornam mesmo valor da função --> 1 grupo 
# Válido para Series com/sem índices repetidos 
# 
#   Obs: a função determina o  grupo em função do label do index
# 
########################################################################## 

def detGrupoLetra( el ): # entra  valor de index, sai categoria/label do grupo 
    return el [ 0 ] 

print ( "\nII) ******Agupando por função determinadora do grupo- ******\n" ) 
gFunc = sR.groupby ( by = detGrupoLetra ) 

''' observando grupos criados:''' 
print ( "II.a) grupos\n" , gFunc.groups ) 

#----------------------------------------------------------------------- 
# agg --> resumos por grupo: aplica a(s) função(ões) para cada grupo. 
#------------------------------------------------------------------------- 

'''Usando funções de sumarização do Pandas''' 
sResUm = gFunc.agg ([ 'min' ]) 
dfResVarios = gFunc.agg ([ 'sum' , 'min' , 'max' , 'mean' , 'median' ]) 
print ( "\nII.b) Mínimo de cada grupo\n" , sResUm ) 

print ( "\nII.c) Medidas Descritivas de cada grupo\n" , dfResVarios ) 

'''Usando função construída pelo progamador''' 
sResSeriesc = gFunc.agg ( detDuzias ) 
print ( "\nII.d) Qt dúzias de cada grupo\n{}".format ( sResFunc ) ) 

########################################################################## 
# 
# Agupando por duas estruturas (Series e/ou Category)  de mesmo índice: 
#           dois níveis de índices 
# Válido para Series com/sem índices repetidos 
# 
########################################################################## 

print ( "\nIII) ******Agupando por duas estruturas (series/categorys) de mesmo índice******\n" ) 
g2Func = sR.groupby ( by =[ cCatR , sD ]) 

'''observando o dicionário dos grupos criados:''' 
print ( "III.a) grupos\n" , g2Func.groups ) 

#------------------------------------------------------------------------- 
# agg --> resumos por grupo: aplica a(s) função(ões) para cada grupo. 
#------------------------------------------------------------------------- 

'''Usando funções de sumarização do Pandas: Categoria/Qt Dezenas''' 
sResUm = g2Func.agg ([ 'min' ]) 
dfResVarios = g2Func.agg ([ 'sum' , 'min' , 'max' , 'mean' , 'median' ]) 
print ( "\nIII.b) Mínimo de cada grupo\n" , sResUm ) 
print ( "\nIII.c) Medidas Descritivas de cada grupo\n" , dfResVarios ) 

'''Usando função construída pelo progamador''' 
sResFunc = g2Func.agg ( detDuzias ) 
print ( "\nIII.d) Qt dúzias de cada grupo\n{}".format ( sResFunc ) ) 


########################################################################## 
# 
# Agupando por uma series/cateory de mesmo índice e uma função: 
#   dois níveis de índices 
# Válido para Series com/sem índices repetidos 
# 
########################################################################## 
 
print ( "\nIV) ******Agupando por uma series de mesmo índice e uma função ******\n" ) 
gMistaSF = sR.groupby ( by =[ cCatR , detGrupoLetra ]) 

'''observando o dicionário de grupos criados:''' 
print ( "IV.a) grupos\n" , gMistaSF.groups ) 

# ----------------------------------------------------------------------- 
# agg --> resumos por grupo: aplica a(s) função(ões) para cada grupo. 
#------------------------------------------------------------------------- 

'''Usando funções de sumarização do Pandas''' 
sResUm = gMistaSF.agg ([ 'min' ]) 
dfResVarios = gMistaSF.agg ([ 'sum' , 'min' , 'max' , 'mean' , 'median' ]) 
print ( "\nIV.b) Mínimo de cada grupo\n" , sResUm ) 
print ( "\nIV.c) Medidas Descritivas de cada grupo\n" , dfResVarios ) 

'''Usando função construída pelo progamador''' 
sesFunc = gMistaSF.agg ( detDuzias ) 
print ( "\nIV.d) Qt dúzias de cada grupo\n{}".format ( sesFunc ) ) 

########################################################################## 
# 
# Agupando por nível e função ou series ou catregory de mesmo índice 
#       dois níveis de índices 
# Válido para Series com índices repetidos 
# 
########################################################################## 
 
print ( "\nV) ******Agupando por nível e função / series de mesmo índice******\n" ) 
# é preciso tornar o nível um tipo de agrupador: pd.grouper
gMista = sR.groupby ( by =[ cCatR , pd.Grouper ( level = 0 )]) 
# observando dicionário de grupos criados: 
print ( "V.a) grupos\n" , gMista.groups ) 

#----------------------------------------------------------------------- 
# agg --> resumos por grupo: aplica a(s) função(ões) para cada grupo. 
#------------------------------------------------------------------------- 
 
''' Usando funções de sumarização do Pandas''' 
sResUm = gMista.agg ([ 'min' ]) 
dfResVarios = gMista.agg ([ 'sum' , 'min' , 'max' , 'mean' , 'median' ]) 
print ( "\nV.b) Mínimo de cada grupo\n" , sResUm ) 
print ( "\nV.c) Medidas Descritivas de cada grupo\n" , dfResVarios ) 
''' Usando função construída pelo progamador''' 
sResFunc = gMista.agg ( detDuzias ) 
print ( "\nV.d) Qt dúzias de cada grupo\n{}".format ( sResFunc ) ) 



########################################################################## 
# 
# APLICANDO uma função num agrupamento  via .APPLY
# (grupos criados por função ou series de mesmo índice) 
# -->VÁLIDO SOMENTE PARA SERIES COM ÍNDICES SEM REPETIÇÃO 
# 
########################################################################## 
 
print ( "\nVI) ******Usando .apply num agrupamento ******" ) 
print ( "\t Válido em series sem repetição" ) 
print ( "\tgrupos construídos por função ou series de mesmo índice\n" ) 


#----------------------------------------------------------------------- 
# groupby --> construindo grupo por função. 
#------------------------------------------------------------------------- 

gNivelS = sS.groupby ( by = detGrupoLetra ) 

#----------------------------------------------------------------------- 

# apply --> aplica a função em cada grupo. 
# Resultado: uma Series onde o 
#   index: índices da series que gerou o agupamento 
#   e values: resultado da função p/grupo 
# 
#------------------------------------------------------------------------- 

def AlteraPorgrupo( seriesGrupo ): 
    ''' 
    Modifica alguns valores do grupo. Acrescenta metade da média do grupo 
    aos elementos  
    ''' 
    MetMedia = seriesGrupo.mean ()// 2 
    print("Média do grupo",MetMedia)
    return seriesGrupo.add(MetMedia)
  
sNova = gNivelS.apply ( AlteraPorgrupo ). sort_index () 
#----------------------------------------------------------------------- 
# exibindo as series 
#------------------------------------------------------------------------- 

print ( "\nVI.a) Series original:\n{}".format ( sS.sort_index ())) 
print ( "\nVI.b) Nova Series com valores modificados por grupo:\n{}".format ( sNova )) 
    
    
    
########################################################################## 
# 
# APLICANDO uma função num agrupamento  via TRANSFORM
# (grupos criados por função ou series de mesmo índice) 
#  
########################################################################## 
 
print ( "\nVII) ******Usando .transform num agrupamento ******" ) 
print ( "\t Válido em series com ou sem repetição\n" ) 



#----------------------------------------------------------------------- 
# groupby --> construindo grupo por função. 
#------------------------------------------------------------------------- 

gNivelR = sR.groupby ( by = detGrupoLetra ) 

#----------------------------------------------------------------------- 

# apply --> aplica a função em cada grupo. 
# Resultado: uma Series onde o 
#   index: índices da series que gerou o agupamento 
#   e values: resultado da função p/grupo 
# 
#------------------------------------------------------------------------- 

def AlteraPorgrupo( seriesGrupo ): 
    ''' 
    Modifica alguns valores do grupo. Acrescenta metade da média do grupo 
    aos elementos  
    ''' 
    MetMedia = seriesGrupo.mean ()// 2 
    print("Média do grupo",MetMedia)
    return seriesGrupo.add(MetMedia)
  
sNovaR = gNivelR.transform ( AlteraPorgrupo ). sort_index () 
#----------------------------------------------------------------------- 
# exibindo as series 
#------------------------------------------------------------------------- 

print ( "\nVII.a) Series original:\n{}".format ( sR) )
print ( "\nVII.b) Nova Series com valores modificados por grupo:\n{}".format ( sNovaR )) 

'''
def AlteraPorgrupo( grupo ): 
    
    #    Modifica alguns valores do grupo. Acrescenta metade da média do grupo 
    #   aos elementos cujos valores são menores ou iguais à mediana do grupo 
  
    MetMedia = grupo.mean ()// 2 
    mediana = grupo.median () 
    sMediana = grupo.loc [ grupo <= mediana ] #filtra elementos <= a mediana 
    sMediana = sMediana + MetMedia # soma, aos elementos filtrados, metade da média 
    grupo.update ( sMediana ) #atualiza no grupo,os elementos modificados return grupo 
'''