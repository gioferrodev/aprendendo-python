# A seguinte tabela lista os nívens de sons em decibéis alguns sons comuns.
# SOM   NÍVEIS DE DECIBÉIS (db)
# ---   -------------------
# Britadeira  130
# Cortador de grama 106
# ASpirador 70
# Sala vazia  40

# Escreva um algortimo que leia o nível de som do usuário.
# Se o usuário digitar um nível de decibel correspondente aos níveis acima, informar ao usuário em qual nível o valor digitado se encontra

nivel_digitado = int(input('Digite o valor do nível do decibel: '))

if nivel_digitado < 40:
  print(f"{nivel_digitado}db é um valor de decibéis é pequeno demais.")
elif nivel_digitado>= 40 and nivel_digitado < 70:
  print(f"{nivel_digitado}db é equivalente a uma sala vazia.")
elif nivel_digitado>= 70 and nivel_digitado < 106:
  print(f"{nivel_digitado}db é equivalente a um aspirador.")
elif nivel_digitado>= 106 and nivel_digitado < 130:
  print(f"{nivel_digitado}db é equivalente a uma britadeira.")
