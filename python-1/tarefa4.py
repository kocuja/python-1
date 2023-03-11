#4. Faça  um  programa  que  receba  dois  números  reais,  realize  as operações básicas: soma, subtração, multiplicação e divisão.

# area = base . altura

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))



print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)
print(n1//n2)
print(n1**n2)
print(n1%n2)






base = int(input('Base do retângulo: '))
altura = int(input('Altura do retângulo: '))

area = base*altura
print('Área do retângulo = {}'.format(area))