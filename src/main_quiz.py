#This is the main file that the interactive quiz will run off of.

#libraries
import pygame, random, sys, time

#other file imports
from question_choosing.question_bank import question_list
from question_choosing.randquestion import random_question_chooser

#initialisation
pygame.init()

#globals
running = True
display_x = 800
display_y = 800
background_colour = (255,255,255) #default white background colour (put as variable so that it can be changed in settings)

#window setup
pygame.display.set_caption("OCR computer science quiz!")
window = pygame.display.set_mode((display_x,display_y))
window.fill(background_colour)

#program loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()