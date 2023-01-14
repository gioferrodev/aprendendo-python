# Um triângulo pode ser classificado de acordo com a medida dos seus lados como:
# Equilátero, isóceles ou escaleno. Todos os lados de um triângulo equilátero são iguais.
# O triângulo isóceles têm dois lados iguais e um diferente e o triângulo escaleno tem todos
# lados diferentes.
# Escreva um algoritmo que leia os três lados de um triângulo e imprima na tela se ele é equilátero, isóceles ou escaleno.

lado1 = int(input('digite a medida do lado 1 do triângulo: '))
lado2 = int(input('digite a medida do lado 1 do triângulo: '))
lado3 = int(input('digite a medida do lado 1 do triângulo: '))

if lado1 == lado2 == lado3:
    print('O triângulo é equilátero.')
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
    print('o triângulo é escaleno.')
else:
    print('O triângulo é isóceles.')