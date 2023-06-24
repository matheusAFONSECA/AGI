# imporatções necessarias para solucionar a questão
from sympy import Symbol, solve

# definindo o componente C da expressão
c = 1994 % 10       # C -> resto do numero de matricula dividido por 10

# definindo o simbolo
x = Symbol('x')


# definindo a expressão que vamos resolver
def funcao(x):
    return (c + 2)*x**3 - (c + 1)*x**2 - 5*x + 4*c


# solucionando a questão
resultado = solve(funcao(x))

# mostrando o resultado da questão
print("A solução da equação é: " + str(resultado))
