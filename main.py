from time import sleep
from game_pygame import main_pygame
from game_terminal import main_term
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type', type=int, help='term or pygame')
parser.add_argument('--width', type=int, help='width')
parser.add_argument('--height', type=int, help='height')
parser.add_argument('--gens', type=int, help='generations', default=None)
args = parser.parse_args()

print('Реализация игры "Жизнь" для вступительного экзамена ML&DL\Winter`22')

if args.type == 1:
     main_term(args.width, args.height, args.gens)

if args.type == 2:
    main_pygame(args.width, args.height, args.gens)