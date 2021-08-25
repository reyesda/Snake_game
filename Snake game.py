import pygame
import random

# init the game,

pygame.init()

# init colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 165, 0)
blue = (100, 100, 255)

# tamaño del display
width_display, height_display = 1000, 700

game_display = pygame.display.set_mode((width_display, height_display))
pygame.display.set_caption("Snake game")

clock = pygame.time.Clock()


# clase para jugador


class Snake:
    def __init__(self, size, color):
        self.size = size
        self.speed_x = 0
        self.speed_y = 0
        self.pixels = []
        self.length = 1
        self.color = color
        self.x = width_display / 2
        self.y = height_display / 2
        self.move = False

    def draw_snake(self):
        for pixel in self.pixels:
            pygame.draw.rect(game_display, self.color, [pixel[0], pixel[1], self.size, self.size])


# clase comida


class Target:
    def __init__(self, snake_size, width, height):
        self.x = 0
        self.y = 0
        self.snake_size = snake_size
        self.width = width
        self.height = height

    def position(self):
        self.x = round(random.randrange(0, self.width - self.snake_size) / 10.0) * 10.0
        self.y = round(random.randrange(0, self.height - self.snake_size) / 10) * 10.0


class Obstacle:
    def __init__(self, snake_size_o, width_o, height_o, color):
        self.snake_size_o = snake_size_o
        self.width_o = width_o
        self.height_o = height_o
        self.x = 0
        self.y = 0
        self.position_o = []
        self.color = color

    def position(self):
        self.x = round(random.randrange(0, self.width_o - self.snake_size_o) / 10.0) * 10.0
        self.y = round(random.randrange(0, self.height_o - self.snake_size_o) / 10) * 10.0

        self.position_o.append([self.x, self.y])

    def draw_obstacle(self):
        for pixel in self.position_o:
            pygame.draw.rect(game_display, self.color, [pixel[0], pixel[1], self.snake_size_o, self.snake_size_o])


# formato de los mensjes
message_font = pygame.font.SysFont('ubuntu', 30)
score_font = pygame.font.SysFont('ubuntu', 25)
name_font = pygame.font.SysFont('ubuntu', 18)


def print_score(score):
    text = score_font.render("Score: " + str(score), True, orange)
    game_display.blit(text, [0, 0])


n_obtacle = 20


def run_game():
    game_over = False
    game_close = False

    snake = Snake(10, white)
    target1 = Target(snake.size, width_display, height_display)
    obstacle = Obstacle(snake.size, width_display, height_display, blue)

    obstacle.position()
    target1.position()

    while not game_over:

        while game_close:

            game_display.fill(black)
            game_over_mesage = message_font.render("Game Over", True, red)
            game_display.blit(game_over_mesage, [width_display / 2.6, height_display / 3])

            print_score(snake.length - 1)

            text1 = name_font.render("By Marcos Reyes", True, orange)
            game_display.blit(text1, [width_display - 115, height_display - 20])

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

                if event.key == pygame.K_LEFT and not snake.speed_x == snake.size:
                    snake.speed_x = -snake.size
                    snake.speed_y = 0

                    snake.move = True

                if event.key == pygame.K_RIGHT and not snake.speed_x == -snake.size:
                    snake.speed_x = snake.size
                    snake.speed_y = 0

                    snake.move = True

                if event.key == pygame.K_DOWN and not snake.speed_y == -snake.size:
                    snake.speed_x = 0
                    snake.speed_y = snake.size

                    snake.move = True

                if event.key == pygame.K_UP and not snake.speed_y == snake.size:
                    snake.speed_x = 0
                    snake.speed_y = -snake.size

                    snake.move = True

        # if snake.xa not in range(0 + int(snake.size/2), width_display - int(snake.size/2)) \
        #         or snake.ya not in range(0 + int(snake.size/2), height_display - int(snake.size/2)):
        #     game_close = True

        if snake.x < 0:
            snake.x = width_display - snake.size

        if snake.x > width_display:
            snake.x = snake.size

        if snake.y > height_display:
            snake.y = snake.size

        if snake.y < 0:
            snake.y = height_display - snake.size

        snake.x += snake.speed_x
        snake.y += snake.speed_y

        game_display.fill(black)
        pygame.draw.rect(game_display, red, [target1.x, target1.y, snake.size, snake.size])
        snake.pixels.append([snake.x, snake.y])

        if len(snake.pixels) > snake.length:
            del snake.pixels[0]

        if snake.move:
            for pixel in snake.pixels[:-1]:
                if pixel == [snake.x, snake.y]:
                    game_close = True

        snake.draw_snake()
        obstacle.draw_obstacle()
        print_score(snake.length - 1)

        text1 = name_font.render("By Marcos Reyes", True, orange)
        game_display.blit(text1, [width_display - 115, height_display - 20])

        if [snake.x, snake.y] == [target1.x, target1.y]:

            target1.position()
            for i in range(n_obtacle):
                obstacle.position()

            snake.length += 1

        posx, posy = pygame.mouse.get_pos()
        # print(posx, posy, " -- ", int(target1.xa) + int(snake.size / 2), int(target1.xa) - int(snake.size / 2))
        # pygame.draw.line(game_display, white, [0, 0], [posx, posy], 2)

        if posx in range(int(target1.x) - int(snake.size / 0.5), int(target1.x) + int(snake.size / 0.5)) \
                and posy in range(int(target1.y) - int(snake.size / 0.5), int(target1.y) + int(snake.size / 0.5)):
            target1.position()

        for obs in obstacle.position_o:
            if [snake.x, snake.y] == obs:
                game_close = True

        clock.tick(15)
        pygame.display.update()

    pygame.quit()
    quit()


run_game()
