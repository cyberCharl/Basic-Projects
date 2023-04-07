import pygame
import time
from pygame.locals import *

SIZE = 20

class Snake:
    def __init__(self, parent_screen, direction, length):
        self.length = length
        self.direction = direction
        self.parent_screen = parent_screen
        x_pos = self.parent_screen.get_size()[0] // 2 
        y_pos = self.parent_screen.get_size()[1] // 2 
        self.snake = pygame.draw.rect(parent_screen, (137, 220, 235), Rect(x_pos, y_pos, 20, 20), 4) 
        self.x = [SIZE] * length
        self.y = [SIZE] * length

    def drawSnake(self):
        self.parent_screen.fill((30, 30, 46))
        for i in range(self.length):
            pygame.draw.rect(self.parent_screen, (137, 220, 235), Rect(self.x[i], self.y[i], 20, 20), 4) 
        pygame.display.flip()
    
    def slither(self):

        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        match self.direction:
            case "Right":
                self.x[0] += SIZE
            case "Left":
                self.x[0] -= SIZE
            case "Up":
                self.y[0] -= SIZE
            case "Down":
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
        self.background = self.screen.fill((30, 30, 46))
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
            time.sleep(0.1)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()    
