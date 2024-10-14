import pygame
import sys
import random
import re
import time

from pygame.locals import *

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
GREY = (200,200,200)
YELLOW = (255,255,0)

pygame.init()
pygame.display.set_caption("CodeForce Hangman")

#32 bit display
Display = pygame.display.set_mode((500,500),0,32)
Display.fill(WHITE)

# hardness = 1
EASY = ["MOLE", "BOWL", "HOLE", "ROLL", "POLE", "TOLL", "SOUL"]
# hardness = 2
MEDIUM = ["SUPER", "MEGATRON", "OPTIMUS", "BUMBLEBEE", "RATCHET"]
# hardness = 3
HARD = ["STARSCREAM", "PATRIOTIC", "MATRIARCHY"]
# hardness = 4
IMPOSSIBLE = ["SUPERCALIFRAGILISTICEXPIALIDOCIOUS", "MICROPACHYCEPHALOSAURUS"]

def chooseRandomWord(hardness):
    RandomNumber = 0
    if hardness == 1:
        RandomNumber = random.randint(0, len(EASY)-1)
    elif hardness == 2:
        RandomNumber = random.randint(0, len(EASY)-1)
    else:
        RandomNumber = random.randint(0, len(HARD)-1)
    return RandomNumber

def getWord(number, hardness):
    word = ""
    if hardness == 1:
        word = EASY[number]
    elif hardness == 2:
        word = MEDIUM[number]
   
    elif hardness == 4:
        word = IMPOSSIBLE[number]
    else:
        work = HARD[number]    
    return word

def PreHangman():
    pygame.draw.line(Display,BLUE,(10,400),(300,400),8) #baseline
    pygame.draw.line(Display,BLUE,(50,50),(50,400),8) #stick 1
    pygame.draw.line(Display,BLUE,(50,60),(250,60),8) #stick 2
    pygame.draw.line(Display,BLUE,(150,60),(150,100),8) #rope
    pygame.draw.circle(Display,BLUE,(150,150),50,8) #head
    pygame.draw.line(Display,BLUE,(150,200),(150,300),8) #body
    pygame.draw.line(Display,BLUE,(150,210),(100,250),8) #left hand
    pygame.draw.line(Display,BLUE,(150,210),(200,250),8) #right hand
    pygame.draw.line(Display,BLUE,(150,300),(100,350),8) #left leg
    pygame.draw.line(Display,BLUE,(150,300),(200,350),8) #right leg

FONT2 = pygame.font.Font("freesansbold.ttf", 20)

def StartScreen():
    Display.blit(pygame.font.Font("freesansbold.ttf",40).render("CodeForce Hangman",True, BLACK), (20,20))
    Display.blit(FONT2.render("By Matt Livingston", True, BLACK), (60,60))

def hangman(condition):
    # Game Over
    if (condition == 0):
        pass
    # Draw the base
    elif condition == 1:
        pygame.draw.line(Display,BLUE,(10,400),(300,400,)8)
    # Stick One
    elif condition == 2:
        pygame.draw.line(Display,BLUE,(50,50),(50,400),8)
    # Stick Two
    elif condition == 3:
        pygame.draw.line(Display,BLUE,(50,60),(250,60),8)
    # Rope
    elif condition == 4:
        pygame.draw.line(Display,BLUE,(150,60),(150,100),8)
    # Head
    elif condition == 5:
        pygame.draw.circle(Display,BLUE,(150,150),50,8)
    # Body
    elif condition == 6:
        pygame.draw.line(Display,BLUE,(150,200),(150,300),8)
    # Left hand
    elif condition == 7:
        pygame.draw.line(Display,BLUE,(150,210),(100,250),8)
    # Right hand
    elif condition == 8:
        pygame.draw.line(Display,BLUE,(150,210),(200,250),8)
    # Left leg
    elif condition == 9:
        pygame.draw.line(Display,BLUE,(150,300),(100,350),8)
    # Right leg
    elif condition == 10:
        pygame.draw.line(Display,BLUE,(150,300),(200,350),8)

def main():
    #StartScreen()
    #PreHangman()
    run = True
    while run:
        #print("Welcome to Hangman")
        hardness = 1
        word = getWord(chooseRandomWord(hardness), hardness)
        #print(word)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        Display.fill(WHITE)


        Word = FONT2.render("The word is: ", True, BLACK)
        WordRect = Word.get_rect()
        WordRect.center = (250,250)
        Display.blit(Word,WordRect)
        

        TheWord = FONT2.render(word, True, BLACK)
        Word2Rect = TheWord.get_rect()
        Word2Rect.center = (250,285)
        Display.blit(TheWord,Word2Rect)
        pygame.display.flip()

main()
