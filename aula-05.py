# exemplo 1:
# def fala_oi():
#     print("Oi")

# fala_oi()



# exemplo 2:
# def fala_oi_pra_alguem(nome_de_alguem):
#     print(f"Oi {nome_de_alguem}, que bom te ver!")


# fala_oi_pra_alguem("Wesley")



# exemplo 3:
# def fala_oi_pra_alguem(nome_de_alguem = 'Wesley'):
#     print(f"Oi {nome_de_alguem}, que bom te ver!")

# fala_oi_pra_alguem()


# exemplo: 4:
# def cumprimento_parte_do_dia(nome, parte_do_dia):

#     if parte_do_dia == "manhã":
#         cumprimento = "Bom dia"
#     elif parte_do_dia == "tarde":
#         cumprimento = "Boa tarde"
#     elif parte_do_dia == "noite":
#         cumprimento = "Boa noite"
#     else:
#         raise ValueError(f"A parte do dia informada ({parte_do_dia}) não é valida!")
    
#     cumprimento = f"{cumprimento}, {nome}"
#     print(cumprimento)

#     return cumprimento

# cumprimento_parte_do_dia("Wesley", "manhã")
# // também pode usar assim: cumprimento_parte_do_dia(nome="Wesley", parte_do_dia="manhã") atribuindo corretamente a cada variavel//



# exemplo 5:
# def calculor_subtracao(n1, n2):
#     return n1 - n2


# resultado = calculor_subtracao(5, 1)

# print(resultado)



# exemplo 6:
# def multiplica_soma(n1, n2):
#     return n1 * n2

# resultado = multiplica_soma(2, 2)

# print(resultado)




# 7: Problema gerador!: CALCULADORA
# def calc_soma(n1, n2):
#     return n1 + n2

# def calc_sub(n1, n2):
#     return n1 - n2

# def calc_div(n1, n2):
#     return n1 / n2

# def calc_mult(n1, n2):
#     return n1 * n2

# def calculadora(n1, n2, op):
#     if op == "+":
#         return calc_soma(n1, n2)
#     elif op == "-":
#         return calc_sub(n1, n2)
#     elif op == "/":
#         return calc_div(n1, n2)
#     elif op == "*":
#         return calc_mult(n1, n2)
#     else:
#         raise ValueError(f"O operador informado ({op}) não é um operador valido!")
    
# print(calculadora(2, 10, "%"))


# 7,1 : Também é de boas praticas usar apenas um return e não varios, colocando dentro do if uma variavel que podemos chamar de resp // exemplo abaixo:

def calc_soma(n1, n2):
    return n1 + n2

def calc_sub(n1, n2):
    return n1 - n2

def calc_div(n1, n2):
    return n1 / n2

def calc_mult(n1, n2):
    return n1 * n2

def calculadora(n1, n2, op):
    if op == "+":
        resp = calc_soma(n1, n2)
    elif op == "-":
        resp = calc_sub(n1, n2)
    elif op == "/":
        resp = calc_div(n1, n2)
    elif op == "*":
        resp = calc_mult(n1, n2)
    else:
        raise ValueError(f"O operador informado ({op}) não é um operador valido!")
    return resp
    
print(calculadora(2, 10, "+"))