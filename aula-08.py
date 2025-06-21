# EXEMPLO 1:
# class Horario:

#     def __init__(self, hora, min, seg):
#         self.h = hora
#         self.m = min
#         self.s = seg

# agora = Horario(15, 12, 30)

# # print(agora)
# print(vars(agora))

# print(f'{agora.h}:{agora.m}:{agora.s}')

# EXEMPLO 2:
class Horario:

    def __init__(self, hora, min, seg):
        self.h = hora
        self.m = min
        self.s = seg
    
    def __repr__(self):
        return f"O horário é: {self.h}:{self.m}:{self.s}"
    
agora = Horario(15, 12, 30)

print(agora)


# EXEMPLO 3:
class Horario:

    def __init__(self, hora, min, seg):
        self.h = hora
        self.m = min
        self.s = seg
    
    def __str__(self):
        return f"O horário é: {self.h}:{self.m}:{self.s}"
    
h1 = Horario(15, 12, 30)

print(h1)


# EXEMPLO 4:

import pandas as pd

df = pd.DataFrame({"a": [1, 2, 3, 4, 5],
                   "b": [6, 7, 8, 9, 10]})

print(df)


# EXEMPLO 5:

n1 = 'abacate'
n2 = 'abacaxi'

n3 = n1.__add__(n2)

print(n3)


# EXEMPLO 6:

n1 = 2
n2 = 8

n3 = n1.__add__(n2)

print(n3)


# EXEMPLO 7:

n1 = 'ada'

n2 = n1.__mul__(3)

print(n2)



# EXEMPLO 8:
class Horario:

    def __init__(self, hora, min, seg):
        self.h = hora
        self.m = min
        self.s = seg
    
    def __str__(self):
        return f"O horário de saida é: {self.h}:{self.m}:{self.s}"
    
    def __add__(self, other):
        se = self.s + other.s
        mi = self.m + other.m
        ho = self.h + other.h 

        if se >= 60:
            mi += 1    ## mi = mi + 1
            se -= 60   ## se = se - 60
        
        if mi >= 60:
            ho += 1
            mi -= 60
        
        if ho >= 24:
            ho -= 24

        return Horario(ho, mi, se)


hora1 = Horario(9, 27, 42)
hora2 = Horario(8, 0, 0)
hora3 = hora1 + hora2

print(hora3)



# EXEMPLO 9:
class Horario:

    def __init__(self, hora, min, seg):
        self.h = hora
        self.m = min
        self.s = seg
    
    def __str__(self):
        return f"O horário de saida é: {self.h}:{self.m}:{self.s}"
    
    def __add__(self, other):
        se = self.s + other.s
        mi = self.m + other.m
        ho = self.h + other.h 

        if se >= 60:
            mi += 1    ## mi = mi + 1
            se -= 60   ## se = se - 60
        
        if mi >= 60:
            ho += 1
            mi -= 60
        
        if ho >= 24:
            ho -= 24

        return Horario(ho, mi, se)
    
    def __gt__(self, other):
        if self.h > other.h:
            return True
        
        elif self.h == other.h and self.m > other.m:
            return True
        
        elif self.h == other.h and self.m == other.m and self.s > other.s:
            return True
        
        return False ##else


hora1 = Horario(9, 27, 42)
hora2 = Horario(8, 0, 0)


print(hora1 < hora2)
