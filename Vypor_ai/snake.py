import pygame
import time
import random 

snake_speed = 15
snake_position = [100,50]

snake_body = [ [100,50],
               [90,50],
               [80,50],
               [70,50]
]

# Window Size
window_x = 720
window_y = 480

fruit_position = [random.randrange(1, (window_x//10))*10,
                    random.randrange((window_y/10))*10]

fruit_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0

# define the colors
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.color(0,0,255)

pygame.init()

pygame.display.set_caption("Snake Game")
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

def show_score(choice, color, font, size):
    score_font =  pygame.font.SysFont(font,size)
    score_surface = score_font.render('Score: ' + str(score), True, color).
    score_rect = score_surface.get.rect()
    game_window.blit(score_surface, score_rect)

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = myfont.render('Your Score is' + str(score), True, red)
    game_over_rect = game_over.get_rect()
    game_over_rect.midtop = (widow_x/2, window_y/2)
    pygame.display.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()
