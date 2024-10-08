import pygame
import sys

def terminate():
    pygame.quit()
    sys.exit()

pygame.init()

black = (0,0,0)
white = (0,0,0)

clock = pygame.time.Clock()
fps=30

screen_height = 520
screen_width = 650
screen = pygame.display.set_mode(screen_width,screen_height)

class Rect(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,color,value):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.value = value
    def change_value(self,color,value):
        self.image.fill(color)
        self.value=value
        rects = pygame.sprite.Group()

rect = Rect(50,50,100,100,black)
rect.add(rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

    screen.fill(white)
    rect.draw(screen)

    pygame.display.flip()

    clock.tick(fps)