from copy import deepcopy


class Node:

    def __init__(self, sequence, terminal_sequence, parent=None):
        self.sequence = sequence
        self.parent = parent
        self.terminal_sequence = terminal_sequence
        if self.parent:
            self.h = parent.h + 1
        else:
            self.h = 0

    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        board = self.flat_to_board(self.sequence)
        return ''.join([str(row) + "\n" for row in board])[:-1]

    @property
    def g(self):
        return self.manhattan_distance(self.terminal_sequence)

    @property
    def f(self):
        return self.h + self.g

    @property
    def neighbours(self):
        side_size = int(len(self.sequence) ** 0.5)
        actions = [-side_size, side_size, -1, 1]
        zero_position = self.get_zero_index()

        # Проверка допустимости ходов
        directions = []
        for action in actions:

            if zero_position + action < 0 or zero_position + action >= len(self.sequence):
                continue
            if action == 1 and (zero_position + 1) % side_size == 0:
                continue
            if action == -1 and (zero_position + 1) % side_size == 1:
                continue
            directions.append(zero_position + action)
        # Формирование дочерних вершин
        neighbours = (self.move(zero_position, direction) for direction in directions)
        return neighbours

    def manhattan_distance(self, goal):
        distance = 0
        side_size = int(len(self.sequence) ** 0.5)
        board = self.flat_to_board(self.sequence)

        for x in range(side_size):
            for y in range(side_size):
                value = board[x][y]
                x_goal, y_goal = self.get_element_index(value, goal)
                distance += abs(x - x_goal) + abs(y - y_goal)
        return distance

    def get_element_index(self, element, sequence):
        board = self.flat_to_board(sequence)
        for row_index, row in enumerate(x for x in board):
            try:
                item_index = row.index(element)
                return row_index, item_index
            except ValueError:
                pass

    def get_zero_index(self):
        board = self.sequence
        for index, item in enumerate(board):
            if item == 0:
                return index

    def move(self, at, to):
        neighbour = list(deepcopy(self.sequence))
        neighbour[at], neighbour[to] = neighbour[to], neighbour[at]
        return tuple(neighbour)

    @staticmethod
    def flat_to_board(sequence):
        side_size = int(len(sequence) ** 0.5)
        board = []
        row = []
        for i, item in enumerate(sequence):
            row.append(item)
            if (i + 1) % side_size == 0:
                board.append(deepcopy(row))
                row.clear()
        return board
