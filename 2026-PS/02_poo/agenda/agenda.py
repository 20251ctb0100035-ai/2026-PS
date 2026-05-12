#=======================================================
# Disciplina : Programação de Sistemas
# Aula       : 23 - Menu interativo e persistência de objetos
# Tipo       : Gabarito (Mão na Massa)
# Autor      : Anthony Pagani
# Data       : 07/05/2026
# Descrição  : Agenda de Contatos com menu, CRUD em memória
#              e dois formatos de persistência (.txt e binário).
#              serve de modelo para o Sistema de Hotel para Pets V2.0.
#=======================================================

"""
agenda.py - Aula 23 (programação de sistemas, 2026)
Agenda de Contatos: classe Inicial.
"""

# ====================================================
# CLASSE Contato - representa um contato da agenda
# ====================================================
# Em vez de guardar nome, telefone e email em três lista paralelas
# (um padrão estrutarado, frágil e propenso a erros), agrupamos esses
# dados - e os comportamentos relacionados - dentro de uma classe.
class Contato:
    """ Representa um contato simples na agenda."""

def __init__(self, nome, telefone, email):
    # O construtor é o "cartório" do objeto: aqui registramos
    # tudo o que esse Contato precisa saber sobre si mesmo.
    self.nome = nome
    self.telefone = telefone
    self.email = email

def exibir(self):
    # Comportamento (método) que pertence ao objeto: o próprio
    # contato sabe se mostar. Assim, quem usa a classe não
    # precisa saber por dentro como ela é organizado
    print(f" Nome     : {self.nome}")
    print(f" Telefone : {self.telefone}")
    print(f" Email    : {self.email}")

def para_linha_txt(self):
    # Cada contato sabe se transformar em UMA linha de texto.
    # Por que dentro da classe? Porque o formato é detalhe da
    # representação do contato - quem é o dono da informação
    # deve ser dono da forma de expoortá-la (encapsulamento).
    # Separador escolhido: ponto-e-vírgula ("';").
    return f"{self.nome};{self.telefone};{self.email}"

# Teste rápido da classe
if __name__ == "__main__":
    c1 = Contato("Maria Silva", "42 99999-0001", "maria@email.com")
    c1.exibir()

def menu():
    # Carregamos o estado salvo da execução anterior (se existir)
    # Escolhemos o formato binário porque preserva os objetos intactos.
    contatos = carregar_de_binario("contatos.bin")

    while True: # loop infinito - só sai com break
        print("\n======== Agenda ========")
        print("1 - Cadastrar Contato")
        print("2 - Listar Contatos")
        print("3 - Remover Contato")
        print("4 - Salvar em .txt")
        print("5 - Salvar em binário")
        print("0 - Sair")
        opcao = input("opção: ")

        # Despacho por opção. Cada caso chama uma função especializado
        # - o menu não sabe NADA sobre como cadastrar, listar etc.
        # Essa separação entre "interface" e "lógica" é o que permite
        # trocar o menu por uma GUI no futuro sem reescrever o sistema.
        if opcao == "1":
            cadastrar(contatos)
        elif opcao == "2":
            listar(contatos)
        elif opcao == "3":
            remover(contatos)
        elif opcao == "4":
            salvar_em_txt(contatos, "agenda.txt")
        elif opcao == "5":
            salvar_em_binario(contatos, "agenda.bin")
        elif opcao == "0":
            # Antes de sair, salvamos automaticamente. Garantia de
            # que o usuário não perde o trabalho da sessão.
            salvar_em_binario(contatos, "agenda.bin")
            print("Até logo!")
        break
    else:
        print("Opção inválida.")

#===================================================
# PONTO DE ENTRADA
#===================================================
# O if abaixo só roda se o arquivo for executado diretamente
# (python agenda.py), e NÃO se for importado por outro arquivo.
# É uma boa prática de organização que veremos com mais cuidado
# adiante, quando começarmos a separar código em vários arquivos
if __name__ == "__main__":
    menu()

def cadastrar(contatos):
    print("\n--- Novo Contato ---")
    nome = input("Nome : ")
    telefone = input("Telefone : ")
    email = input("Email : ")
    contatos.append(Contato(nome, telefone, email))
    print("✓Contato cadastrado.")

def listar(contatos):
    if not contatos:
        print("\n(agenda vazia)")
        return
    print(f"\n--- Agenda ({len(contatos)} contatos) ---")
    for i, c in enumerate(contatos, start=1):
        print(f"\n[{i}]")
        c.exibir()


def remover(contatos):
    listar(contatos)
    if not contatos:
        return
    indice = int(input("\nNᵒ do contato a remover: ")) - 1
    if 0 <= indice < len(contatos):
        removido = contatos.pop(indice)
        print(f"✓ Contato '{removido.nome}' removido.")
    else:
        print("Índice inválido.")
# ====================================================
# PERSISTÊNCIA EM TEXTO (.txt)
# ====================================================
# Vantagem: humano lê. Desvantagem: tudo vira string e a "remontagem"
# do objeto é manual (perdemos tipos, classe, métodos).

def salvar_em_txt(contatos, caminho):
    """Grava cada contato em uma linha no arquivo de texto."""
    # Modo "w": abre para escrita e SOBRESCREVE o conteúdo existente.
    # encoding="utf-8": garante que acentos funcionem corretamente.
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for c in contatos:
            # Cada contato sabe se transformar em uma linha de texto  
            # o formato
            linha = f"{c.nome};{c.telefone};{c.email}\n"
            arquivo.write(linha)
    print(f"✓ {len(contatos)} contatos(s) salvo(s) em {caminho}")

def carregar_de_txt(caminho):
    contatos = []
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                # strip() remove o \n e espaços nas pontas.
                linha = linha.strip()
                if not linha:
                    # Pula linhas em branco (mais robusto).
                    continue
                # split(";") quebra a linha em pedaços usando o separador.
                # Aqui aparece a fragilidade do .txt: se algum campo tiver
                # ponto-e-vírgula no conteúdo, esse parsing quebra.
                partes = linha.split(";")
                nome, telefone, email = partes[0], partes[1], partes[2]
                # Reconstrução manual do objeto a partir das strings.
                contatos.append(Contato(nome, telefone, email))
    except FileNotFoundError:
        # Na primeira execução, o arquivo não existe - Começamos vazio.
        # Sem esse tratamento, o programa quebraria ao iniciar.
        print(f"Arquivo {caminho} ainda não existe. Começando vazio.")
    return contatos

# Importamos pickle: módulo padrão do Python para "serializar" objetos
# (transformar um objeto Python em bytes que podem ser gravados em disco
# e depois recuperados intactos).
import pickle #(Rick)

# ====================================================
# PERSISTÊNCIA EM BINÁRIO (pickle)
# ====================================================
# pickle "congela" o objeto inteiro: classe, atributos e tipos
# preservados. Vantagem: zero parsing manual. Desvantagem: só Python lê
# e existe risco de segurança ao abrir .bin de fontes desconhecidos.

def salvar_em_binario(contatos, caminho):
    # Modo "wb": write binary. NÃO usamos encoding aqui - não é texto.
    with open(caminho, "wb") as arquivo:
        # pickle.dump grava QUALQUER objeto Python.
        # lista inteira; ele cuida de tudo.
        pickle.dump(contatos, arquivo)
    print(f"✓ {len(contatos)} contatos(s) salvo(s) em {caminho}")


def carregar_de_binario(caminho):
    try:
        with open(caminho, "rb") as arquivo:
            # pickle.load reconhece o formato e reconstruí o objeto
            # original - sem que precisemos escrever nenhuma "remontagem".
            return pickle.load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo {caminho} ainda não existe. Começando vazio.")
        return []
