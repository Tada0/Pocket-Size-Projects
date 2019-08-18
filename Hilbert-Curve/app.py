import pygame
import sys


def generate_hilbert_curve(cell_size, moves):
    lines = [(int(cell_size / 2), (int(sys.argv[2]) - cell_size) + int(cell_size / 2))]
    direction = 'RIGHT'
    dir_dict = {'LEFT': {'TOP': 'LEFT', 'LEFT': 'BOTTOM', 'BOTTOM': 'RIGHT', 'RIGHT': 'TOP'},
                'RIGHT': {'TOP': 'RIGHT', 'RIGHT': 'BOTTOM', 'BOTTOM': 'LEFT', 'LEFT': 'TOP'}}

    def get_new_point():
        return {'TOP': (lines[-1][0], lines[-1][1] - cell_size),
                'LEFT': (lines[-1][0] - cell_size, lines[-1][1]),
                'RIGHT': (lines[-1][0] + cell_size, lines[-1][1]),
                'BOTTOM': (lines[-1][0], lines[-1][1] + cell_size)}[direction]

    for move in moves:
        if move in {'LEFT', 'RIGHT'}:
            direction = dir_dict[move][direction]
        else:
            lines.append(get_new_point())
    return lines


def generate_moves(steps):
    alphabet = {'A', 'B'}
    rules = {'A': '-BF+AFA+FB-', 'B': '+AF-BFB-FA+'}
    drawing_steps = {'F': 'DRAW', '-': 'LEFT', '+': 'RIGHT'}
    AXIOM = 'A'
    for _ in range(0, steps):
        AXIOM = ''.join([rules[AXIOM[idx]] if AXIOM[idx] in alphabet else AXIOM[idx] for idx in range(len(AXIOM))])
    return [drawing_steps[c] for c in AXIOM.replace('A', '').replace('B', '').replace('+-', '').replace('-+', '')]


if __name__ == '__main__':
    curve = generate_hilbert_curve(round(int(sys.argv[2]) / 2 ** int(sys.argv[1])), generate_moves(int(sys.argv[1])))
    surface = pygame.Surface((int(sys.argv[2]), int(sys.argv[2])), 0, 32)
    pygame.draw.lines(surface, (0xFF, 0x00, 0x00), False, curve, 1)
    pygame.image.save(surface, 'curve.jpg')
