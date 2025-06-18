# class Pessoa:

#     #metodo construtor
#     def __init__(self, name, age, home):
        
#        #inicializar os atributos da classe
#        self.nome = name
#        self.idade = age
#        self.residencia = home


# #instanciar a classe (criar os objetos)

# wesley = Pessoa('Wesley', 28, 'SP')

# print(wesley.nome)
# print(wesley.idade)
# print(wesley.residencia)


# wesley.idade += 1
# print(wesley.idade)

# wesley.residencia = 'Paris'
# print(wesley.residencia)

# print(vars(wesley))



class Pessoa:

    #metodo construtor
    def __init__(self, name, age, home):
        
       #inicializar os atributos da classe
       self.nome = name
       self.idade = age
       self.residencia = home

       self.num_filhos = 0
       self.profissao = None
    
    def fala(self, mensagem):
        print(f'{self.nome}', "diz:", f'{mensagem}')

    def consegue_emprego(self, prof, valor_salario):
        self.profissao = prof
        self.salario = valor_salario

    def aumento_salario(self, porcentagem):
        self.aumento = self.salario * (1 + porcentagem)


maria = Pessoa(name='Maria', age=25, home='Londres')

# print(vars(maria))

maria.fala('Meu nome é Maria')

maria.consegue_emprego("Cientista de Dados", 7000)
print(maria.profissao, maria.salario)
maria.aumento_salario(0.2)
print(maria.profissao, maria.salario, maria.aumento)