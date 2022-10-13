# Escreva um algoritmo que leia o valor de uma refeição que o usuário teve
# em um restaurante. O restaurante cobra os 1o% do garçom mais R$15 o cover artístico.

preco_refeicao = float(input("digite o valor da refeição -> "))
garcom = preco_refeicao * 0.10
print("="*15,"CONTA", "="*15)
print("="*10,"Preço do pedido - R$:",preco_refeicao)
print("="*10,"10% do garçom - R$:",garcom)
print("="*10,"Couver artístico - R$:",15)
print("="*10,"Total - R$:", preco_refeicao+garcom+15)