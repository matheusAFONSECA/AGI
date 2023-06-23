# imporatções necessarias para solucionar a questão
from sympy import Limit, Symbol, sqrt

# definindo o componente C da expressão
c = 1994 % 10       # C -> resto do numero de metricula dividido por 10

# definindo o simbolo
x = Symbol('x')

# definindo a expressão que vamos achar o limite
def funcao(x):
    return (((c + 1) - sqrt(x)) / ((c + 1)**2 - x))


# calculando o limite da expressão para x -> (c+1)²
limite = float(Limit(funcao(x), x, (c+1)**2).doit())

print("Resultado do limite para x -> 25: " + str(limite))
