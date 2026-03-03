# ===============================================
# SISTEMA DE BIBLIOTECA
# ===============================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 05 - Revisão: Estruturas de Dados
# Autor      : [Anthony Pagani]
# Data       : [26/06/2026]
# Repositório: https://github.com/[20251ctb0100035-ai]/2026-PS
# ===============================================
#
# DESCRIÇÃO:
# Catálogo de livros que demonstra o uso de listas
# e dicionários para armazenar, consultar e filtrar
# dados estruturado.
# ===============================================

# ---- LISTAS: CONCEITO BÁSICO ----

# Criando uma Lista de titulos
titulos = [
    "O Programador Pragmático",
    "Código Limpo",
    "Entendendo Algoritmos",
]

# Acesso por indice (começa em 0, não em 1!)
print("Primeiro livro:", titulos[0])
print("Último livro  :", titulos[-1])   # indice -1 = último elemento
print("Total de livros:", len(titulos))
# Ao acessar o titulos[3] vai dar erro e o erro é que isso faz os elementos tarem fora de alcance da ordem esperada(Eu acho)
# no titulos[-2] o ultimo livro é Código Limpo

# ---- MÉTODOS DE LISTA ----

print("\n--- Operações na lista ---")

# Adicionar um item ao final
titulos.append("Python Fluente")
print("Após append:", titulos)

# Verificar se um item existe
busca = "Código Limpo"
if busca in titulos:
    print(f'"{busca}" está no catálogo.')
else:
    print(f'"{busca}" não encontrado.')

# Ordenar a lista
titulos.sort()
print("Listas ordenada:", titulos)

# Remover um item
titulos.remove("Entendendo Algoritmos")
print("Após remove:", titulos)
# se remover um titulo que N existe vai continuar com o processo mas vai dar erro mesmo assim se for colocado qualquer coisa depois

# .sort() acho que cria uma nova para poder ordenar/arrumar a lista
def new_func(titulos):
    for index, titulo in enumerate(titulos):
        print(f"{index + 1}.0 {titulo}")

new_func(titulos)
# Um dicionário representa um livro com seus atributos

# ---- DICIONÁRIOS: CONCEITO BÁSICO ----

# Um dicionário representa um livro com seus atributos
livro = {
    "titulo":      "O Programador Pragmático",
    "autor":       "Andrew Hunt",
    "ano":         1999,		      # int, não string
    "disponível":  True,		     # bool
}

# Acessando valores pelas chaves
print("Titulo:", livro["titulo"])
print("Autor: ", livro["autor"])
print("Ano    ", livro["ano"])
print("Status ", "Disponível" if livro["disponível"] else "Emprestado")
# ---- MODIFICANDO E CONSULTANDO ----

# Atualizando um valor existente
livro ["disponivel"] = False # livro foi emprestado
print("\nApós empréstimo:", livro["disponivel"])

# Adicionando uma nova chave
livro ["paginas"] = 352
print("Páginas:", livro["paginas"])

# .get() acesso seguro: retorna None (ou padrão) se a chave não existir
editora = livro.get("editora", "Não informada")
print("Editora:", editora) # não lança KeyError, retorna o padrão

# ---- CATÁLOGO: LISTA DE DICIONÁRIOSCATÁLOGO: LISTA DE DICIONÁRIOS ----

catalogo = [
    {"titulo": "0 Programador Pragmático", "autor": "Andrew Hunt", "ano": 1999,
"disponivel": True},
    {"titulo": "Código Limpo", "autor": "Robert C. Martin", "ano": 2008,
"disponivel": False},
    {"titulo": "Entendendo Algoritmos", "autor": "Aditya Bhargava", "ano": 2016,
"disponivel": True},
    {"titulo": "Clean Architecture", "autor": "Robert C. Martin", "ano": 2017,
"disponivel": True},
]

print("=== Catálogo da Biblioteca ===")
print()

# Percorrendo cada livro com for

for indice, livro in enumerate(catalogo):
    status = "Disponível" if livro["disponivel"] else "Emprestado"
    # Adicionando o número do livro (indice + 1) antes do título
    print(f'{indice + 1}. {livro["titulo"]} ({livro["ano"]})')
    print(f' Autor: {livro["autor"]} | {status}')
print("-" * 40)

# ---- CONSULTAS E FILTROS ----

disponiveis = 0
emprestados = 0
for livro in catalogo:
    if livro["disponivel"]:
        disponiveis += 1                      # filtra apenas os disponíveis
    else:           
        emprestados += 1
print(f"Disponíveis: {disponiveis} | Emprestados: {emprestados}")


print("\n=== Busca por título ===")
busca = input("Digite o título (ou parte): ").lower()
encontrado = False
for livro in catalogo:
    if busca in livro ["titulo"].lower():       #.lower() ignora maiúsculas/minúsculas
       print(f' Encontrado: {livro["titulo"]} - {livro["autor"]}')
       encontrado = True
if not encontrado:
     print(" Nenhum livro encontrado com esse termo.")

print("\n=== Atributos do primeiro livro ===")
for chave, valor in catalogo[0].items():        #.items() retorna pares (chave, valor)
    print(f" {chave}: {valor}")

# Arquivo: 01b-debug.py
# ATENÇÃO: 4 erros propositais. Encontre e corrija todos!

catalogo = [
    {"titulo": "Código Limpo",      "autor": "Robert C. Martin","disponivel":
True},
    {"titulo": "Entendendo Algoritmos", "autor": "Aditya Bhargava", "disponivel":
False},
    {"titulo": "Python Fluente",          "autor": "Luciano Ramalho",
"disponivel": True},
]

print("Primeiro livro:", catalogo[0]["titulo"])

print("\nLivros disponíveis:")
for livro in catalogo:
    if livro["disponivel"] == True:
        print(f' ✓ {livro["titulo"]}')

total = len (catalogo)
print(f"\nTotal de livros: {total}")

for chave, valor in catalogo[0].items():
    print(f" {chave}: {valor}")

primeiro_autor = catalogo [0] ["autor"]
print("\nAutor do primeiro livro:", primeiro_autor)
