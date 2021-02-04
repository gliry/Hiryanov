import pygame
from pygame.draw import *


def drawing_fence(width_fence, height_fence, x_fence, y_fence, number_board):
    """
    This fucntions draws fence from (x_fence, y_fence) of width = width_fence and height = height_fence
    :param width_fence: full width of fence
    :param height_fence:full height of fence
    :param x_fence: x coordinate of top left angle
    :param y_fence: y coordinate of top left angle
    :param number_board: number of boards in fence
    :return: None
    """
    polygon(screen, (255, 204, 0),
            [(x_fence, y_fence), (x_fence + width_fence, y_fence), (x_fence + width_fence, y_fence + height_fence),
             (x_fence, y_fence + height_fence)])

    for i in range(number_board):
        line(screen, (0, 0, 0), (x_fence + width_fence * i / number_board, y_fence),
             (x_fence + width_fence * i / number_board, y_fence + height_fence), 2)


def drawing_dog():
    pass


def drawing_booth(width_booth, height_booth, x_booth, y_booth):
    """
    This function draw booth, that have roofs peak in (x_booth, y_booth),
    :param width_booth:
    :param height_booth:
    :param x_booth:
    :param y_booth:
    :return:
    """
    polygon(screen, (255, 255, 0), [(x_booth, y_booth),
                                    (x_booth + width_booth / 2, y_booth + height_booth / 1.5),
                                    (x_booth - width_booth / 2, y_booth + height_booth / 2)])  # Rectangle part of booth

    polygon(screen, (255, 255, 0), [(x_booth, y_booth),
                                    (x_booth + width_booth / 2, y_booth - height_booth / 7),
                                    (x_booth + width_booth, y_booth + height_booth / 2),
                                    (x_booth + width_booth / 2,
                                     y_booth + height_booth / 1.5)])  # Polygon part of booth's roof

    polygon(screen, (255, 204, 0), [(x_booth - width_booth / 2, y_booth + height_booth / 2),
                                    (x_booth + width_booth / 2, y_booth + height_booth / 1.5),
                                    (x_booth + width_booth / 2, y_booth + height_booth * 1.35),
                                    (x_booth - width_booth / 2,
                                     y_booth + height_booth * 1.1)])  # Front wall part of booth

    polygon(screen, (255, 204, 0), [(x_booth + width_booth / 2, y_booth + height_booth / 1.5),
                                    (x_booth + width_booth, y_booth + height_booth / 2),
                                    (x_booth + width_booth, y_booth + height_booth * 1.12),
                                    (x_booth + width_booth / 2,
                                     y_booth + height_booth * 1.35)])  # Back wall part of booth

    polygon(screen, (0, 0, 0), [(x_booth, y_booth),
                                (x_booth + width_booth / 2, y_booth + height_booth / 1.5),
                                (x_booth - width_booth / 2, y_booth + height_booth / 2)],
            2)  # Rectangle perimeter part of booth

    polygon(screen, (0, 0, 0), [(x_booth, y_booth),
                                (x_booth + width_booth / 2, y_booth - height_booth / 7),
                                (x_booth + width_booth, y_booth + height_booth / 2),
                                (x_booth + width_booth / 2, y_booth + height_booth / 1.5)],
            2)  # Polygon perimeter part of booth's roof

    polygon(screen, (0, 0, 0), [(x_booth - width_booth / 2, y_booth + height_booth / 2),
                                (x_booth + width_booth / 2, y_booth + height_booth / 1.5),
                                (x_booth + width_booth / 2, y_booth + height_booth * 1.35),
                                (x_booth - width_booth / 2, y_booth + height_booth * 1.1)],
            2)  # Front perimeter wall part of booth

    polygon(screen, (0, 0, 0), [(x_booth + width_booth / 2, y_booth + height_booth / 1.5),
                                (x_booth + width_booth, y_booth + height_booth / 2),
                                (x_booth + width_booth, y_booth + height_booth * 1.12),
                                (x_booth + width_booth / 2,
                                 y_booth + height_booth * 1.35)], 2)  # Back wall perimeter part of booth

    circle(screen, (0, 0, 0), (x_booth, y_booth + height_booth * 0.9), width_booth / 3.5)


def drawing_background(width_background, height_background):
    """
    This function draw background in polygon from (0,0) to (width_background, height_background)

    :param width_background: Must be equal to screen width
    :param height_background: Must be equal to screen height
    :return: None
    """
    polygon(screen, (0, 191, 200),
            [(0, 0), (width_background, 0), (width_background, height_background * 0.6), (0, height_background * 0.6)])
    polygon(screen, (0, 255, 127), [(0, height_background * 0.6), (width_background, height_background * 0.6),
                                    (width_background, height_background), (0, height_background)])


def drawing_picture():
    drawing_background(width, height)
    drawing_fence(width, height / 2, 0, 100, 10)
    drawing_booth(width / 5, height / 4, 340, 350)
    drawing_dog()


pygame.init()
FPS = 30
width = 500
height = 700
screen = pygame.display.set_mode((width, height))  # screen size
pygame.display.update()
clock = pygame.time.Clock()
finished = False

drawing_picture()
pygame.display.update()

while not finished:

    clock.tick(FPS)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
