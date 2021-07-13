#Nome completo: Daniel Stulberg Huf
#Matrícula PUC-Rio: 1920468
#Declaração de autoria: Declaro que este documento foi produzido em sua totalidade por mim,
#sem consultas a outros alunos, professores ou qualquer outra pessoa.

def exibeMomentoMatricula(dicCursos,dicAprov):
    for aluno in dicAprov:
        nome=aluno
        curso=dicAprov[aluno][0]
        dia=dicCursos[curso][0]
        colocacao=dicAprov[aluno][1]
        vagas=dicCursos[curso][1]
        if colocacao<=(1/5)*vagas:
            hora='8h às 9:30h'
        elif colocacao<=(2/5)*vagas:
            hora='10h às 11:30h'
        elif colocacao<=(3/5)*vagas:
            hora='13h às 14:30h'
        elif colocacao<=(4/5)*vagas:
            hora='15h às 16:30h'
        else:
            hora='17h às 18:30h'
        s='Nome: {:<5}  curso: {:<10}  dia: {:<5}  horário: {:<5}'.format(nome,curso,dia,hora)
        print(s)
    return

dCursos={'engenharia':('5/01/2018',550),'direito':('6/01/2018',350),
         'economia':('7/01/2018',160),'design':('8/01/2018',240)}

dAprovados={'Ana':('economia',75),'Jose':('engenharia',399),'Joao':('direito',5)}

exibeMomentoMatricula(dCursos,dAprovados)

