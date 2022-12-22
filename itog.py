import copy
import sys


step = 0

sys.setrecursionlimit(10000)

def draw(a):
    for i in range(5):
        print(a[i])
    print('-----------------')


def write_steps(order):
    global step
    f = open(f'POBEDA{step}.txt', 'w')
    f.write(str(len(order)) + '\n')
    for i in order:
        for j in i:
            f.write(str(j) + '\n')
        f.write('___' + '\n')
    step += 1
    f.close()


# a = [[0 for j in range(4)] for i in range(5)]
#
# for i in range(4):
#     a[0][i] = 1
#     a[4][i] = 2

a = [[2, 2, 2, 2],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [1, 1, 1, 1]]

ideal = [[1, 1, 1, 1],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [2, 2, 2, 2]]

"""Функцяи самых ходов слона, разращает массивы для ходов слона, чтобы использовать их в дальнейшем"""



def bishopW(a, c, CanSteps, order):
    lots_of_moves = []
    for x in range(5):
        for y in range(4):
            if a[x][y] == c:
                for i in range(5):
                    for j in range(4):
                        if CanSteps[i][j] == 0:
                            if abs(i - x) == abs(j - y):
                                b = copy.deepcopy(a)
                                b[x][y] = 0
                                b[i][j] = c
                                if b == ideal:
                                    print('Решение найдено')
                                    draw(b)
                                    print('-----------------')
                                    write_steps(order)
                                    b.clear()
                                elif b != a:
                                    lots_of_moves.append(b)
                                else:
                                    b.clear()

    return lots_of_moves


def bishopB(a, c, CanSteps, order):
    lots_of_moves = []
    for x in range(5):
        for y in range(4):
            if a[x][y] == c:
                for i in range(5):
                    for j in range(4):
                        if CanSteps[4 - i][3 - j] == 0:
                            if abs(4 - i - x) == abs(3 - j - y):
                                b = copy.deepcopy(a)
                                b[x][y] = 0
                                b[4 - i][3 - j] = c
                                if b == ideal:
                                    print('Решение найдено')
                                    draw(b)
                                    print('-----------------')
                                    write_steps(order)
                                    b.clear()
                                elif b != a:
                                    lots_of_moves.append(b)
                                else:
                                    b.clear()

    return lots_of_moves


"""Рабочая функция принимает массив и цвет фигуры, а возращает массив заполненный и только по 0 можно ходить"""


def variant(a, c):
    mat_vat = copy.deepcopy(a)
    for x in range(5):
        for y in range(4):
            if a[x][y] == c:
                for i in range(5):
                    for j in range(4):
                        if abs(i - x) == abs(j - y):
                            mat_vat[i][j] = c
    return mat_vat


# CanSteps = variant(a, 1)
# bishop(a, 2, CanSteps)
def recurs(a, c, order):
    order_local = copy.deepcopy(order)
    order_local.append(a)
    if len(order_local) < 40:
        c = c % 3
        if c == 0:
            c = 1
        if c == 1:
            t = 2
        else:
            t = 1
        cant_step = variant(a, c)
        if t == 1:
            mat_voz = bishopW(a, t, cant_step, order_local)
        else:
            mat_voz = bishopB(a, t, cant_step, order_local)
        for i in mat_voz:
            if i not in order_local:
                recurs(i, c + 1, order_local)
    else:
        order_local.clear()


recurs(a, 1, [])
