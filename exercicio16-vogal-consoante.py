# Escreva um algoritmo que que verifique se um caractere digitado pelo
# usuário é uma vogal ou consoante

def vogal_consoante(c:str):
  if c in ('aeiou'):
    print("o caractere digitado é uma vogal")
  else:
    print("o caractere digitado é uma consoante")

if __name__ == '__main__':
  char = input('Digite um caractere: ')
  vogal_consoante(char)