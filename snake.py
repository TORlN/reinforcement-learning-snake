import pygame
import random

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

class Snake:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.segments = [[200,200], [200,210], [200,220]]
        self.direction = 'RIGHT'
    def move(self, distance):
        head_x, head_y = self.segments[0]
        if self.direction == 'RIGHT':
            new_head = (head_x + distance, head_y)
        elif self.direction == 'LEFT':
            new_head = (head_x - distance, head_y)
        elif self.direction == 'UP':
            new_head = (head_x, head_y - distance)
        elif self.direction == 'DOWN':
            new_head = (head_x, head_y + distance)
        self.segments.insert(0, new_head)
        self.segments.pop()
    
    def draw(self, window):
        for segment in self.segments:
            pygame.draw.rect(window, green, pygame.Rect(segment[0], segment[1], 10, 10))
    
    def check_collision(self, win_width, win_height):
        head = self.segments[0]
        x, y = head
        if x < 0 or x >= win_width or y < 0 or y >= win_height or head in self.segments[1:]:
            return True
        return False
    def grow(self):
        prevSeg = self.segments[len(self.segments)-1]
        self.segments.append(prevSeg)
    
class Food:
    def __init__(self):
        self.reset()
    def reset(self):
        self.position = self.spawn()
    def spawn(self):
        return random.randint(0,39) * 10, random.randint(0, 29) * 10
    def draw(self, window):
        pygame.draw.rect(window, red, pygame.Rect(self.position[0], self.position[1], 10, 10))
    def eaten(self, snake):
        if pygame.Rect(self.position[0], self.position[1], 10, 10).colliderect(pygame.Rect(snake.segments[0][0], snake.segments[0][1], 10, 10)):
            self.position = self.spawn()
            return True
        return False
        
    
    