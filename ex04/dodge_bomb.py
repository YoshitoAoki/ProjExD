import pygame as pg
import sys
from random import *


def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろこうかとん！")
    scrn_sfc = pg.display.set_mode((1400,700))
    scrn_rct = scrn_sfc.get_rect()

    pgbg_sfc = pg.image.load("ex04/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900,400
    scrn_sfc.blit(tori_sfc,tori_rct)

    bomb_sfc = pg.Surface((20,20))#正方形の空(透明）のSurface
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc,(255,0,0),(10,10),10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0,scrn_rct.width)
    bomb_rct.centery = randint(0,scrn_rct.height)

    while True:
        scrn_sfc.blit(pgbg_sfc,pgbg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        key_dct = pg.key.get_pressed()
        if key_dct[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -=1
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 1
        
        scrn_sfc.blit(tori_sfc,tori_rct)
        
        vx,vy = +1,+1
        bomb_rct.move_ip(vx,vy)
        scrn_sfc.blit(bomb_sfc,bomb_rct)
        
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()