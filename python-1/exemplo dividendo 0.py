import sys

a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))


if b==0:
    print('Não é possível dividir um número por 0! Tente novamente.')
    sys.exit()


resultado = a/b

print("O resultado de {} dividido por {}, é equivalente à: {}".format(a,b,resultado))
