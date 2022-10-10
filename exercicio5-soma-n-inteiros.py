# Escreva um algoritmo que leia um inteiro positivo N do usuário e imprima a
# soma dos números até N


def somatorio(n:int)->int:
  soma = n * (n+1)
  return soma / 2

n = int(input("digite um número: "))

print(f"A soma de 1 até {n} é {somatorio(n)}")