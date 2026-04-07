# ------------------------------------------------
# Meme Gambling 
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
def verificar_ganha(valor):     # Verifica se o valor é 3, 6 ou 9 e retorna o meme correspondente
    if valor == 3:
        return "Meme: https://youtu.be/97JDCEN80yM?si=nTk9HUXRTsgenyXi"
    elif valor == 6:
        return "Meme: https://youtu.be/daFzNfSK3b4?si=Vv3J3rFxE2i9VCZA"
    elif valor == 9:
        return "Meme: https://youtu.be/dQw4w9WgXcQ?si=im3qezEJO_Mwh7to"
    else:
        return "Droga..."

# Entrada
def Leia():         # Loop principal do jogo, onde o usuário pode escolher entre girar ou sair
    while True:
        print("\n--- Meme Gambling ---")
        print("R - Girar")
        print("SAIR - Encerrar")
        
        opcao = input("Escolha uma opção: ").upper()
        
        if opcao == 'R':
            A = random.randint(1, 3)        # Gera números aleatórios entre 1 e 3
            B = random.randint(1, 3)
            C = random.randint(1, 3)
            print(f"Número sorteado: {A}")
            print(f"Número sorteado: {B}")
            print(f"Número sorteado: {C}")
            
            resultado = Soma(A, B, C)       # Calcula a soma dos números sorteados
            Escreva("Soma", resultado)
            
            answer = A + B + C          # Calcula a soma dos números sorteados
            if answer == 3 or answer == 6 or answer == 9:
                print("Parabéns, você acertou o número!")
            else:
                print("Que pena, tente novamente!")
            
            memes = verificar_ganha(answer)
            print("MEME SORTEADA:", memes)
            
            # Aqui ele envia para a função salvar que agora funciona
            salvar(resultado)
            
        elif opcao == 'SAIR':       # Se o usuário escolher sair, o loop é encerrado e uma mensagem de despedida é exibida
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