# ==================================================
# SISTEMA DE CÁLCULO DE IMC
# ==================================================
# Disciplina : Programação de sistemas (PS)
# Aula       : 06 - Revisão: Funções
# Autor      : Anthony Pagani
# Data       : 03/03/2026
# Repositório: https://github.com/20251ctb0100035-ai/2026-PS
# ==================================================
#
# DESCRIÇÃO:
# Calcula e classifica o IMC de uma pessoa.
# Demonstra definição de funções, parâmetros,
# retorne, escopo e recursão.
# ==================================================

# ---- FUNÇÃO SEM PARÂMETROS E SEM RETORNO ---- 

def exibir_cabecalho():
    """Exibe o cabeçalho do sistema no terminal."""   # docstring: documentação da função
    print("=" * 40)
    print("   SISTEMA DE CÁLCULO DE IMC")
    print("=" *  40)

# Chamando a função
exibir_cabecalho() #Se for exibido 3 vezes ou mais vai mostrar a mesma mensagem normalment mas sem o exibir_cabecalho() não mostra a mensagem

# ---- FUNÇÃO COM PARÂMETROS E COM RETORNO ----

def calcular_imc(peso, altura):
    """Calcula e retorna o IMC. Fórmula: peso / altura²."""
    imc = peso / (altura ** 2)   # * * é o operador de potência
    return imc                   # devolve o resultado para quem chamou

# Coletando dados do usuário
peso    = float(input("Peso (kg): "))
altura  = float(input("Altura (m): "))

# Chamando a função e armazenando o retorno
resultado = calcular_imc(peso, altura)
print(f"Seu IMC é: {resultado:.2f}")

# ---- ESCOPO LOCAL vs. GLOBAL ----

versao = "1.0"  # variável GLOBAL - existe fora de qualquer função

def demonstre_escopo():
    mensagem = "Olá do interior da função!"  # variável LOCAL
    print("Dentro da função:")
    print(f"  Mensagem = {mensagem}")   # OK: local exist aqui
    print(f"  Versão   = {versao}")     # OK: global é visível dentro

demonstre_escopo()

print("\nFora da função:")
print(f"  Versão   = {versao}")     # OK: global existe aqui
# print(mensagem)                 # ERRO: local não existe aqui!

# ---- VALOR PADRÃO E MÚLTIPLOS RETORNOS ----

def classificar_imc(imc, unidades="kg/m²"):
    """Classifica o IMC e retorna a classificação e emoji de status. Parâmetro 'unidades' tem valor padrão - não é obrigatório informar."""

    if imc < 18.5:
        classificacao = "Abaixo do peso"
        emoji = "⬇️"
    elif imc < 25.0:
        classificacao = "Peso normal"
        emoji = "✅"
    elif imc < 30.0:
        classificacao = "Sobrepeso"
        emoji = "⚠️"
    else:
        classificacao = "Obesidade"
        emoji = "❌"

    return classificacao, emoji # retorna dois valores - Python empacota como tupla

# Chamando sem o parâmetro opcional (usa o valor padrão "kg/m²")
imc_teste = 22.5
classificacao, emoji = classificar_imc(imc_teste)
print(f"IMC {imc_teste} ({classificacao}) {emoji}")

# Chamada informando o parâmetro opcional
classificacao, emoji = classificar_imc(imc_teste, unidades="lb/in²")
print(f"Mesma chamando com unidade customizada: {classificacao} {emoji}")

# ---- RECURSÃO BÁSICA ----

def contagem_regressiva (n):
    """Exibe uma contagem regressiva de n até 0 usando recursão."""
    if n < 0:               # CASO BASE: para a recursão
        return
    print(n)
    contagem_regressiva(n - 1)  # CHAMADA RECURSIVA: resolve um subproblema menor

print("\n--- Contagem regressiva ---")
contagem_regressiva(5)

# Fatorial: exemplo clássico de recursão com retorno
def fatorial(n):
    """Calcula n! recursivamente. Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120"""
    if n == 0:              # caso base
        return 1
    return n * fatorial(n - 1)  # caso recursivo

print("\n--- Fatorial ---")
for i in range(1, 7):
    print(f"{i}! = {fatorial(i)}")

