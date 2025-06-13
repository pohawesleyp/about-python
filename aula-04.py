# dia, mes, ano = 1, 2, 2000
# nome = 'wesley'

# print("{:02d}/{:02d}/{:04d}".format(dia, mes, ano))

# print(f"{dia:02d}/{mes:02d}/{ano:04d}")
# print(nome)

# preco = 245845.4575115517
# print(f'R${preco:.2f}')

opcoes_validas = {
    "S", "C", "D", "V", 
    "SOLTEIRO", "CASADO", "DIVORCIADO", "VIUVO", 
    "SOLTEIRA", "CASADA", "DIVORCIADA", "VIUVA"
}

prompt = "Digite seu estado civil (opções possíveis: S, C, D, V): "
estado_civil = input(prompt).upper()

while estado_civil not in opcoes_validas:
    print("Resposta inválida! Digite seu estado civil (opções possiveis: S, C, D, V:) ")
    estado_civil = input(prompt).upper()

print(f"\nEstado civil registrado: {estado_civil}")