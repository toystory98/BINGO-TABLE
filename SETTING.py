import pygame, sys
from pygame.locals import * 

#set color
white = (255,255,255)
red = (166,0,12)
red_dark = (125,2,11)
black = (0,0,0)
black_med = (17,17,19)
black_light = (58,58,58)

color_set1 = ['start',red_dark,red,red_dark,red]
color_set2 = ['start',red,red_dark,red,red_dark]

pygame.init()   #initialize all imported pygame modules
pygame.display.set_caption('4x7 BINGO TABLE') # set window caption
screen = pygame.display.set_mode((420,700)) # set window size
screen.fill(white) # set window background color
font = pygame.font.SysFont('Arial', 40) # set font