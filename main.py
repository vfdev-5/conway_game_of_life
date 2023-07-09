import random
import pygame as pg

from game_of_life import GameOfLife
from game_of_life import (
    create_blinker,
    create_beacon,
    create_block,
    create_toad,
    create_penta_decathlon,
    create_r_pentomino,
    create_gospel_glider_gun,
)


white = 255, 240, 200
black = 20, 20, 40
true_black = 0, 0, 0


class GameOfLifeRenderer(GameOfLife):

    cell_color = white
    cell_size = 10

    def draw(self, screen):
        screen.fill(black)
        for cell in self.live_cells:
            x, y = cell
            rect = [
                self.cell_size * x,
                self.cell_size * y,
                self.cell_size,
                self.cell_size,
            ]
            pg.draw.rect(screen, self.cell_color, rect)


def main():
    pg.init()

    screen = pg.display.set_mode((600, 600))
    pg.display.set_caption("Conway's Game of Life")
    clock = pg.time.Clock()

    screen_width, screen_height = pg.display.get_window_size()
    print("Screen size:", screen_width, screen_height)

    screen.fill(black)

    # init_state = create_block(1, 1) | create_beacon(10, 10) | create_blinker(5, 5) | create_toad(12, 3)
    # init_state |= create_blinker(25, 25) | create_blinker(25 + 1, 25 + 1)
    # init_state |= create_block(40, 10, 5)

    # init_state = create_block(3, 3, 3) | create_block(10, 10, 4) | create_block(20, 20, 5) | create_block(30, 30, 6)

    # init_state = create_block(10, 10, 10) | create_block(15, 15, 10)

    # init_state = create_block(15, 5, 10) | create_block(15, 25, 10)
    # init_state |= create_block(5, 15, 10) | create_block(25, 15, 10)

    # init_state = create_penta_decathlon(10, 10)

    # init_state = create_r_pentomino(30, 30)

    init_state = create_gospel_glider_gun(10, 30)

    # random.seed(0)
    # x = y = 10
    # n = 10
    # s = 15
    # init_state = {
    #     (x + random.randint(0, s), y + random.randint(0, s)) for _ in range(n)
    # }

    # random.seed(0)
    # x = y = 10
    # n = 15
    # s = 5
    # init_state = {
    #     (int(random.normalvariate(x, s)), int(random.normalvariate(y, s))) for _ in range(n)
    # }

    game = GameOfLifeRenderer(init_state=init_state)

    done = False
    acc = 0.0
    while not done:

        screen.fill(black)

        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYUP and e.key == pg.K_ESCAPE):
                done = True
                break

        game.draw(screen)

        game.next()

        pg.display.update()
        clock.tick(1.0 + acc)
        acc = min(5.0, acc + 0.1)

        # print(len(game.live_cells), end="  ")

    pg.quit()


if __name__ == "__main__":
    main()
