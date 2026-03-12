import sys

# Entrada
def Leia():
    estoque = []

    print('=== Cadastro de Produtos (digite sair para terminar) ===')

    while True:
        nome = input('Nome do produto: ')

        if nome == 'sair':
            break

        quantidade = int(input('Quantidade em estoque: '))

        estoque.append((nome, quantidade)) 

    Escreva(estoque)

# Saída
def Escreva(estoque):
    print('\n=== Estoque Cadastrado ===')

    if len(estoque) == 0:
        print('Nenhum produto cadastrado.')
        return

    for produto in estoque:
        nome = produto[0]
        quantidade = produto[1]
        print(f'{nome} - Quantidade: {quantidade}')

Leia()