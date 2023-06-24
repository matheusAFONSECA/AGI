# imporatções necessarias para solucionar a questão
from sympy import Derivative, Symbol

# definindo o componente C da expressão
c = 1994 % 10       # C -> resto do numero de matricula dividido por 10

# definindo o simbolo
t = Symbol('t')


# definindo a expressão de deslocamento do objeto
def funcao(t):
    return (t**(1/3)/5) + ((c+1)/(t**3)) - ((c+2)*(t**2)) - 15


# Calculando a derivada da função do deslocamento -> velocidade
Derivada = Derivative(funcao(t), t).doit()

# Mostrando a equação de velocidade
print("Equação da velocidade: " + str(Derivada))

# Calculando a velocidade aos 7s
Velocidade = Derivative(funcao(t), t).doit().subs({t:7})
print("Velocidade em 7s : " + str(Velocidade) + " m/s")

# Calculando a derivada segunda do deslocamento -> aceleração
DerivadaSegunda = Derivative(funcao(t), t, 2).doit()

# Mostrando a equação da aceleração
print("Equação da aceleração: " + str(DerivadaSegunda))

# Calculando a aceleração em 2s
Aceleracao = Derivative(funcao(t), t, 2).doit().subs({t:2})
print("Aceleração em 2s: " + str(Aceleracao) + " m/s²")



