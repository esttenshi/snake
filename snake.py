import pygame
import time
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

clock = pygame.time.Clock()

block_size = 20
snake_speed = 5

font_style = pygame.font.SysFont("arial", 20)
score_font = pygame.font.SysFont("arial", 35)

def display_score(score):
    value = score_font.render("Ваш результат: " + str(score), True, white)
    game_window.blit(value, [0, 0])

def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(game_window, green, [block[0], block[1], block_size, block_size])

def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [5, 100])

def game_loop():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, height - block_size) / block_size) * block_size

    while not game_over:
        while game_close:
            game_window.fill(black)
            display_message("Вы проиграли! Нажмите Q для выхода или R для возобновления игры", red)
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        game_window.fill(black)
        pygame.draw.rect(game_window, red, [food_x, food_y, block_size, block_size])
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        display_score(snake_length - 1)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, height - block_size) / block_size) * block_size
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()