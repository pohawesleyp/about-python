# produtos = [
#     {"nome": 'Batata', "quantidade": 10, "preco": 5.0},
#     {"nome": 'Cebola', "quantidade": 1, "preco": 0.97},
#     {"nome": 'Cenoura', "quantidade": 3, "preco": 2.57},
#     {"nome": 'Banana', "quantidade": 1, "preco": 4.20}
#     ]

# quantidadeProdutos = 0

# for produto in produtos:
#     quantidadeProdutos += produto["quantidade"]


# print(quantidadeProdutos)



# minha_lista = [10, 4, 20, 5, 30, 15, 25]

# def encontrar_tres_maiores(lista_numeros):
#     if len(lista_numeros) < 3:
#         print("A lista tem menos de 3 números. Retornando os números disponíveis.")
#         return (lista_numeros)
    

#     primeiro_maior = float('-inf')
#     segundo_maior = float('-inf')
#     terceiro_maior = float('-inf')

   
#     for numero in lista_numeros:
#         if numero > primeiro_maior:
#             terceiro_maior = segundo_maior
#             segundo_maior = primeiro_maior
#             primeiro_maior = numero
#         elif numero > segundo_maior and numero != primeiro_maior:
#             terceiro_maior = segundo_maior
#             segundo_maior = numero
#         elif numero > terceiro_maior and numero != primeiro_maior and numero != segundo_maior:
#             terceiro_maior = numero

#     return [primeiro_maior, segundo_maior, terceiro_maior]



# maiores = encontrar_tres_maiores(minha_lista)
# print(f"Os três maiores valores em {minha_lista} são: {maiores}")



# class Caixinha:
#     def __init__(self, saldo_inicial=0):
#         if not isinstance(saldo_inicial, (int, float)) or saldo_inicial < 0:
#             print("Erro: O saldo inicial deve ser um número positivo ou zero. Definindo saldo para 0.")
#             self.__saldo = 0
#         else:
#             self.__saldo = saldo_inicial
#         print(f"Caixinha criada com saldo inicial de R${self.__saldo:.2f}")


#     def depositar(self, valor):
#         if not isinstance(valor, (int, float)) or valor <= 0:
#             print("Erro: O valor do depósito deve ser um número positivo.")
#             return False 
        
#         self.__saldo += valor
#         print(f"Depósito de R${valor:.2f} realizado com sucesso.")
#         self.ver_saldo()
#         return True 


#     def sacar(self, valor):
#         if not isinstance(valor, (int, float)) or valor <= 0:
#             print("Erro: O valor do saque deve ser um número positivo.")
#             return False
        
#         elif self.__saldo - valor < 0:
#             print(f"Erro: Saldo insuficiente. Saldo atual: R${self.__saldo:.2f}. Valor solicitado: R${valor:.2f}")
#             return False
#         else:
#             self.__saldo -= valor
#             print(f"Saque de R${valor:.2f} realizado com sucesso.")
#             self.ver_saldo()
#             return True

#     def ver_saldo(self):
#         print(f"Saldo atual da caixinha: R${self.__saldo:.2f}")
#         return self.__saldo

#     def __str__(self):
#         return f"Caixinha (Saldo: R${self.__saldo:.2f})"



# print("--- Teste da Caixinha 1 ---")
# minha_caixinha = Caixinha()
# minha_caixinha.ver_saldo()

# minha_caixinha.depositar(100.50)
# minha_caixinha.sacar(30.00)
# minha_caixinha.ver_saldo()

# minha_caixinha.sacar(150.00) # Tentativa de saque para saldo insuficiente
# minha_caixinha.ver_saldo()

# minha_caixinha.depositar(200)
# minha_caixinha.sacar(25.75)

# print("\n--- Teste da Caixinha 2 (com saldo inicial) ---")
# caixinha_do_wes = Caixinha(saldo_inicial=500)
# caixinha_do_wes.ver_saldo()
# caixinha_do_wes.sacar(550) # Tentativa de saque insuficiente
# caixinha_do_wes.sacar(400)
# print(caixinha_do_wes)

# print("\n--- Teste com entradas inválidas ---")
# minha_caixinha.depositar(-50)
# minha_caixinha.sacar(0)
# caixinha_invalida = Caixinha(saldo_inicial="abc") # Saldo inicial inválido



numeroInput = input("Escreva um numero: ")

numero = int(numeroInput)

if numero % 2 == 0:
    numero == "par"
    print(f"O numero {numero} digitado é par")
else:
    numero == "impar"
    print(f"O numero {numero} digitado é impar")