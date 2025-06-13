# exemplo 1:
tuplas = 1, 2, 3, 4, 5

print(tuplas)


# exemplo 2:
for i in range(len(tuplas)):
    print(i, tuplas[i])



# exemplo 3:
def valor_valorQuadrado_valorCubo(x):
    return x, x**2, x**3

resultado = valor_valorQuadrado_valorCubo(2)

print(resultado)


# exemplo 4: //DICIONARIOS

dicionario = {'a':2, 'b': 4, 'c': 6}

print(dicionario['b'])


# exemplo 5: //CADASTRO usando DICIONARIOS
cadastro_dic = {"nomes": ["José", "Maria", "Tulla"], "idades": [29, 25, 22], "cidades": ["Sp", "RJ", "BA"]}
print(cadastro_dic["nomes"])

cadastro_dic["alturas"] = [1.82, 1.78, 1.73]
# print(cadastro_dic)

del cadastro_dic["alturas"]
print(cadastro_dic)



# exemplo 6: Conjuntos
conjunto = {1, 15, True, "wesley", 29.0}
print(conjunto)

