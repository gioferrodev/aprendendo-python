# Escreva um algoritmo que leia dois inteiros A e B, do usuário. O algoritmo deve
# computar e mostrar:
# * A soma de A e B
# * A diferença quando B é subtraido de A
# * O produto de A e B
# * O quociente quando A é dividido por B
# * O resto da divisão de A por B
# * O resultado de A elevado a B

def soma(a:int, b:int)->int:
  return a+b

def diferenca(a:int, b:int)->int:
  return b-a

def produto(a:int, b:int)->int:
  return a*b

def quociente(a:int, b:int)->int:
  return a//b

def resto(a:int, b:int)->float:
  return a%b

if __name__ == "__main__":
  a=int(input("digite um número -> "))
  b=int(input("digite outro número -> "))

  print(f"A soma de {a} com {b} é: ",soma(a,b))
  print(f"A diferença quando {b} é subtraído de {a} é: ",diferenca(a,b))
  print(f"O produto de {a} e {b}:", diferenca(a,b))
  print(f"O quociente quando {a} é dividido por {b} é: ",quociente(a,b))
  print(f"O resto da divisão de {a} por {b} é: ",resto(a,b))