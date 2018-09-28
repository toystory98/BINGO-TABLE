import random 
import pygame, sys
from pygame.locals import * 
from SETTING import *

def square(val): # draw square table
    #create number list 1-28
    number = [] 
    number2 = []
    for i in range(1,29):
        number.append(i)
        number2.append(i)

    if val == 'normal':  #for sort number table
        for i in range(1,29):
            if i <= 4 :
                x = 70*i
                y = 70    
                pygame.draw.rect(screen,color_set1[i], (x, y, 70, 70))   # draw square
                screen.blit(font.render(str(number[i-1]),True,white), ((x+23,y+23)))  # set font in square
            elif i <= 8:
                x = 70*(i-4)
                y = 140   
                pygame.draw.rect(screen,color_set2[i-4], (x, y, 70, 70))  
                screen.blit(font.render(str(number[i-1]),True,white), ((x+23,y+23)))
            elif i <= 12:
                x = 70*(i-8)
                y = 210 
                pygame.draw.rect(screen,color_set1[i-8], (x, y, 70, 70))  
                screen.blit(font.render(str(number[i-1]),True,white), ((x+23,y+23)))
            elif i <= 16:
                x = 70*(i-12)
                y = 280 
                pygame.draw.rect(screen,color_set2[i-12], (x, y, 70, 70))  
                screen.blit(font.render(str(number[i-1]),True,white), ((x+23,y+23)))
            elif i <= 20:
                x = 70*(i-16)
                y = 350 
                pygame.draw.rect(screen,color_set1[i-16], (x, y, 70, 70))  
                screen.blit(font.render(str(number[i-1]),True,white), ((x+23,y+23)))
            elif i <= 24:
                x = 70*(i-20)
                y = 420 
                pygame.draw.rect(screen,color_set2[i-20], (x, y, 70, 70))  
                screen.blit(font.render(str(number[i-1]),True,white), ((x+23,y+23)))
            elif i <= 28:
                x = 70*(i-24)
                y = 490 
                pygame.draw.rect(screen,color_set1[i-24], (x, y, 70, 70))  
                screen.blit(font.render(str(number[i-1]),True,white), ((x+23,y+23)))

    elif val == 'random':  #for random number table
        random.shuffle(number2)  #shuffle number in list number2
        for i in range(1,29):
            if i <= 4 :
                x = 70*i
                y = 70    
                pygame.draw.rect(screen,color_set1[i], (x, y, 70, 70))  
                screen.blit(font.render(str(number2[i-1]),True,white), ((x+23,y+23)))
            elif i <= 8:
                x = 70*(i-4)
                y = 140   
                pygame.draw.rect(screen,color_set2[i-4], (x, y, 70, 70))  
                screen.blit(font.render(str(number2[i-1]),True,white), ((x+23,y+23)))
            elif i <= 12:
                x = 70*(i-8)
                y = 210 
                pygame.draw.rect(screen,color_set1[i-8], (x, y, 70, 70))  
                screen.blit(font.render(str(number2[i-1]),True,white), ((x+23,y+23)))
            elif i <= 16:
                x = 70*(i-12)
                y = 280 
                pygame.draw.rect(screen,color_set2[i-12], (x, y, 70, 70))  
                screen.blit(font.render(str(number2[i-1]),True,white), ((x+23,y+23)))
            elif i <= 20:
                x = 70*(i-16)
                y = 350 
                pygame.draw.rect(screen,color_set1[i-16], (x, y, 70, 70))  
                screen.blit(font.render(str(number2[i-1]),True,white), ((x+23,y+23)))
            elif i <= 24:
                x = 70*(i-20)
                y = 420 
                pygame.draw.rect(screen,color_set2[i-20], (x, y, 70, 70))  
                screen.blit(font.render(str(number2[i-1]),True,white), ((x+23,y+23)))
            elif i <= 28:
                x = 70*(i-24)
                y = 490 
                pygame.draw.rect(screen,color_set1[i-24], (x, y, 70, 70))  
                screen.blit(font.render(str(number2[i-1]),True,white), ((x+23,y+23)))
    elif val == 'bt_random':  # create random button
        x = 100
        y = 595
        pygame.draw.rect(screen,black, (x, y, 200, 70))  
        screen.blit(font.render('RANDOM',True,white), ((x+35,y+23)))  

    elif val == 'start':  # create start button 
        x = 100
        y = 5
        pygame.draw.rect(screen,black, (x, y, 200, 50))  
        screen.blit(font.render('START',True,white), ((x+53,y+12)))  