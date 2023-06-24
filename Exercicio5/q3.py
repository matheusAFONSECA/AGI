# imporatções necessarias para solucionar a questão
from sympy import Symbol, sin, solve

# definindo o componente C da expressão
c = 1994 % 10       # C -> resto do numero de metricula dividido por 10

# definindo o simbolo
x = Symbol('x')


# definindo a expressão que vamos resolver
def funcao(x):
    return 2*sin(4 * (c - 3) * x) - 10


# solucionando a questão
resultado = solve(funcao(x))

# mostrando o resultado da questão
print("A solução da questão é: " + str(resultado))
