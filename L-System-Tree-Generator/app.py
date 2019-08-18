import math
import pygame
import random
import sys

if __name__ == '__main__':
    alphabet = {'F'}
    rules = {'F': 'FF+[+F-F-F]-[-F+F+F]'}
    AXIOM = 'F'
    for _ in range(int(sys.argv[1])):
        AXIOM = ''.join((rules[step] if step in alphabet else step for step in AXIOM))

    position = (int(sys.argv[3])/2, int(sys.argv[3])-10)
    points = [(position, position)]
    positions = []
    deg = 0
    R = -int(sys.argv[2])

    for move in AXIOM:
        if move == 'F':
            new_x = position[0] + R * math.cos(math.radians(90 - deg))
            new_y = position[1] + R * math.sin(math.radians(90 - deg))
            new_position = (new_x, new_y)
            points.append((position, new_position))
            position = new_position
        elif move == '[':
            positions.append((position, deg))
        elif move == ']':
            position = positions[-1][0]
            deg = positions[-1][1]
            positions = positions[:-1]
        elif move == '+':
            deg += 25 + (random.randint(0, 6) - 3)
        elif move == '-':
            deg -= 25 + (random.randint(0, 6) - 3)

    s = pygame.Surface((int(sys.argv[3]), int(sys.argv[3])), 0, 32)
    for line in points[1:]:
        pygame.draw.line(s, (0xFF, 0xFF, 0xFF), *line)
    pygame.image.save(s, 'tree.jpg')
