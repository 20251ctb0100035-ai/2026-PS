# Entrada
def LerAlunos():
    lista_alunos = []
    lista_medias = []

    while True:
        nome_aluno = input('Nome do aluno (sair): ')
        if nome_aluno == 'sair':
            break

        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))

        media_aluno = CalcularMedia(nota1, nota2)
        situacao_aluno = VerificarSituacao(media_aluno)

        lista_alunos.append((nome_aluno, media_aluno, situacao_aluno))
        lista_medias.append(media_aluno)

    aprovados, recuperacao, reprovados = ResumoTurma(lista_alunos)
    media_turma = CalcularMediaTurma(lista_medias)

    MostrarResultado(lista_alunos, media_turma, aprovados, recuperacao, reprovados)


def CalcularMedia(nota1, nota2):
    return (nota1 + nota2) / 2


def VerificarSituacao(media):
    if media >= 7:
        return 'Aprovado'
    elif media >= 4:
        return 'Recuperação'
    else:
        return 'Reprovado'


def CalcularMediaTurma(lista_medias):
    if len(lista_medias) == 1:
        return lista_medias[0]
    return (lista_medias[0] + CalcularMediaTurma(lista_medias[1:]) * (len(lista_medias)-1)) / len(lista_medias)


def ResumoTurma(lista_alunos):
    total_aprovados = 0
    total_recuperacao = 0
    total_reprovados = 0

    for aluno in lista_alunos:
        if aluno[2] == 'Aprovado':
            total_aprovados += 1
        elif aluno[2] == 'Recuperação':
            total_recuperacao += 1
        else:
            total_reprovados += 1

    return total_aprovados, total_recuperacao, total_reprovados


def MostrarResultado(lista_alunos, media_turma, aprovados, recuperacao, reprovados):
    for aluno in lista_alunos:
        print(aluno[0], aluno[1], aluno[2])

    print('Media da turma:', media_turma)
    print('Aprovados:', aprovados)
    print('Recuperacao:', recuperacao)
    print('Reprovados:', reprovados)


LerAlunos()
