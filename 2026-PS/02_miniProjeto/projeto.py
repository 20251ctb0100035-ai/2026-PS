# ------------------------------------------------
# Roleta
# ================================================
# DISCIPLINA : Programação de sistemas (PS)
# AULA       : Mini-Projeto
# Autor      : [Anthony Pagani e Rafael Lopes]
# Data       : [29/03/2026]
# ================================================


import random

ARQUIVO = "dados.txt"
SEPARADOR = "|"

# Carregar histórico Ajustado para ler e mostrar o conteúdo do arquivo
def load():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            print("\n--- Histórico de Resultados ---")
            for linha in f:
                print(linha.strip())
    except FileNotFoundError:
        print("\nArquivo de histórico ainda não existe.")
    except Exception as e:
        print(f"Erro ao carregar os resultados: {e}")

# Salvar resultado
def salvar(resultado):
    try:
        with open(ARQUIVO, "a", encoding="utf-8") as f:
            f.write(f"Resultado: {resultado}\n")
    except Exception as e:
        print(f"Erro ao salvar o resultado: {e}")

# Verificar ganha
def verificar_ganha(valor):
    if valor == 3:
        return "APPLE"
    elif valor == 6:
        return "CHERRY"
    elif valor == 9:
        return "LEMON"
    else:
        return "NÃO GANHOU"

# Entrada
def Leia():
    while True:
        print("\n--- Roleta ---")
        print("R - Girar")
        print("SAIR - Encerrar")
        
        opcao = input("Escolha uma opção: ").upper()
        
        if opcao == 'R':
            A = random.randint(1, 3)
            B = random.randint(1, 3)
            C = random.randint(1, 3)
            print(f"Número sorteado: {A}")
            print(f"Número sorteado: {B}")
            print(f"Número sorteado: {C}")
            
            resultado = Soma(A, B, C)
            Escreva("Soma", resultado)
            
            answer = A + B + C
            if answer == 3 or answer == 6 or answer == 9:
                print("Parabéns, você acertou o número!")
            else:
                print("Que pena, tente novamente!")
            
            fruit = verificar_ganha(answer)
            print("FRUTA SORTEADA:", fruit)
            
            # Aqui ele envia para a função salvar que agora funciona
            salvar(resultado)
            
        elif opcao == 'SAIR':
            print("Saindo do jogo. Até a próxima!")
            break

def Soma(A, B, C):
    return (A + B + C)

# Saída
def Escreva(msg, resultado):
    print(f'{msg} = {resultado}')

# Executar
if __name__ == '__main__':
    load()
    Leia()