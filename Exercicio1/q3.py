# imporatções necessarias para solucionar a questão
from sympy import Limit, Symbol, sqrt, S

# definindo o componente C da expressão
c = 1994 % 10       # C -> resto do numero de matricula dividido por 10

# definindo o simbolo
x = Symbol('x')


# definindo a expressão que vamos achar o limite
def funcao(x):
    return ((c + 1) - sqrt(x)) / ((c + 1)**2 - x)


# calculando o limite da expressão para x -> -∞
limite = float(Limit(funcao(x), x, -S.Infinity).doit())

print("Resultado do limite para x -> -∞: " + str(limite))
