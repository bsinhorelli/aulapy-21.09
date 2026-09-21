# 2. Dada uma nota, verificar se ela é válida (entre 0 a 10) ou inválida
# Entrada: 8.5      Saída: Nota Válida
# Entrada: 45      Saída: Nota Inválida
import os
os.system('cls')

nota = float(input('Digite uma nota: '))

if nota >= 0 and nota <= 10:
    print('Nota Válida')

else:
    print('Nota Inválida')

# Forma complemento (oposto)
nota2 = float(input('Digite uma nota: '))

if nota < 0 or nota2 > 10:
    print('Nota Inválida')

else:
    print('Nota Válida')
