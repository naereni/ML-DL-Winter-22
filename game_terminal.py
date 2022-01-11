from random import randint
from os import system as clear
from platform import system
from copy import deepcopy
from time import sleep

class Life():
    def __init__(self, width, height, gen):
        self.COLS = width
        self.ROWS = height
        self.GENERATIONS = gen

        if system() == 'Windows':
            self.CLEAR = 'cls'
        else:
            self.CLEAR = 'clear'

    def init_grid(self, rows, cols, making_gen):
        for i in range(rows):
            making_gen_row = []
            for j in range(cols):
                if (i == 0 or j == 0 or (i == rows - 1) or (j == cols - 1)):
                    making_gen_row += [-1]
                else:
                    ran = randint(0,3)
                    if ran == 0:
                        making_gen_row += [1]
                    else:
                        making_gen_row += [0]
            making_gen += [making_gen_row]

        
    def print_gen(self, rows, cols, making_gen, gen_no):
        clear(self.CLEAR)

        print("Итерация номер " + str(gen_no) )
        
        for i in range(rows):
            for j in range(cols):
                if making_gen[i][j] == -1:
                    print("+", end="")
                elif making_gen[i][j] == 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print("")
        
    def process_neighbours(self, x, y, making_gen):
        n_count = 0
        for j in range(y-1,y+2):
            for i in range(x-1,x+2):
                if not(i == x and j == y):
                    if making_gen[i][j] == 1:
                        n_count += making_gen[i][j]
        if making_gen[x][y] == 1 and (n_count < 2 or n_count > 3):
            return 0
        if making_gen[x][y] == 0 and n_count == 3:
            return 1
        else:
            return making_gen[x][y]

    def process_next_gen(self, rows, cols, current_status, next_status):
        for i in range(1,rows-1):
            for j in range(1,cols-1):
                next_status[i][j] = self.process_neighbours(i, j, current_status)

    def term_game(self):
        this_gen = []
        next_gen = []

        self.init_grid(self.ROWS, self.COLS, this_gen)

        next_gen = deepcopy(this_gen)

        self.print_gen(self.ROWS, self.COLS, this_gen, 0)

        for gens in range(1, self.GENERATIONS+1):
            self.process_next_gen(self.ROWS, self.COLS, this_gen, next_gen)
            self.print_gen(self.ROWS, self.COLS, next_gen, gens)
            this_gen = deepcopy(next_gen)
            sleep(0.5)

def main_term(width, height, gen):
    Life(width, height, gen).term_game()
