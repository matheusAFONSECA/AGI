# imporatções necessarias para solucionar a questão
from sympy import Symbol, solve

# definindo o componente C da expressão
c = 1994 % 10       # C -> resto do numero de matricula dividido por 10

# definindo o valor das tensões
V1 = 7 + (2*c)
V2 = 12 + (2*c)

# definindo os simbolos matemáticos
i1 = Symbol('i1')
i3 = Symbol('i3')


# equacionando a malha 1 em sentido horário
def m1(v1, i1, i3):
    return -v1 + 25*i1 + 10*i1 + 10*i3


# equacionando a malha 2 em sentido anti-horário
def m2(v2, i1, i3):
    return -v2 + 20*i3 + 10*i3 + 10*i1


# definindo as funções para serem resolvidas
funcao1 = m1(V1, i1, i3)
funcao2 = m2(V2, i1, i3)

# resolvendo as equações -> fazendo assim igualamos as equações das melhas à 0 e resolve o sistema de equações
resultado = solve((funcao1, funcao2))

# como i2 é no sentido contrário de i1 e i3 podemos multiplicar por -1
i2 = (resultado[i1] + resultado[i3]) * (-1)

# mostrando os resultados das correntes
print("Corrente 1: " + str(resultado[i1]) + " A")
print("Corrente 2: " + str(i2) + " A")
print("Corrente 3: " + str(resultado[i3]) + " A")
