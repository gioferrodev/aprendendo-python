# Escreva um algoritmo que calcule o IMC (índice de massa corporal) de uma pessoa.

altura = float(input("Digite sua altura: "))
peso = float(input("digite seu peso: "))

imc = peso / (altura * altura)

print(f"Você tem {altura}m de altura e pesa {peso}kg. Logo, seu IMC é de {imc:0.2f}.")