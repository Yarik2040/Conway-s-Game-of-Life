# В этом файле описаны функции для изменения поля и правила
# игрового мира.

from random import randint

SCREEN_SIZE = (1280, 720)
CELL_SIZE = (10, 10)
WIDTH = SCREEN_SIZE[0] // CELL_SIZE[0]
HEIGHT = SCREEN_SIZE[1] // CELL_SIZE[1]


# создаёт новое пустое поле
def new_field():
    return [[0] * WIDTH for i in range(HEIGHT)]


# создаёт случайное поле
def random_field():
    field = new_field()
    for x in range(HEIGHT):
        for y in range(WIDTH):
            field[x][y] = randint(0, 1)
    return field

# new field with 'airforce' pattern
def airforce(dx=0, dy=0):
    field = new_field()
    sx = HEIGHT // 2 + dx
    sy = WIDTH // 2 + dy
    field[sx - 1][sy - 1] = 1
    field[sx - 1][sy] = 1
    field[sx][sy - 1] = 1
    field[sx + 1][sy + 2] = 1
    field[sx + 1][sy + 1] = 1
    field[sx][sy + 2] = 1
    return field


# new field with simple glider
def glider(dx=0, dy=0):
    field = new_field()
    sx = HEIGHT // 2 + dx
    sy = WIDTH // 2 + dy
    field[sx + 0][sy + 1] = 1
    field[sx + 0][sy + 2] = 1
    field[sx + 1][sy + 0] = 1
    field[sx + 1][sy + 1] = 1
    field[sx + 2][sy + 2] = 1


    return field


# описывает правила раскраски пикселей
def color(nei_num, cur_color):
    if cur_color == 1:
        if nei_num == 2 or nei_num == 3:
            return 1
        return 0
    else:
        if nei_num == 3:
            return 1
        return 0


# строит следующую итерацию поля по текущей
def get_new_iteration(field):
    n_field = new_field()
    for i in range(HEIGHT):
        for j in range(WIDTH):
            nei_num = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if 0 <= x < HEIGHT and 0 <= y < WIDTH and field[x][y] == 1:
                        nei_num += 1
            nei_num -= field[i][j]
            n_field[i][j] = color(nei_num, field[i][j])
    return n_field
