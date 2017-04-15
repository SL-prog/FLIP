import pygame
from pygame.locals import *
pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("FLIP")

class Case:
    def __init__(self, IMAGE, posx, posy):#, numero):
        self.img = pygame.image.load(IMAGE)
        self.posx = posx
        self.posy = posy
        self.clicked = False
        self.moovex = 0
        self.moovey = 0
        #self.numero = numero

    def clic(self, mousex, mousey):
        emptyx = case[0].posx
        emptyy = case[0].posy

        if (self.posx <= mousex <= self.posx + 125):
            if (self.posy <= mousey <= self.posy + 125):
                self.clicked = True
        else:
            self.clicked = False

        if self.clicked:
            if ((self.posx - 125) == emptyx) and (self.posy == emptyy):
                    self.moovex = -125
            elif ((self.posy - 125) == emptyy) and (self.posx == emptyx):
                    self.moovey = -125
            elif ((self.posx + 125) == emptyx) and (self.posy == emptyy):
                    self.moovex = 125
            elif ((self.posy + 125) == emptyy) and (self.posx == emptyx):
                    self.moovey = 125

        if self.moovex != 0:
            self.MooveX()

        if self.moovey != 0:
            self.MooveY()

    def MooveX(self):
        self.posx = case[0].posx
        case[0].posx-=self.moovex
        self.moovex = 0

    def MooveY(self):
        self.posy = case[0].posy
        case[0].posy-=self.moovey
        self.moovey = 0

    def blit(self, window):
        window.blit(self.img, (self.posx, self.posy))

case = [0]*16
i = 0
for y in range(0, 4):
    for x in range(0, 4):
        case[i] = Case(str(i)+".png", x*125, y*125) #, i)
        i+=1

loop = True
while loop:

    for event in pygame.event.get():
        if event.type == QUIT:
            loop = False
        if event.type == MOUSEBUTTONDOWN and event.button == 1 :
            i = 0
            for y in range(0, 4):
                for x in range(0, 4):
                    if i!=0:
                        case[i].clic(event.pos[0], event.pos[1])
                    if case[i].clicked:
                        case[i].clicked = False
                    i+=1
    i = 0
    for y in range(0, 4):
        for x in range(0, 4):
            case[i].blit(window)
            i+=1


    pygame.display.flip()
pygame.quit()