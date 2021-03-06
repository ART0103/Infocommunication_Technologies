# На вход программе подаются 3 коэффициента квадратного
# уравнения. Программа должна находить корни квадратного уравнения.

import math

tmp = input('Введите коэффициенты квадратного уравнения через пробел: ').split()
k = [int(x) for x in tmp]
D = (k[1]) ** 2 - 4*k[0]*k[2]
if D > 0:
    tmp = round(math.sqrt(D))
    x1 = round((-k[1] + tmp)/(2*k[0]))
    x2 = round((-k[1] - tmp)/(2*k[0]))
    print(f'Полученные корни:\nx1:{x1}\nx2:{x2}')
elif D == 0:
    x1 = round((-k[1])/(2*k[0]))
    print(f'Полученный корень:\nx:{x1}')
else:
    print('Дискриминант меньше 0, корней нет.')
