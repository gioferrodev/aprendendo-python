# Costuma-se dizer que um ano humano equivale a 7 anos caninos.
# No entanto, esta simples conversão não reconhece que os cães atingem
# a idade adulta em aproximadamente dois anos.
# Como resultado, algumas pessoas acreditam que é melhor contar cada um dos dois
# primeiros anos humanos como 10,5 anos caninos, e então contar cada ano
# humano adicional como 4 anos caninos.

# Escreva um programa que implemente a conversão de anos humanos para anos de cães descritos no parágrafo anterior. Certifique-se de que seu programa funcione corretamente para conversões de menos de dois anos humanos e para conversões de dois ou mais anos humanos. Seu programa deve exibir uma mensagem de erro apropriada se o usuário inserir um número negativo.

def idade_anos_caninos(idade:int):
  idade_canina=0
  if idade < 0:
    print("Idade não pode ser nagativa.")
  else:
    if idade >= 0 and idade <= 2:
      idade_canina = 10.5
      print(f"Idade canina igual a {idade_canina} anos")
    else:
      idade_canina = 10.5 + (idade -2) * 4
      print(f"Idade canina igual a {idade_canina} anos")


if __name__ == '__main__':
  idade = int(input("Digite uma idade humana: "))
  print(f"{idade} anos humanos equivalem a {idade_anos_caninos(idade)}")