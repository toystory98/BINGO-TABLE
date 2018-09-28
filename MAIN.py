
import random
import pygame, sys
from pygame.locals import * 
from SET_SQUARE import *   # import code from SET_SQUARE file
from SETTING import *  # import code from SETTING file

def is_click(self):  # mouse click function
    return pygame.mouse.get_pressed()[0] and self.collidepoint(pygame.mouse.get_pos())  

def main(): # main function
    start = True

    while start: # pygame main loop
        
        pygame.display.update() # update display
        square('bt_random')
        square('start')

        for event in pygame.event.get():  #	events from the queue
            
            if event.type == pygame.MOUSEMOTION: # set mouse
                rectpos = event.pos 
            if event.type == pygame.MOUSEBUTTONDOWN : # if use click mouse 
                if is_click(pygame.draw.rect(screen,black_light, (100, 595, 200, 70))) : #if click button on window 
                    square('random')  # show random number table
                elif is_click(pygame.draw.rect(screen,black_light, (100, 5, 200, 50))) :
                    square('normal')  # show sort number table

        
        if event.type == QUIT :  # close pygame if close window 
            start = False
        
        

main() # call main function

pygame.quit() # quit pygame
quit()


