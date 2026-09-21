# 1. Dado um número, verificadar se ele é positivo, negativo ou nulo.
import os
os.system('cls')

n = int(input('Numero: '))

if n < 0:
    print('Negativo')
elif n > 0:
    print('Positivo')
else:
    print('Nulo')
    