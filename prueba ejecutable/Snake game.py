import pygame
import random
# import time

# init pygame
pygame.init()

# init colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 165, 0)

width, height = 600, 400

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake game")

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

message_font = pygame.font.SysFont('ubuntu', 30)
score_font = pygame.font.SysFont('ubuntu', 25)
name_font = pygame.font.SysFont('ubuntu', 18)


def print_score(score):
    text = score_font.render("Score: " + str(score), True, orange)
    game_display.blit(text, [0, 0])


def draw_snake(snake_size_, snake_pixel):
    for pixel in snake_pixel:
        pygame.draw.rect(game_display, white, [pixel[0], pixel[1], snake_size_, snake_size_])


def run_game():
    game_over = False
    game_close = False

    snake_move = False

    x = width / 2
    y = height / 2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    target_y = round(random.randrange(0, height - snake_size) / 10) * 10.0

    while not game_over:

        while game_close:

            game_display.fill(black)
            game_over_mesage = message_font.render("Game Over", True, red)
            game_display.blit(game_over_mesage, [width / 2.6, height / 3])
            print_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                    continue
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                        continue
                    # if event.key == pygame.K_2:
                    #     run_game()

                    run_game()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    game_over = True
                    game_close = False
                    continue

                if event.key == pygame.K_LEFT and not x_speed == snake_size:
                    x_speed = -snake_size
                    y_speed = 0

                    snake_move = True

                if event.key == pygame.K_RIGHT and not x_speed == -snake_size:
                    x_speed = snake_size
                    y_speed = 0

                    snake_move = True

                if event.key == pygame.K_DOWN and not y_speed == -snake_size:
                    x_speed = 0
                    y_speed = snake_size

                    snake_move = True

                if event.key == pygame.K_UP and not y_speed == snake_size:
                    x_speed = 0
                    y_speed = -snake_size

                    snake_move = True

        if x not in range(0, width) or y not in range(0, height):
            game_close = True

        x += x_speed
        y += y_speed

        game_display.fill(black)
        pygame.draw.rect(game_display, orange, [target_x, target_y, snake_size, snake_size])

        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        if snake_move:
            for pixel in snake_pixels[:-1]:
                if pixel == [x, y]:
                    game_close = True

        draw_snake(snake_size, snake_pixels)
        print_score(snake_length - 1)

        text1 = name_font.render("By Marcos Reyes", True, orange)
        game_display.blit(text1, [480, 380])

        pygame.display.update()

        if [x, y] == [target_x, target_y]:

            target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            target_y = round(random.randrange(0, height - snake_size) / 10) * 10.0

            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


run_game()
