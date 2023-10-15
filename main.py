import pygame
from snake import *

pygame.init()

clock = pygame.time.Clock()
win_height = 800
win_width = 800

win = pygame.display.set_mode((win_width, win_height))

snake = Snake()
food = Food()
speed = 100
running = True
while running:
    dt = clock.tick(60) / 1000  #Convert milliseconds to seconds
    snake.move(speed * dt)
    if snake.check_collision(win_width, win_height) == True:
        snake.reset()
        food.reset()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = 'UP'
            if event.key == pygame.K_DOWN:
                snake.direction = 'DOWN'
            if event.key== pygame.K_LEFT:
                snake.direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                snake.direction = 'RIGHT'
    if food.eaten(snake):
        snake.grow()
    pygame.display.update()

    #Clear the screen
    win.fill(black)

    #Draw to the screen here
    snake.draw(win)
    food.draw(win)

    #Update the display
    pygame.display.update()

#Quit pygame
pygame.quit()
