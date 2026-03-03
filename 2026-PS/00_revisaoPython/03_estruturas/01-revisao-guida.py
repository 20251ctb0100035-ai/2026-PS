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
