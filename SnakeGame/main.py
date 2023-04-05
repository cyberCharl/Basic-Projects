import pygame
import time
from pygame.locals import *

SIZE = 20

class Snake:
    def __init__(self, parent_screen, direction, length):
        self.length = length
        self.direction = direction
        self.parent_screen = parent_screen
        self.snake = pygame.image.load("resources/snake.jpg").convert()
        self.x = [SIZE] * length
        self.y = [SIZE] * length

    def drawSnake(self):
        self.parent_screen.blit(self.parent_screen, (0,0))        
        for i in range(self.length):
            self.parent_screen.blit(self.snake, (self.x[i], self.y[i]))
        pygame.display.flip()
    
    def slither(self):

        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == "Right":
            self.x[0] += SIZE
        if self.direction == "Left":
            self.x[0] -= SIZE
        if self.direction == "Up":
            self.y[0] -= SIZE
        if self.direction == "Down":
            self.y[0] += SIZE
        
        self.drawSnake()


    def moveRight(self):
        self.direction ="Right"

    def moveLeft(self):
        self.direction ="Left"

    def moveUp(self):
        self.direction ="Up"

    def moveDown(self):
        self.direction ="Down"

class Game:
# basic game loop attempt         
    def __init__(self): 
        pygame.init() 
        self.screen = pygame.display.set_mode((1280,720))
        self.grass = pygame.image.load("resources/grass.jpg").convert()
        self.screen.blit(self.grass, (0,0))        
        self.clock = pygame.time.Clock()
        self.snake = Snake(self.screen, "Right", 5)

    def run(self) :
        running = True

        # Game event loop
        while running:
            # Quit game functionality
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(self.grass, (0,0))

            # Listen for keystokes
            keys = pygame.key.get_pressed() 
            if keys[pygame.K_w]:
                self.snake.moveUp()
                # direction = "Up"
            if keys[pygame.K_s]:
                self.snake.moveDown()
                # direction = "Down"
            if keys[pygame.K_a]:
                self.snake.moveLeft()
                # direction = "Left"
            if keys[pygame.K_d]:
                self.snake.moveRight()
                # direction = "Right"

            self.snake.slither()          
            # Flip / Update screen
            pygame.display.flip()
            time.sleep(0.2)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()    
