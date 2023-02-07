# O horóscopo é comumente representado usando a posição do sol em relação
# ao nascimento da pessoa. Este sistema astrológico divide o ano em 12 signos
# do zodíaco como é mostrado na tabela abaixo.
# =============================================
# Signo do zodíaco || Data
# =============================================
# Capricórnio   ||  22/Dezembro a 19/Janeiro
# Aquário   ||  20/Janeiro a 18/Fevereiro
# Peixes    ||  19/Fevereiro a 20/Março
# Áries     ||  21/Março a 19/Abril
# Touro     || 20/Abril a 20/Maio
# Gêmeos    || 21/Maio a 20/Junho
# Câncer    ||  21/Junho a 22/Junho
# Leão      || 23/Julho a 23/Agosto
# Virgem    || 23/Agosto a 22/Setembro
# Libra     ||  23/Setembro a 22/Outubro
# Escorpião || 23/Outubro a 21/Novembro
# Sagitário ||  22/Novembro a 21/Dezembro

# Escreva um programa em Python que peça ao usuário o dia e mês em que ele nasceu.
# O programa deve mostrar uma msg informando o seu signo
print('\n','*'*10, 'CALCULADORA DO ZODÍACO', '*'*10,'\n')

dia = int(input('digite o seu dia de nascimento: '))
mes = input('digite por extenso o mês do seu aniversário: ')


if mes == 'dezembro' and dia in range(22,31) or mes == 'janeiro' and dia in range(1,20):
    print('Você é do signo de capricórnio.')
elif mes == 'janeiro' and dia in range(20, 32) or mes == 'fevereiro' and dia in range(1, 19):
    print('Você é do signo de aquário.')
elif mes == 'feveiro' and dia in range(19, 29) or mes == 'março' and dia in range(1, 21):
    print('Você é do signo de peixes.')
elif mes == 'março' and dia in range(21, 32) or mes == 'abril' and dia in range(1, 20):
    print('Você é do signo de áries.')
else:
    print('Data inválida')
