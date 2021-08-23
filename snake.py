# Snake 

import sys
import random
import pygame
from pygame.locals import *

# Game constants
FPS = 15
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELL_SIZE = 20
assert WINDOW_WIDTH % CELL_SIZE == 0, "Window width must be a multiple of cell size"
assert WINDOW_HEIGHT % CELL_SIZE == 0, "Window height must be a multiple of cell size"
CELL_WIDTH = int(WINDOW_WIDTH / CELL_SIZE)
CELL_HEIGHT = int(WINDOW_HEIGHT / CELL_SIZE)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game objects
class Snake(object):
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.body = []
        self.add_body(x, y)
        self.score = 0
        self.eaten = 0
        self.dead = False
        self.speed = 1
        self.color = GREEN
        
    def add_body(self, x, y):
        self.body.append((x, y))
        self.body.append((x - 1, y))
        self.body.append((x - 2, y))
        self.body.append((x - 3, y))
        self.body.append((x - 4, y))
        self.body.append((x - 5, y))
        self.body.append((x - 6, y))
        self.body.append((x - 7, y))
        self.body.append((x - 8, y))
        self.body.append((x - 9, y))
        self.body.append((x - 10, y))
        self.body.append((x - 11, y))
        
    def move(self):
        if self.dead:
            return
        if self.direction == 'up':
            self.y -= self.speed
        elif self.direction == 'down':
            self.y += self.speed
        elif self.direction == 'left':
            self.x -= self.speed
        elif self.direction == 'right':
            self.x += self.speed
        self.body.pop(0)
        self.body.append((self.x, self.y))
        if self.x < 0 or self.x >= CELL_WIDTH or self.y < 0 or self.y >= CELL_HEIGHT:
            self.dead = True

        
    def draw(self, surface):
        for x, y in self.body:
            pygame.draw.rect(surface, self.color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


class Food(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = RED

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def draw_text(text, surface, x, y):
    font_size = 20
    font = pygame.font.SysFont('Arial', font_size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Snake')
    clock = pygame.time.Clock()
    snake = Snake(CELL_WIDTH / 2, CELL_HEIGHT / 2, 'right')
    food = Food(random.randint(0, CELL_WIDTH - 1), random.randint(0, CELL_HEIGHT - 1))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    snake.direction = 'up'
                elif event.key == K_DOWN:
                    snake.direction = 'down'
                elif event.key == K_LEFT:
                    snake.direction = 'left'
                elif event.key == K_RIGHT:
                    snake.direction = 'right'
        screen.fill(BLACK)  
        snake.move()
        if snake.dead:
            draw_text('Game Over', screen, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
            pygame.display.update()
            pygame.time.wait(2000)
            break
        snake.draw(screen)
        food.draw(screen)
        if snake.x == food.x and snake.y == food.y:
            snake.eaten += 1
            snake.add_body(snake.x, snake.y)
            food.x = random.randint(0, CELL_WIDTH - 1)
            food.y = random.randint(0, CELL_HEIGHT - 1)
            snake.score += 1
            snake.speed += 1
            snake.color = GREEN

        draw_text('Score: ' + str(snake.score), screen, 10, 10)
        draw_text('Eaten: ' + str(snake.eaten), screen, 10, 30)
        draw_text('Speed: ' + str(snake.speed), screen, 10, 50)
        draw_text('Direction: ' + snake.direction, screen, 10, 70)
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()

