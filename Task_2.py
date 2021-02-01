import pygame
from pygame.draw import *


def drawing_fence():
    pass


def drawing_dog():
    pass


def drawing_booth():
    pass

def drawing_background():
    pass




def drawing_picture():
    drawing_background()
    drawing_fence()
    drawing_booth()
    drawing_dog()





FPS = 30
screen = pygame.display.set_mode((500, 700))  # screen size
clock = pygame.time.Clock()
finished = False

while not finished:
    drawing_picture()
    clock.tick(FPS)
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    pygame.quit()

pygame.init()
