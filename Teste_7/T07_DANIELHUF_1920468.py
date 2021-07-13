#Nome completo: Daniel Stulberg Huf
#Matrí­cula PUC-Rio: 1920468
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, 
#sem consultas a outros alunos, professores ou qualquer outra pessoa.

'''
O grupo CinPlex deseja conhecer melhor o movimento das sessões de sábado de suas salas 
de cinema. Um mesmo filme é exibido em diferentes sessões. Há filmes de diferentes gêneros.
Deseja analisar:
  - total da venda de ingressos do sábado, por filme, por gênero
  - cancelamentos
  - gêneros preferidos
Armazenou em dois arquivos xlsx informações sobre as vendas e gêneros dos filmes em cartaz:
=>arquivo cinemasabado.xlsx armazena a venda de ingressos nas diferentes sessões de sábado,
   com os seguintes dados:
   1ª coluna: HORA do início da sessão
   2ª coluna: nome do FILME
   3ª coluna: quantidade de INGRESSOS vendidos deste filme nesta sessão
   
=>arquivo generofilmes.xlsx, contém informações sobre os gêneros dos filmes em cartaz,
   com os seguintes dados:
   1ª coluna: nome do FILME
   2ª coluna: GENERO do filme
No entanto, há informações incorretas nessas planilhas que precisam ser consertadas.
Usaremos duas Series, que já foram criadas neste arquivo e que são:
•	srSessoes onde o índice é o nome do FILME e o valor a quantidade de INGRESSOS vendidos,
   deste filme em uma sessão. 
•	srGeneros onde o índice é o nome do FILME e o valor o GENERO do filme. 
Os dois arquivos têm uma linha de cabeçalho, com os nomes das colunas.

ATENÇÃO: SUA SOLUÇÃO TEM QUE MANIPULAR A ESTRUTURA DA BIBLIOTECA PANDAS DENOMINADA 
SERIES E OS MÉTODOS APRESENTADOS E TRABALHADOS NAS AULAS E MATERIAL DISPONIBILIZADOS.
NÃO É PERMITIDO TRANSFORMÁ-LA EM OUTRA ESTRUTURA PARA OBTER A RESPOSTA PEDIDA.

'''
import pandas as pd
import matplotlib.pyplot as plt

#################################################
# 1. CONHECENDO AS SERIES CRIADAS
################################################
srSessoes = pd.read_excel('cinemasabado.xlsx', header=0,usecols=[1,2],index_col=0, squeeze=True)
srGeneros = pd.read_excel('generofilmes.xlsx', header=0, index_col=0, squeeze=True)
'''1.1 - Exibir as 6 primeiras linhas da Series srSessoes criada'''
print('\n')
print('1.1 - Series srSessoes criada: 6 primeiros')
print(srSessoes.head(6))

'''1.2 - Exibir as 3 ultimas linhas da Series srGeneros criada'''
print('\n')
print('1.2 - Series srGeneros criada: 3 ultimos')
print(srGeneros.tail(3))
print('\n')
print('*****************************************')

#################################################
# 2. CORRIGINDO OS VALORES INCORRETOS
################################################
"""Os seguintes erros foram constatados na planilha do arquivo cinemasabado.xlsx e devem ser
corrigidos na Series srSessoes:
->As sessões sem ingressos vendidos estão com a quantidade em branco. 
O correto seria o valor zero (0).
->Na planilha não deveria haver nenhum valor acima de 1000, já que nenhuma sala de cinema tem 
capacidade tão grande. Entretanto alguns valores foram lançados errados na planilha, com um 
dígito a mais no final. Por exemplo, um valor que deveria ser 123 foi lançado como 1235.
Voce deve fazer a correção dos valores, aplicando uma função denominada "corrige" criada por 
voce, e alterando a Series srSessoes.
"""
''' Corrigindo na Series srSessoes as sessoes sem ingressos vendidos'''
srSessoes.fillna(value=0,inplace=True)

''' Corrigindo na Series srSessoes as quantidades maiores que 1000'''
def corrige(num):
    if num>1000:
        return num//10
    return num
srSessoes=srSessoes.apply(corrige)

'''2 - Exibindo a Serias srSessoes com ambas as correcoes'''
print('2 - Series srSessoes apos ser corrigida')
print(srSessoes)
print('\n')
print('*****************************************')
#################################################
# 3. CONHECENDO O MOVIMENTO NO SÁBADO
#     Qual o total de ingressos vendidos no sábado?
#     Qual o melhor e pior desempenho de vendas, considerando as sessões individualmente?
#     Qual a média de ingressos vendidos? (qt total vendida no sábado/nº de sessões)
################################################
'''3.1- Exibir total de ingressos vendidos no sabado.'''
print('3.1 - O total de ingressos vendidos no sabado:')
print(srSessoes.sum())
print('\n')

'''3.2- Exibir maior e menor quantidade de ingressos vendidos em uma unica sessao.'''
print('3.2 - Maior e menor quantidade de ingressos numa sessao:')
print(srSessoes.max())
print(srSessoes.min())
print('\n')

'''3.3- Exibir a quantidade media de ingressos vendidos por sessao no sabado.'''
print('3.3 - Quantidade media de ingressos vendidos por sessao no sabado:')
print(srSessoes.mean())
print('\n')
print('*****************************************')
#################################################
# 4. CONHECENDO O MOVIMENTO DO GÊNERO AÇÃO
#     Quantas sessões de filmes deste gênero foram canceladas?
#     Qual o percentual de vendas deste gênero em relação ao total do sábado?
################################################
"""4. GUERRAS, HEROES e MATADOR são os filmes de ACAO do sábado que o grupo CinPlex deseja 
avaliar. """
'''4.1- Quantidade total de sessoes canceladas para os filmes do gênero ação porque nao
houve venda de ingressos.'''
print('4.1 - Quantidade de Sessoes canceladas para Gênero Ação: ')
gSessoesTipo=srSessoes.groupby(by=srGeneros)
sAcao=gSessoesTipo.get_group('ACAO')
print(sAcao.loc[sAcao==0].size)
print('\n')

'''4.2- Percentual das vendas dos filmes de Ação com relacao ao total de vendas. '''
print('4.2 - Percentual das vendas dos filmes de Ação em relacao ao total de sabado: ')
print(sAcao.sum()*100/srSessoes.sum())
print('\n')
print('*****************************************')
#################################################
# 5. CONHECENDO OS GÊNEROS EM CARTAZ
#     Quantos e quais os gêneros dos filmes em cartaz?
#     Qual  gênero com maior número de filmes?
#################################################
'''5.1- Mostre os Gêneros em cartaz.'''
print('5.1 - Lista de gêneros dos filmes em cartaz(sem repetição)')
print(srGeneros.unique())
print('\n')

'''5.2- Quantidade de Gêneros distintos estão em cartaz .'''
print('5.2 - Quantidade de Gêneros distintos estão em cartaz')
print(srGeneros.unique().size)
print('\n')

'''5.3 - Exibir gênero com maior número de filmes '''
print('5.3 - o genero mais frequente. Se houver mais de um, exibir todos')
sFreqGeneros=srGeneros.value_counts()
print(sFreqGeneros.loc[sFreqGeneros==sFreqGeneros.max()].index.values)
print('\n')

print('*****************************************')
#################################################
# 6. CONHECENDO O MOVIMENTO POR FILME
#     Número de sessões, por filme, cuja quantidade de ingressos vendidos é inferior à
#      média do sábado?
#     Qual a quantidade média de ingressos vendidos por filme, considerando todas as suas sessões?
#     Análise da quantidade media de ingressos vendidos  de acordo com faixas de vendas 
################################################
'''6.1 - Número de sessoes de cada filme com venda abaixo da quantidade media do sabado. '''
print('6.1 - Número de sessoes de cada filme com venda abaixo da média do sabado.')
sAbaixoMedia=srSessoes.loc[srSessoes<srSessoes.mean()]
print(sAbaixoMedia.index.value_counts())
print('\n')

''' A partir da srSessoes criar uma nova series (srFilmesSabado), com a media de 
INGRESSOS VENDIDOS de cada FILME no sabado. '''
srFilmesSabado=srSessoes.mean(level=0)

'''6.2 - Exibir a Series srFilmesSabado ordenada decrescentemente pela quantidade media de 
 INGRESSOS VENDIDOS.'''
print('6.2 - Filmes ordenados descrescentemente por quantidade media de ingressos vendidos')
print(srFilmesSabado.sort_values(ascending=False))
print('\n')

'''6.3 - Exibir gráfico pizza da srFilmesSabado, ou seja, gráfico com a  
"Quantidade media de INGRESSOS VENDIDOS por FILME no sabado" '''
print('6.3 - GRAFICO PIZZA: Quantidade media de INGRESSOS VENDIDOS por FILME no sabado')
srFilmesSabado.plot.pie(figsize=(8,8),autopct='%.1f%%',title='Quantidade média de ingressoes vendidos por filme no sábado')
plt.show()
print('\n')

'''6.4 - A partir da srFilmesSabado criar a Series srVendasSabado com 4 categorias de acordo 
com a quantidade media de ingressos vendidos (de 0 a 180, de 181 a 250, de 251 a 300, acima de 300). 
As categorias sao respectivamente: pouca,razoavel, media, alta. Exibir a series srVendasSabado'''
print('6.4 - SABADO: Faixas de venda')
srVendasSabado=pd.cut(srFilmesSabado,bins=[0,180,250,300,srFilmesSabado.max()],labels=['pouca','razoavel','media','alta'])
print(srVendasSabado)
print('\n')

'''6.5 - Tabela de frequencias da Series srVendasSabado, exibida com o grafico de barras 
na ordem das categorias, isto é: pouca, razoavel, media, alta'''
print('6.5 - Grafico de barras, em ordem de categoria, referente a tabela de frequencia da ' \
      'series srVendasSabado')
sFreqVendasSabado=srVendasSabado.value_counts().reindex(['pouca','razoavel','media','alta'])
sFreqVendasSabado.plot.bar(width=0.5)
plt.show()
print('\n')
print('*****************************************') 
#################################################
# 7. CONHECENDO O MOVIMENTO POR GÊNERO 
#     Qual o total de ingressos vendidos de cada genero
#     Qual a quantidade média de ingressos vendidos por filme, considerando todas as suas sessões?
#     Análise da quantidade media de ingressos vendidos  de acordo com faixas de vendas 
################################################
''' 7.1 - Exibir o total de ingressos vendidos de cada genero '''
print('7.1 - Total de ingressos vendidos de cada genero ')
gSessoes=srSessoes.groupby(level=0)
sTotGenero=gSessoesTipo.agg('sum')
print(sTotGenero)
print('\n')

'''7.2 - Exibir o genero mais assistido '''
print('7.2 - o genero mais assistido. Se houver mais de um, exibir todos')
print(sTotGenero.loc[sTotGenero==sTotGenero.max()].index.values)
print('\n')
print('*****************************************')


