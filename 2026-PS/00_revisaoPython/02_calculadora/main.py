import sys

# Entrada
def Leia():
    op = input('Digite a Operação [* / + - sair]: ')
    if op == 'sair':
        sys.exit()
    A = int(input('Digite um valor: '))
    B = int(input('Digite outro valor: '))
    msg = f'{A} {op} {B}'
    if op == '+':     
        res = Soma(A, B)
    elif op == '-':
        res = Subtração(A, B)
    elif op == '*':
        res = Multiplicação(A, B)
    elif op == '/':
        res = Divisão(A, B)
    else:
        res = 'Operação inválida'
    Escreva(msg, res)
# Soma
def Soma(A, B):
    return (A+B)
# Subtração
def Subtração(A, B):
    return (A-B)
# Multiplicação
def Multiplicação(A, B):
    return (A*B)
# Divisão
def Divisão(A, B):
    return (A/B)
# Saída
def Escreva(msg, resultado):
    print(f'{msg} = {resultado}')

Leia()
