catalogo = [
    {"titulo": "O Programador Pragmático", "autor": "Andrew Hunt",      "disponivel": 
True},
    {"titulo": "Codigo Limpo",             "autor": "Robert C. Martin", "disponivel": 
False},
    {"titulo": "Padrões de Projeto",        "autor": "Erich Gamma",     "disponivel":
True}
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
    autor  = input("Autor: ").strip()

    if not titulo or not autor:
        print("⚠️ Título e Autor são obrigatórios.")
        return
    
    catalogo.append({
        "titulo":     titulo,
        "autor":      autor,
        "disponivel": True
    })
    print(f"✅  '{titulo}' adicionado com sucesso!") #chamando adicionar_livro() seguido de listar_livros(): o usuário pode ver o novo livro adicionado imediatamente no catálogo.

def buscar_livro():
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
    listar_livros()
    if not catalogo:
        return
    print("\n--- Registrar Empréstimo ---")

    try:
        numero = int(input("Número do livro: "))  # valueError se digitar letras

        if numero < 1 or numero > len(catalogo):
            print("⚠️ Número fora do intervalo.")
            return
        
        livro = catalogo[numero - 1]   # -1 porque lista começa em 0

        if not livro["disponivel"]:
            print(f"⚠️ '{livro['titulo']}' já está emprestado.")
        else:
            livro["disponivel"] = False
            print(f"✅  Empréstimo registrado de '{livro['titulo']}' registrado.")

    except ValueError:
        print("❌ Entrada inválida. Digite um número.")

        # Número válido de livro disponível → deve registrar: o empréstimo marcara o livro como indisponível.
        # Número de livro já emprestado → deve avisar: mostrara que o livro já está emprestado.
        # Digite abc → o ValueError deve ser capturado sem quebrar o programa: o programa mostra uma mensagem de erro mas continua rodando normalmente.

def devolver_livro():
    listar_livros()
    if not catalogo:
        return
    print("\n--- Registrar Devolução ---")

    try:
        numero = int(input("Número do livro: "))
        livro  = catalogo[numero - 1] # IndexError se número for negativo > len
      
        if livro["disponivel"]:
            print(f"⚠️ '{livro['titulo']}' já está disponível.")
        else:
            livro["disponivel"] = True
            print(f"✅  Devolução de '{livro['titulo']}' registrada.")

    except ValueError:
        print("❌ Digite apenas o número do livro.")
    except IndexError:
        print("❌ Número fora da lista. Verifique os livros cadastrados.")

def menu():
    print("\n📚 SISTEMA DE BIBLIOTECA - v1 (em memória)")

    opcoes = {
        "1": ("Listar livros",          listar_livros),
        "2": ("Adicionar livro",        adicionar_livro),
        "3": ("Buscar livro",           buscar_livro),
        "4": ("Registrar empréstimo",   registrar_emprestimo),
        "5": ("Registrar devolução",    devolver_livro),
        "0": ("Sair",                   None),
    }

    while True:
        print("\n Opções:")
        for chave, (descricao, _) in opcoes.items():
            print(f"  {chave}. {descricao}")

        try:
            escolha = input("\n sua escolha: ").strip()
            if escolha not in opcoes: 
                raise ValueError(f"Opção '{escolha}' inválida.")
            
        except ValueError as e:
            print(f"⚠️ {e}")
            continue           # volta ao while - não executa else/finally abaixo

        else:
            # Executa SOMENTE quando try terminar sem exceção
            if escolha == "0":
                print("\n Até logo! 📚")
                break
            _, funcao = opcoes[escolha]
            funcao()

        finally:
            # Executa SEMPRE - com ou sem exceção
            # Aqui: didático. Em produção: fecha arquivos, conexões, etc.
            pass


    if __name__ == "__main__": # ao digitar 7, x em um capo branco o arquivo não é encontrado mas o programa não fecha mas mostrara uma mensagem de erro e continuara rodando, da pra tentar novamente ou escolher outra opção no menu.
        menu()
        
# Centralizar o nome evita erros de digitação em todo o código
ARQUIVO = "biblioteca.txt"
SEPARADOR = "|" # separa campos em cada linha do .txt

# Formato de cada linha no arquivo:
# titulo|autor|disponivel
# Exemplo:
#   Código Limpo|Robert C. Martin|False 

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
        # 'w' = write: cria se não existir, sobrescreve se existir
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            for livro in catalogo:
               #salvar_catalogo([{"titulo": "Teste", "autor": "Autor", "disponivel": True}]) # vai mostrar Teste|Autor|True mas ao remover antes de testar: o arquivo não é encontrado mas o programa não fecha mas mostrara uma mensagem de erro e continuara rodando mas da pra tentar denovo ou escolher outra opção no menu.
                linha = f"{livro['titulo']}{SEPARADOR}{livro['autor']}{SEPARADOR}{livro['disponivel']}\n"
                f.write(linha)
            print(f"💾  catálogo salvo em '{ARQUIVO}'.")
    except IOError as e:
        # IOError: disco cheio, permissão negada, etc.
        print(f"❌ Erro ao salvar: {e}")

        # precisam chamar salvar catalogo: adicionar_livro, registrar_emprestimo, devolver_livro/ e n precisa chamar: listar_livros, buscar_livro

