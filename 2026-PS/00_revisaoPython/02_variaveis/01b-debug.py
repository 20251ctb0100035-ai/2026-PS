# Arquivo: 0lb-debug.py
# ATENÇÃO: Este código contém 4 erros propositais. Encontre e corrija todos!

nome  = input("Digite o nome do aluno: ") #imput -> input
notal = float(input("Digite a nota 1: ")) #Digite a nota l -> Digite a nota 1:
nota2 = float(input("Digite a nota 2: "))

media = notal + nota2 / 2 # nota1 -> notal

if media >= 6.0:
    situacao = "Aprovado"
elif media >= 4.0:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"Aluno: {nome} | Média: {media:.2f} | Situação: {situacao}") #pront -> print