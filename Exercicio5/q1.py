# imporatções necessarias para solucionar a questão
from sympy import Symbol, exp, solve

# definindo o componente C da expressão
c = 1994 % 10       # C -> resto do numero de metricula dividido por 10

# definindo o simbolo
x = Symbol('x')


# definindo a expressão que vamos resolver -> exp: exponencial de base 'e'
def funcao(x):
    return exp(-x - 1) + exp(-x - 3) + exp(x) + 5*(c + 1)


# solucionando a questão
resultado = solve(funcao(x))

# mostrando o resultado da questão
print("A solução da equação é: " + str(resultado))
