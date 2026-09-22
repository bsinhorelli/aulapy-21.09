# 3. Dadas duas nota, verificar se elas são válidas. Se sim, calcular a média.
# Caso uma das notas não seja válida, encerrar o programa.

n1 = float(input('Nota 1: '))
if n1 >= 0 and n1 <= 10:
    n2 = float(input('Nota 2: '))
    if n2 >= 0 and n2 <= 10:
        media = (n1+n2) / 2
        if media > 7:
            media += 1
        print(f'Média das duas notas: {media}')
    else:
        print('nota 2 inválida')


else:
    print('nota 1 inválida')

