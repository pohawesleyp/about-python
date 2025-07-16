class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fala (self):
        return(f"{self.nome} faz barulho!")

a1 =  Animal('grilo')

print(f"O {a1.fala()}")



class Cachorro:
    def __init__(self, nome):
        self.nome = nome

    def fala (self):
        return(f"O {self.nome} late!")

c1 =  Cachorro ('Totó')

print(f"{c1.fala()}")