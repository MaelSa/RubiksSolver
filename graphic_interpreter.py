from time import *
import pygame
from ressources import *
from pygame.locals import *

def graphic_inter(arretes,coins,centres, arrete_graph, milieu_graph, coin_graph,wait):
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    orange = (255, 128, 0)
    list_color = [red, orange, white, yellow, green, blue]
    pygame.init()
    fenetre = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Rubik's cube")
    fenetre.fill((0,0,0))

    #arretes:
    for i in range(0,12):
        for j in range(0,2):
            c = arretes[i][j]
            colour = list_color[c-1]
            pygame.draw.rect(fenetre,colour, arrete_graph[i][j])

    for i in range(0,6):
        c = centres[i]
        colour = list_color[c-1]
        pygame.draw.rect(fenetre,colour, milieu_graph[i])

    for i in range(0,8):
        for j in range(0,3):
            c = coins[i][j]
            colour = list_color[c-1]
            pygame.draw.rect(fenetre, colour, coin_graph[i][j])
    pygame.display.update()
    continuer = 1
    sleep(5)
    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = 0
            elif wait == True:

                continuer = 0


    pygame.quit()
    #quit()

