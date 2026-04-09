# ------------------------------------------------
# Meme Gambling 
# Jogo de azar onde o usuário pode ganhar memes ou perder, dependendo da combinação de símbolos sorteados.
# ================================================
# DISCIPLINA : Programação de sistemas (PS)
# AULA       : Mini-Projeto
# Autor      : [Anthony Pagani e Rafael Lopes]
# Data       : [29/03/2026]
# ================================================

import random
import os
#Criara a pasta dados.txt dentro da pasta para evitar problemo no caminho
PASTA_ATUAL = os.path.dirname(os.path.abspath(__file__))
ARQUIVO = os.path.join(PASTA_ATUAL, "dados.txt")
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
            f.write(f"{resultado}\n")
    except Exception as e:
        print(f"Erro ao salvar o resultado: {e}")

# Verificar ganha
def verificar_ganha(Sequence):    
    if Sequence == ("🍋", "🍋", "🍋"):
        return "Meme: https://youtu.be/97JDCEN80yM?si=nTk9HUXRTsgenyXi"
    elif Sequence == ("🍒", "🍒", "🍒"):
        return "Meme: https://youtu.be/daFzNfSK3b4?si=Vv3J3rFxE2i9VCZA"
    elif Sequence == ("🔔", "🔔", "🔔"):
        return "Meme: https://youtu.be/dQw4w9WgXcQ?si=im3qezEJO_Mwh7to"
    else:
        return "Droga..."

# Entrada
def Leia():         # Loop principal do jogo, onde o usuário pode escolher entre girar ou sair
    user_input = input("Digite seu nome antes de começar: ")
    print(f"Bem vindo {user_input}! Vamos jogar Meme Gambling!")

    jackpot = 0
    falhas = 0

    while True:
        print("\n--- Meme Gambling ---")
        print("R - Girar")
        print("SAIR - Encerrar")
        
        opcao = input("Escolha uma opção: ").upper()
        
        if opcao == 'R':
            A = random.choice(["🍋", "🍒", "🔔"])    
            B = random.choice(["🍋", "🍒", "🔔"])
            C = random.choice(["🍋", "🍒", "🔔"])
            print(f"Simbolo sorteado: {A}")
            print(f"Simbolo sorteado: {B}")
            print(f"Simbolo sorteado: {C}")
            
            resultado = Sequence(A, B, C)       
            Escreva("Sequencia", resultado)
            
            answer = A, B, C          
            if answer == ("🍋", "🍋", "🍋") or answer == ("🍒", "🍒", "🍒") or answer == ("🔔", "🔔", "🔔"):
                print("JACKPOT!")
                jackpot += 1
            else:
                print("Que pena, tente novamente!")
                falhas += 1
            
            
            memes = verificar_ganha(answer)
            print("MEME SORTEADA:", memes)
            
            # Aqui ele envia para a função salvar que agora funciona
            salvar(resultado)
            
        elif opcao == 'SAIR':       # Se o usuário escolher sair, o loop é encerrado e uma mensagem de despedida é exibida
            print(f"Volte sempre! Até a próxima, {user_input}!")
            if jackpot > falhas:
                print("Parabéns, você gastou toda a sua sorte com memes, vocé é sortudo!")
            else:
                print("Infelizmente você não adquirio nada, mas você não gastou toda sua sorte com isso tmb...")
            break

def Sequence(A, B, C):
    return A, B, C

# Saída
def Escreva(msg, resultado):
    print(f'{msg} = {resultado}')

# Executar
if __name__ == '__main__':
    load()
    Leia()