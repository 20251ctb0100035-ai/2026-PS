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

def exibir_rodape():
    """Sistema encerrado."""
    print("=" * 40)
    print("   Sistema encerrado.")
    print("=" *  40)

exibir_rodape()

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

def mostrar_versao():
    print(f"Versão do sistema: {versao}")  

mostrar_versao()

#Bloco 3
