import pygame as pg
import sys

def main():
    clock = pg.time.Clock()
    scrn_sfc = pg.display.set_mode((1400,700))
    pgbg_sfc = pg.image.load("ex04/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()
    
    while True:
        scrn_sfc.blit(pgbg_sfc,pgbg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()