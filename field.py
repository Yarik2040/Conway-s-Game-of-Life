# В этом файле описаны функции для изменения поля и правила
# игрового мира.

SCREEN_SIZE = (1280, 720)
CELL_SIZE = (10, 10)
WIDTH = SCREEN_SIZE[0] / CELL_SIZE[0]
HEIGHT = SCREEN_SIZE[1] / CELL_SIZE[1]


# создаёт новое пустое поле
def new_field():
    return [[0] * WIDTH for i in range(HEIGHT)]


# описывает правила раскраски пикселей
def color(nei_num):
    if nei_num <= 2 or nei_num >= 7:
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
                    if 0 <= x < HEIGHT and 0 <= y < WIDTH:
                        nei_num += 1
            n_field[i][j] = color(nei_num)
    return n_field
