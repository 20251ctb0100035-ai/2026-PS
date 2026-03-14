# SISTEMA DE CONVERSÃO DE UNIDADES
#
# Disciplina: Programação de Sistemas (PS)
# Aula: 07 Revisão: Módulos
# Autor: [Anthony Pagani]
# Data: [23/02/2026]
# Repositório: https://github.com/[20251ctb0100035-ai]/2026-PS
#

from conversores import (
    celsius_para_fahrenheit, celsius_para_kelvin, fahrenheit_para_celsius,
    km_para_milhas, milhas_para_km, metros_para_pes
)
from utils import cabecalho_secao, formatar_resultado, linha_separadora

def menu_temperatura():
    print(cabecalho_secao("Conversão de Temperatura"))
    valor = float(input("Valor em °C: "))
    print(formatar_resultado("°C → °F", valor, "°C", celsius_para_fahrenheit(valor), "°F"))
    print(formatar_resultado("°C → K", valor, "°C", celsius_para_kelvin(valor), "K"))

def menu_distancia():
    print(cabecalho_secao("Conversão de Distância"))
    valor = float(input("Valor em km: "))
    print(formatar_resultado("km → mi", valor, "km", km_para_milhas(valor), "mi"))
    print(formatar_resultado("km → pés", valor, "km", metros_para_pes(valor * 1000), "pés"))

def main():
    print(linha_separadora())
    print("SISTEMA DE CONVERSÃO DE UNIDADES")
    print(linha_separadora())
    
    opcoes = {
        "1": menu_temperatura,
        "2": menu_distancia
    }
    
    while True:
        print("\n(1) Temperatura (2) Distância [0] Sair")
        escolha = input("Opção: ").strip()
        
        if escolha == "0":
            print("\nSistema encerrado.")
            break
        elif escolha in opcoes:
            opcoes[escolha]()
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

# Função para conversão de massa (libras para kg)
def menu_massa():
    print(cabecalho_secao("Conversão de Massa"))
    valor = input("Valor em kg: ")
    try:
        valor = float(valor)
    except ValueError:
        print("Entrada inválida! Por favor, insira um número válido.")
        return
    
    print(formatar_resultado("kg → lb", valor, "kg", kg_para_lb(valor), "lb"))
    print(formatar_resultado("kg → g", valor, "kg", kg_para_g(valor), "g"))

    # Adicionando conversão inversa de libras para kg
    valor_libras = input("Valor em libras: ")
    try:
        valor_libras = float(valor_libras)
    except ValueError:
        print("Entrada inválida! Por favor, insira um número válido.")
        return
    
    print(formatar_resultado("lb → kg", valor_libras, "lb", libras_para_kg(valor_libras), "kg"))
