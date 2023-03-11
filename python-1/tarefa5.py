# 5. Faça um programa que calcule o volume de um cone qualquer, lembrar de utilizar a biblioteca math para usar ovalor de pi.

# Volume = areadabase . altura 

pi = float(3.14)
raio = float(input('Raio: '))
alt = float(input('Altura: '))

raio2 = raio**raio

volume1 = (pi*raio2)
volume2 = (volume1*alt)/3

print('Volume: ', volume2)