import pygame
import numpy as np
import random
import os

class Life():
    def __init__(self, width, height, scale, offset):
        self.scale = scale

        self.columns = int(height/scale)
        self.rows = int(width/scale)

        self.size = (self.rows, self.columns)
        self.Life_array = np.ndarray(shape=(self.size))
        self.offset = offset

    def random2d_array(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.Life_array[x][y] = random.randint(0,1)


    def Conway(self, off_color, on_color, surface, pause=False):
        for x in range(self.rows):
            for y in range(self.columns):
                y_pos = y * self.scale
                x_pos = x * self.scale
                if self.Life_array[x][y] == 1:
                    pygame.draw.rect(surface, on_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                else:
                    pygame.draw.rect(surface, off_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])

        next = np.ndarray(shape=(self.size))
        if pause == False:
            for x in range(self.rows):
                for y in range(self.columns):
                    state = self.Life_array[x][y]
                    neighbours = self.get_neighbours( x, y)
                    if state == 0 and neighbours == 3:
                        next[x][y] = 1
                    elif state == 1 and (neighbours < 2 or neighbours > 3):
                        next[x][y] = 0
                    else:
                        next[x][y] = state
            self.Life_array = next

    def HandleMouse(self, x, y):
        _x = x//self.scale
        _y = y//self.scale

        if self.Life_array[_x][_y] != None:
            self.Life_array[_x][_y] = 1
        

    def get_neighbours(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x+n+self.rows) % self.rows
                y_edge = (y+m+self.columns) % self.columns
                total += self.Life_array[x_edge][y_edge]

        total -= self.Life_array[x][y]
        return total


class Beauty_game():
    def __init__(self, width, height):
        os.environ["SDL_VIDEO_CENTERED"]='1'
        self.Life = Life
        self.width, self.height = width, height

        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.fps = 30

        self.black = pygame.Color('#F6F6F6')
        self.contrast = pygame.Color('#212121')
        self.white = pygame.Color('#F6F6F6')

        self.scaler = 10
        self.offset = 1

    def create_Life(self, Life):
        Life = Life(self.width,self.height, self.scaler, self.offset)
        Life.random2d_array()

        run = True
        while run:
            self.clock.tick(self.fps)
            self.screen.fill(self.black)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
            Life.Conway(off_color=self.white, on_color=self.contrast, surface=self.screen)

            if pygame.mouse.get_pressed()[0]:
                mouseX, mouseY = pygame.mouse.get_pos()
                Life.HandleMouse(mouseX, mouseY)
            pygame.display.update()
        pygame.quit()

def main_pygame(width, height, _):
    Beauty_game(width, height).create_Life(Life)