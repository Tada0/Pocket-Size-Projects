import sys


class Sudoku:
    class Cell:
        def __init__(self, grid_pos: (int, int), value: int):
            self.index = 0
            self.value = value
            self.neighbours = None
            self.possible_values = None
            self.grid_position = dict(
                zip(('col', 'row', 'sq'), (*grid_pos, tuple(map(lambda x: int(x / 3), grid_pos)))))

        def grid(self, key: str) -> int or tuple:
            return self.grid_position[key]

        def zero(self):
            self.value = 0
            self.index = 0

    def __init__(self, grid):
        self.cells = [Sudoku.Cell((x, y), grid[x + 9 * y]) for y in range(9) for x in range(9)]
        self.empty_cells = [cell for cell in self.cells if not cell.value]
        self.current_cell_index = 0
        self.calculate_neighbours()
        self.calculate_possible_values()

    def calculate_possible_values(self):
        possibilities = [i for i in range(1, 10)]
        for cell in self.cells:
            cell.possible_values = sorted(tuple(set(possibilities) - set([n.value for n in cell.neighbours])))

    def calculate_neighbours(self):
        for cell in self.cells:
            neighbours = [c for c in self.cells if any([c.grid(s) == cell.grid(s) for s in ('col', 'row', 'sq')])]
            cell.neighbours = ([neighbour for neighbour in neighbours if neighbour is not cell])

    def __solve(self):
        current_cell = self.empty_cells[self.current_cell_index]

        if not current_cell.value < next(iter(reversed(current_cell.possible_values))):
            current_cell.zero()
            self.current_cell_index -= 1
            return

        current_cell.value = current_cell.possible_values[current_cell.index]
        current_cell.index += 1

        if not current_cell.value in set([n.value for n in current_cell.neighbours]):
            self.current_cell_index += 1

    def is_solved(self):
        return all([n.value and c.value != n.value for c in self.cells for n in c.neighbours])

    def solve(self):
        while not self.is_solved():
            self.__solve()
        return [str(c.value) for c in self.cells]


def show(raw):
    for idx, trow in enumerate(tuple(tuple(raw[x:x + 9]) for x in range(0, len(raw), 9))):
        print(' | '.join(map(' '.join, tuple(tuple(trow[x:x + 3]) for x in range(0, len(trow), 3)))))
        print("---------------------") if (idx+1) % 3 == 0 and idx != 8 else None


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        sudoku = [int(s) for s in file.read().split() if s.isdigit()]

    solved_sudoku = Sudoku(sudoku).solve()
    show(solved_sudoku)
