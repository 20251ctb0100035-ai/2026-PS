# ------------------------------------------------
# SISTEMA DE APROVAÇÃO DE ALUNOS
# ================================================
# DISCIPLINA : Programação de sistemas (PS)
# AULA       : 04 - Revisão: Variáveis, Tipos e Controle de Fluxo
# Autor      : [Anthony Pagani]
# Data       : [24/02/2026]
# Repositório: https://github.com/(20251ctb0100035-ai)/2026-PS
# ================================================
#
# DESCRIÇÃO:
# Este programa Processa as notas de uma turma e determina 
# a situação de cada aluno (Aprovado, Recuperação ou Reprovado).
# Conceitos utilizados: variáveis, tipos de dados, operadores,
# estruturas de seleção e estruturas de repetição.
# ================================================

# ---- ENTRADA DE DADOS ----

print("=== Sistema de Aprovação de Alunos ===")
print()  # linha em branco para organizar a saída

nome = input("Digite o nome do aluno: ")   # str - texto
nota1 = float(input("Digite a nota 1 (0 a 10): "))  # float - decimal
nota2 = float(input("Digite a nota 2 (0 a 10): "))  # float - decimal

#print(type(nota1))
#print(type(nome))

# ---- PROCESSAMENTO ----

media = (nota1 + nota2) / 2    # operador aritmético: soma e divisão

print()
print(f"Aluno  : {nome}") #f"..." é usado para imprimir o que foi digitado nessa variavel
print(f"Nota 1 : {nota1:.1f}")
print(f"Nota 2 : {nota2:.1f}")
print(f"Média  : {media:.2f}")  # :.2f - exibe com 2 casas decimais
media = nota1 + nota2 / 2 # Vai somar os dois valores e depois dividir por 2 dando a media do aluno

# ---- DECISÃO ----

if media >= 6.0:                        # condição principal
    situacao ="✅ Aprovado"
elif media >= 4.0:                       # condição alternativa (só verificada se a anterior for falsa)
    situacao = "⚠️ Recuperação"
else:                                    # caso nenhuma condição anterior seja verdadeira
    situacao = "❌ Reprovado"

print(f"Situação: (situacao)")
print(f"Situação: (situacao)")
print("-" * 40) # linha separadora: repete o caractere "-" 40 vezes

if nota1 or nota2 <= 2.0
    print("⚠️ Atenção: nota muito baixa em uma das avaliações.")

    #Bloco 4 / aula 4
