class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fala (self):
        return(f"{self.nome} faz barulho!")

a1 =  Animal('grilo')

print(a1)