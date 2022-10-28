import pygame as pg
import sys



pg.init()
clock = pg.time.Clock()
FPS = 10
WINDOW_size = (1200,800)
screen = pg.display.set_mode((1200, 800))
pg.display.set_caption("GAYS")
bg_color = (0, 0, 0)

n2_spisok = ()  # конечный список ходов компьютера
ur = 3  # количество предсказываемых компьютером ходов
k_rez = 0  # !!!
o_rez = 0
poz1_x = -1  # клетка не задана
f_hi = True  # определение хода игрока(да)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    clock.tick(FPS)

    # while True:
    #     for event in pg.event.get():
    #         if event.type==pg.QUIT:
    #             pg.quit()


# screen.fill(bg_color)
# pg.display.flip()


