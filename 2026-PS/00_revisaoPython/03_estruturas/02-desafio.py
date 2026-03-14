catalogo = [
    {"titulo": "O Programador Pragmático", "autor": "Andrew Hunt", "ano": 1999, "disponível": True},
    {"titulo": "Código Limpo", "autor": "Robert C. Martin", "ano": 2008, "disponível": False},
    {"titulo": "Entendo Algoritmos", "autor": "Aditya Bhargava", "ano": 2016, "disponível": True},
]

def listar(livros):
    for i, l in enumerate(livros, 1):
        status = "Disponível" if l["disponível"] else "Emprestado"
        print(f"{i}. {l['titulo']} ({l['ano']}) - {l['autor']} | {status}")

def cadastrar():
    catalogo.append({
        "titulo": input("Título: "),
        "autor": input("Autor: "),
        "ano": int(input("Ano: ")),
        "disponível": True
    })

def buscar_autor():
    a = input("Autor: ").lower()
    encontrados = [l for l in catalogo if a in l["autor"].lower()]
    if encontrados: listar(encontrados)
    else: print("Nenhum livro encontrado.")

def emprestar_devolver():
    t = input("Título: ").lower()
    for l in catalogo:
        if t == l["titulo"].lower():
            l["disponível"] = not l["disponível"]
            print(f"{'Emprestado' if not l['disponível'] else 'Devolvido'}: {l['titulo']}")
            return
    print("Livro não encontrado.")

def relatorio():
    total = len(catalogo)
    disponiveis = sum(l["disponivel"] for l in catalogo)
    emprestados = total - disponiveis
    print(f"\nTotal: {total} | Disponíveis: {disponiveis} | Emprestados: {emprestados}")
    print("Livros emprestados:", [l["titulo"] for l in catalogo if not l["disponível"]])

while True:
    op = input("\n(1) Listar (2) Cadastrar (3) Buscar por autor (4) Emprestar/Devolver (5) Relatório [0] Sair: ").strip()
    if op == "1": listar(catalogo)
    elif op == "2": cadastrar()
    elif op == "3": buscar_autor()
    elif op == "4": emprestar_devolver()
    elif op == "5": relatorio()
    else: print("Opção inválida. Tente novamente.")