# Python inclui uma biblioteca de funções para uso de tempo, incluindo uma função
# chamada asctime dentro do módulo time. Ela lê o horário atual direto do sistema
# operacional.
# Escreva um algoritmo que mostre o horário atual e a data.

from time import asctime

if __name__ == '__main__':
  horario = asctime().split(' ')
  print(horario)
  print(f'{horario[2]}/{horario[1]}/{horario[4]} - {horario[3]}')