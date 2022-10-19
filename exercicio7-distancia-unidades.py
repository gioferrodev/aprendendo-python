# Crie um algoritmo que que peça ao usuário uma medida em pés e
# mostre a conversão em jardas e milhas.
# 1 pés = 0,33 jardas
# 1 pés = 0,00019

pes = int(input("digite a distância em pés -> "))
jardas = pes * 0.33
milhas = pes * 0.000189394

print(f"A distância de {pes} pés é equivalente a {jardas:.2f} jardas e {milhas:.2f} milhas.")