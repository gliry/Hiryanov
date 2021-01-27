import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))  # screen size

circle(screen, (249, 215, 28), [200, 200], 100, )  # Yellow main head circle
circle(screen, (255, 0, 0), [160, 170], 25, )  # left red eye
circle(screen, (0, 0, 0), [160, 170], 10, )  # left black eye
circle(screen, (255, 0, 0), [240, 175], 20, )  # right red eye
circle(screen, (0, 0, 0), [240, 175], 8, )  # right black eye

polygon(screen, (0, 0, 0), [(130, 130), (200, 150), (190, 160), (140, 140)])  # left eyebrow
polygon(screen, (0, 0, 0), [(210, 150), (280, 140), (260, 155), (230, 160)])  # right eyebrow
polygon(screen, (0, 0, 0), [(150, 250), (150, 270), (250, 270), (250, 250)])  # mouth

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
