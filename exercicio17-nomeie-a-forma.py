# Escreva um algoritmo que nomeie o de acordo com a qtd de lados digitados pelo usiário.
# Leia um valor de dados pelo usuário e o informe o nome do polígono de acordo com o valor.

n_lados = int(input("Digite um número de lados: "))

if n_lados <= 2:
    print("Um polígono necessita de três lados ou mais")
elif n_lados == 3:
    print(f"Um polígono de {n_lados}é um triângulo")
elif n_lados == 4:
    print(f"Um polígono de {n_lados}é um quadrilátero")
elif n_lados == 5:
    print(f"Um polígono de {n_lados}é um pentágono")
elif n_lados == 6:
    print(f"Um polígono de {n_lados}é um hexágono")
elif n_lados == 7:
    print(f"Um polígonod de {n_lados}é um heptágono")
elif n_lados == 8:
    print(f"Um polígono de {n_lados}é um octógono")
elif n_lados == 9:
    print(f"Um polígono de {n_lados}é um eneágono")
elif n_lados == 10:
    print(f"Um polígono de {n_lados}é um decágono")
else:
    print(f"Um polígono de {n_lados}")
