# debug_teste/0lb-debug.py
# ATENÇÃO: 4 erros propositais. Encontre e corrija todos!
# Rode de dentro de 05_modulos/: python debug_teste/01b-debug.py

from conversores import Temperatura # faltou importar a classe Temperatura do módulo conversores

from conversores import celsius_para_kelvin #converter_distancia é uma função do módulo distancia, não do módulo temperatura
resultado = celsius_para_kelvin(25)
print(f"25°C em K: {resultado}")

from utils.formatador import formatar_resultado
print (formatar_resultado("teste", 100, "km", 62.1, "mi")) # argumento "extra" não é necessário, a função formatar_resultado espera apenas 5 argumentos, e aqui foram passados 6. Remova o argumento "extra" para corrigir o erro.

from conversores import km_para_milhas
print (f"50 km = {km_para_milhas(50):.2f} mi")

# from debug_teste import algo # O módulo algo não existe dentro de debug_teste
