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
    for y in range(HEIGHT):
        for x in range(WIDTH):
            field[y][x] = randint(0, 1)
    return field


# new field with 'airforce' pattern
def airforce(field, dx=0, dy=0):
    sx = WIDTH // 2 + dx
    sy = HEIGHT // 2 + dy
    field[sy - 1][sx - 1] = 1
    field[sy][sx - 1] = 1
    field[sy - 1][sx] = 1
    field[sy + 2][sx + 1] = 1
    field[sy + 1][sx + 1] = 1
    field[sy + 2][sx] = 1
    return field


# new field with simple glider
def glider(field, dx=0, dy=0):
    sx = WIDTH // 2 + dx
    sy = HEIGHT // 2 + dy
    field[sy + 1][sx + 0] = 1
    field[sy + 2][sx + 0] = 1
    field[sy + 0][sx + 1] = 1
    field[sy + 1][sx + 1] = 1
    field[sy + 2][sx + 2] = 1
    return field


# new field with "snowflake" pattern
def snowflake(field, dx=0, dy=0):
    sx = WIDTH // 2 + dx
    sy = HEIGHT // 2 + dy
    field[sy][sx] = 1
    field[sy + 1][sx] = 1
    field[sy + 2][sx] = 1

    field[sy + 1][sx - 1] = 1
    field[sy + 1][sx - 2] = 1
    field[sy + 1][sx - 3] = 1
    field[sy][sx - 3] = 1
    field[sy - 1][sx - 3] = 1
    field[sy - 2][sx - 3] = 1
    field[sy - 2][sx - 2] = 1
    field[sy - 2][sx - 4] = 1

    field[sy + 1][sx + 1] = 1
    field[sy + 1][sx + 2] = 1
    field[sy + 1][sx + 3] = 1
    field[sy][sx + 3] = 1
    field[sy - 1][sx + 3] = 1
    field[sy - 2][sx + 3] = 1
    field[sy - 2][sx + 2] = 1
    field[sy - 2][sx + 4] = 1
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
    for j in range(HEIGHT):
        for i in range(WIDTH):
            nei_num = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if 0 <= y < HEIGHT and 0 <= x < WIDTH and field[y][x] == 1:
                        nei_num += 1
            nei_num -= field[j][i]
            n_field[j][i] = color(nei_num, field[j][i])
    return n_field
