# ============================================================
# Nome: Emerson Felix
# Data/Hora: 28/07/2024 17:30
# Nome do Desafio: Verificando Números Pares e Ímpares 🧮
# Descrição: 
# Como entrada, receba um número inteiro e verifique se ele é 
# par ou ímpar. Utilize condicionais para realizar a verificação 
# e, se possível, faça uso do Github Copilot (ou outra IA) para 
# otimizar a estrutura do código.
#
# O que aprenderemos?
# - Utilização de condicionais em Python (if, else) para 
#   realizar verificações.
# - Introdução ao conceito de operador de módulo (%) para 
#   verificar se um número é par ou ímpar.
# - Exploração do uso de uma ferramenta de IA, como o Github 
#   Copilot, para otimizar a estrutura do código.
# ============================================================

# Solicitando o número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Verificando se o número é par ou ímpar usando o operador de módulo
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")

# ============================================================
# - versão com valores iniciais informados
# ============================================================

numero = 21

# Verificando se o número é par ou ímpar usando o operador de módulo
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")