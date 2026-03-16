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

# ---- Dados da turma ----
# Uma lista de dicionários, onde cada dicionário representa um aluno

turma = [
    {"nome": "Ana",   "nota1": 8.0, "nota2": 7.5},
    {"nome": "Bruno", "nota1": 4.5, "nota2": 5.0},
    {"nome": "Carla", "nota1": 2.0, "nota2": 3.5},
]

print("=== RESULTADOS DA TURMA ===")
print()

# O 'for' percorre cada aluno na lista automaticamente, sem precisar de um índice
for aluno in turma:
    nome = aluno["nome"]
    nota1 = aluno["nota1"]
    nota2 = aluno["nota2"]
    media = (nota1 + nota2) / 2

if media >= 6.0:                        # condição principal
    situacao ="✅ Aprovado"
elif media >= 4.0:                       # condição alternativa (só verificada se a anterior for falsa)
    situacao = "⚠️ Recuperação"
else:                                    # caso nenhuma condição anterior seja verdadeira
    situacao = "❌ Reprovado"

    print(f"Aluno    : {nome}")
    print(f"Media    : {media:.2f}")
    print(f"Situação : {situacao}")
    print("-" * 30)
    