# Arquivo: 01b-debug.py
# ATENÇÃO: 4 erros propositais. Encontre e corrija todos!

catalogo = [
    {"titulo": "Código Limpo",          "autor": "Robert C. Martin", "disponivel":
True},
    {"titulo": "Entendendo Algoritmos", "autor": "Aditya Bhargava", "disponivel":
False},
    {"titulo": "Python Fluente",        "autor": "Luciano Ramalho",
"disponivel": True},
]

print("Primeiro livro:", catalogo[0]["titulo"]) # tem que accesar o primeiro livro (índice 0) e a chave "titulo"

print("\nLivros disponíveis:")
for livro in catalogo:
    if livro["disponivel"] == True:   # o erro estava aqui, tinha que ser "disponivel" e não "disponível" # e tmb true para poder acessar os livros disponíveis
        print(f' ✅ {livro["titulo"]}')

total = len(catalogo)
print(f"\nTotal de livros: {total}")

for chave, valor in catalogo[0].items(): # faltou o  "items()" para acessar as chaves e valores do dicionário
    print(f" {chave}: {valor}")

primeiro_autor = catalogo[0]["autor"]  # autor estava escrito errado(Autor(o erro))
print("\nAutor do primeiro livro:", primeiro_autor)
