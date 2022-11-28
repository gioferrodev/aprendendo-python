# Escreva um algoritmo que leia um valor do usuário e verifique se o valor é
# par ou ímpar.

def par_impar(n:int)->bool:
  return n % 2 == 0

if __name__ == '__main__':
  valor = int(input('Digite um valor: '))
  if par_impar(valor):
    print("O valor é par.")
  else:
    print("O valor é ímpar.")