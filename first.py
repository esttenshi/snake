import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

width = 600
height = 400

game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Игра "Змейка"')

block_size = 20
snake_speed = 5

font_style = pygame.font.SysFont("arial", 25)
score_font = pygame.font.SysFont("arial", 35)

def display_score(score):
    value = score_font.render("Ваш результат: " + str(score), True, white)
    game_window.blit(value, [0, 0])

def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [width / 6, height / 3])

def game_loop():
    game_over = False
    game_close = False

    food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, height - block_size) / block_size) * block_size

    while not game_over:

        while game_close:
            game_window.fill(black)
            display_message("Вы проиграли! Нажмите Q для выхода или C для возобновления игры", red)
            pygame.display.update()

        game_window.fill(black)
        pygame.draw.rect(game_window, red, [food_x, food_y, block_size, block_size])
 
        pygame.display.update()

    pygame.quit()
    quit()

game_loop()