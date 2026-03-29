# Centralizar o nome evita erros de digitação em todo o código
ARQUIVO = "biblioteca.txt"
SEPARADOR = "|"  # separa campos em cada linha do .txt

# Formato de cada linha no arquivo:
# titulo|autor|disponivel
# Exemplo:
# Código Limpo|Robert C. Martin|False

catalogo = [
    {"titulo": "O Programador Pragmático", "autor": "Andrew Hunt", "disponivel": True},
    {"titulo": "Codigo Limpo", "autor": "Robert C. Martin", "disponivel": False},
    {"titulo": "Padrões de Projeto", "autor": "Erich Gamma", "disponivel": True}
]

def listar_livros():
    """Exibe todos os livros com numeração e status."""
    print("\n" + "=" * 50)
    print("  📚 CATÁLOGO DA BIBLIOTECA")
    print("=" * 50)

    if not catalogo:
        print("Nenhum livro cadastrado.")
        return

    for i, livro in enumerate(catalogo, 1):
        status = "✅ Disponível" if livro["disponivel"] else "❌ Emprestado"
        print(f"    {i}. {livro['titulo']} - {livro['autor']} [{status}]")

    print("=" * 50)

def adicionar_livro():
    """Coleta dados via input e adiciona um novo livro ao catálogo."""
    print("\n--- Adicionar Novo Livro ---")

    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()

    if not titulo or not autor:
        print("⚠️ Título e Autor são obrigatórios.")
        return
    
    for livro in catalogo:
        if livro["titulo"].lower() == titulo.lower():
            print("⚠️ Livro já cadastrado.")
            return

    catalogo.append({
        "titulo": titulo,
        "autor": autor,
        "disponivel": True
    })
    print(f"✅  '{titulo}' adicionado com sucesso!")
    salvar_catalogo(catalogo)

def buscar_livro():
    """Busca livro por título ou autor."""
    print("\n--- Buscar Livro ---")
    termo = input("Digite o título ou autor para buscar: ").strip().lower()

    try:
        resultados = [l for l in catalogo if termo in l["titulo"].lower()]

        if not resultados:
            print("  Nenhum livro encontrado.")
            return
        
        print(f"\n  {len(resultados)} resultado (s):")
        for livro in resultados:
            status = "Disponível" if livro["disponivel"] else "Emprestado"
            print(f"  ● {livro['titulo']} - {livro['autor']} [{status}]")    

    except Exception as e:
        print(f"❌  Erro inesperado: {e}")

def registrar_emprestimo():
    """Registra o empréstimo de um livro."""
    listar_livros()
    if not catalogo:
        return

    print("\n--- Registrar Empréstimo ---")

    try:
        numero = int(input("Número do livro: "))

        if numero < 1 or numero > len(catalogo):
            print("⚠️ Número fora do intervalo.")
            return

        livro = catalogo[numero - 1]

        if not livro["disponivel"]:
            print(f"⚠️ '{livro['titulo']}' já está emprestado.")
        else:
            livro["disponivel"] = False
            print(f"✅  Empréstimo registrado de '{livro['titulo']}'.")
            registrar_historico("Empréstimo", livro["titulo"])
            salvar_catalogo(catalogo)

    except ValueError:
        print("❌ Entrada inválida. Digite um número.")
    except IndexError:
        print("❌ Número fora da lista. Verifique os livros cadastrados.")

def devolver_livro():
    """Registra a devolução de um livro."""
    listar_livros()
    if not catalogo:
        return

    print("\n--- Registrar Devolução ---")

    try:
        numero = int(input("Número do livro: "))
        livro = catalogo[numero - 1]

        if livro["disponivel"]:
            print(f"⚠️ '{livro['titulo']}' já está disponível.")
        else:
            livro["disponivel"] = True
            print(f"✅  Devolução de '{livro['titulo']}' registrada.")
            registrar_historico("Devolução", livro["titulo"])
            salvar_catalogo(catalogo)

    except ValueError:
        print("❌ Digite apenas o número do livro.")
    except IndexError:
        print("❌ Número fora da lista. Verifique os livros cadastrados.")

from datetime import datetime

def registrar_historico(acao, titulo):
    """Registra ação no histórico."""
    try:
        with open("historico.txt", "a", encoding="utf-8") as f:
            data = datetime.now().strftime("%d/%m/%Y %H:%M")
            f.write(f"{data} - {acao}: {titulo}\n")
    except IOError as e:
        print(f"❌ Erro ao registrar histórico: {e}")

def ver_historico():
    """Exibe o histórico de empréstimos e devoluções."""
    print("\n--- Histórico ---")
    try:
        with open("historico.txt", "r", encoding="utf-8") as f:
            linhas = f.readlines()
        if not linhas:
            print("Nenhum registro no histórico.")
            return
        for linha in linhas:
            print(f"  {linha.strip()}")
    except FileNotFoundError:
        print("Nenhum histórico registrado ainda.")

def relatorio():
    """Exibe relatório dos livros."""
    total = len(catalogo)
    disponiveis = sum(1 for l in catalogo if l["disponivel"])
    emprestados = total - disponiveis

    print("\n📊 RELATÓRIO")
    print(f"Total: {total}")
    print(f"Disponíveis: {disponiveis}")
    print(f"Emprestados: {emprestados}")

def menu():
    """Menu principal do sistema de biblioteca."""
    print("\n📚 SISTEMA DE BIBLIOTECA - v1")

    opcoes = {
        "1": ("Listar livros", listar_livros),
        "2": ("Adicionar livro", adicionar_livro),
        "3": ("Buscar livro", buscar_livro),
        "4": ("Registrar empréstimo", registrar_emprestimo),
        "5": ("Registrar devolução", devolver_livro),
        "6": ("Ver histórico", ver_historico),
        "7": ("Relatório", relatorio),
        "0": ("Sair", None),
    }

    while True:
        print("\n Opções:")
        for chave, (descricao, _) in opcoes.items():
            print(f"  {chave}. {descricao}")
    
        try:
            escolha = input("\nSua escolha: ").strip()
            if escolha not in opcoes:
                raise ValueError(f"Opção '{escolha}' inválida.")
        
        except ValueError as e:
            print(f"⚠️ {e}")
            continue
        
        if escolha == "0":
            print("\nAté logo! 📚")
            break
        
        _, funcao = opcoes[escolha]
        if funcao:
            funcao()

def carregar_catalogo():
    """Lê o .txt e reconstrói a lista de dicionários."""
    catalogo = []
    try:
        # 'r' = leitura | encoding='utf-8' garante acentos corretos
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if not linha:           # ignore linhas vazias
                    continue
                partes = linha.split(SEPARADOR)
                if len(partes) != 3:    # linha malformada - pula
                    continue
                titulo, autor, disponivel_str = partes
                catalogo.append({
                    "titulo":      titulo,
                    "autor":       autor,
                    # a string "True" no arquivo precisa virar bool True
                    "disponivel": disponivel_str == "True" 
                })
    except FileNotFoundError:
        pass   # primeira execução: arquivo ainda não existe - tudo bem 
    return catalogo

def salvar_catalogo(catalogo):
    """Grava toda a lista no arquivo .txt."""
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            for livro in catalogo:
                linha = f"{livro['titulo']}{SEPARADOR}{livro['autor']}{SEPARADOR}{livro['disponivel']}\n"
                f.write(linha)
        print(f"💾  Catálogo salvo em '{ARQUIVO}'.")
    except IOError as e:
        print(f"❌ Erro ao salvar: {e}")


if __name__ == "__main__":
    catalogo = carregar_catalogo()
    menu()