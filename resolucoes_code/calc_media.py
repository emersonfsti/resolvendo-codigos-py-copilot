# ============================================================
# Nome: Emerson Felix
# Data/Hora: 28/07/2024 17:35
# Nome do Desafio: Calculando Média de Notas 📚
# Descrição: 
# Agora vamos calcular a média de três notas fornecidas na entrada 
# do usuário. Utilize operadores aritméticos para realizar o 
# cálculo da média.
#
# O que aprenderemos?
# - Uso de variáveis para armazenar dados fornecidos pelo usuário.
# - Aplicação de operadores aritméticos (+, /) para calcular a 
#   média de um conjunto de valores.
# - Prática na solicitação e manipulação de entrada do usuário.
# ============================================================

# Solicitando as três notas do usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calculando a média das notas
media = (nota1 + nota2 + nota3) / 3

# Exibindo o resultado
print(f"A média das notas é: {media:.2f}")

# ============================================================
# - versão com valores iniciais informados
# ============================================================

nota1 = 10.0
nota2 = 6.5
nota3 = 7.5

# Calculando a média das notas
media = (nota1 + nota2 + nota3) / 3

# Exibindo o resultado
print(f"A média das notas é: {media:.2f}")