# Programa que calcula KPI do bonus de vendas de 2024 que é de 1000 + salário * bonus

# Variáveis de entrada

´´´python
nome = input("Digite o seu nome: ")
salario = float(input("Digite o seu salário: "))
bonus = float(input("Digite o valor da sua porcentagem de bonus: "))
´´´

# Cálculo do KPI do bonus de vendas

´´´python
bonus_porcentagem = float((1000 + salario) * (bonus / 100))
valor_total = float(1000 + salario + bonus_porcentagem)
´´´

# Exibição do resultado

´´´python
print(f"Olá {nome}, o seu bonus foi de: {valor_total:.2f}")
´´´
