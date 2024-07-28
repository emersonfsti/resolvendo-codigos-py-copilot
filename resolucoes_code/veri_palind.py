# ============================================================
# Nome: Emerson Felix
# Data/Hora: 28/07/2024 17:40
# Nome do Desafio: Verificando Palíndromos 🔄
# Descrição: 
# Vamos testar se uma palavra é um palíndromo?! Utilize conceitos 
# de manipulação de strings para inverter a palavra e comparar com 
# a original. Exemplo de palavras. (arara, radar, reviver, socos, 
# osso, mirim, anana)
#
# O que aprenderemos?
# - Manipulação de strings em Python, especialmente invertendo uma 
#   string.
# - Compreensão de como comparar a string original com sua versão 
#   invertida para determinar se é um palíndromo.
# - Introdução ao conceito de palíndromos e sua aplicação em 
#   problemas de programação.
# ============================================================

# Solicitando a palavra do usuário
palavra = input("Digite uma palavra: ")

# Invertendo a palavra
palavra_invertida = palavra[::-1]

# Verificando se a palavra é um palíndromo
if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")


# ============================================================
# - versão com valores iniciais informados
# ============================================================
palavra = "radar"

# Invertendo a palavra
palavra_invertida = palavra[::-1]

# Verificando se a palavra é um palíndromo
if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
