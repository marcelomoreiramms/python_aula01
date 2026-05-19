# Programa que calcula o KPI do bonus de vendas de 2024 que é: 1000 + salário * bonus

# Variáveis de entrada e validação de dados
nome = input("Digite o seu nome: ")
if nome.isdigit():
    print("Você digitou um nome inválido!")
    exit()
elif nome.isspace():
    print("Você não digitou um nome inválido.")
    exit()
elif len(nome.strip()) == 0:
    print("Você não digitou um nome inválido.")
    exit()

salario = input("Digite o seu salário: ")
try:
    salario.strip() != ""
    salario = float(salario)
    salario > 0
except ValueError:
    print("Erro: Digite um valor válido!")
    exit()
if salario <= 0:
    print("Erro: O salário deve ser maior que zero!")
    exit()

bonus = input("Digite o valor da sua porcentagem de bonus: ")
try:
    bonus.strip() != ""
    bonus = float(bonus)
    bonus > 0
    bonus <= 100
except ValueError:
    print("Erro: Digite um valor válido!")
    exit()
if bonus <= 0:
    print("Erro: O bonus deve ser maior que zero!")
    exit()
elif bonus > 100:
    print("Erro: O bonus deve ser menor ou igual a 100!")
    exit()

# Cálculo do KPI do bonus de vendas
bonus_porcentagem = float(salario * (bonus / 100))
valor_total = float(1000 + salario + bonus_porcentagem)

# Exibição dos resultados
print(f"Olá {nome.title()}, o seu bonus foi de: {valor_total:.2f}")
