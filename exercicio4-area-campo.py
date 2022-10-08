# Escreva um algoritmo que peça ap usuário que entre com a largura e comprimento 
# de um campo de um fazendeiro  em pés e depois mostre a área desse campop em acres.

largura = float(input("digite a largura do campo em pés: "))
altura = float(input("digite a altura do campo em pés: "))

area_acre = (altura * largura) / 43560

print(f"Esse campo tem {area_acre} acres de área.")