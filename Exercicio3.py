# imporatções necessarias para solucionar a questão
from sympy import Integral, Symbol

# definindo o componente C da expressão
c = 1994 % 10       # C -> resto do numero de matricula dividido por 10

# definindo o simbolo
x = Symbol('x')


# definindo a expressão de força variável que esta sendo aplicada no objeto
def funcao(x):
    return ((x**2)/5) + x**(4/5) + ((c + 3)*x) - 10


# calculando a intergral da função de força variável -> trabalho em entre 1m e 12m de deslocamento
Trabalho = Integral(funcao(x), (x, 1, 12)).doit()
print("Trabalho realizado entre 1m e 12m foi de " + str(Trabalho) + " J")
