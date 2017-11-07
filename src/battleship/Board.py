import sys

BOARD_SIZE = 3

UNKNOWN = 0  # empty for ship board, unknown for guess board
HIT = 1
MISS = 2
SUNK = 3


def is_blocked(board, start, end):
    """
    checks if the coordinates from start to end, inclusive of both, are blocked anywhere
    :param board: ship board
    :param start: starting Position object
    :param end: ending Position object
    :return: tuple containing True if at least one position is blocked from start to end, False otherwise,
             also contains the manhattan distance between start and end
    """
    if start.x == end.x:
        return check_blocked(board, start, end, True), abs(start.y - end.y) + 1  # horizontal
    return check_blocked(board, start, end, False), abs(start.x - end.x) + 1  # vertical


def check_blocked(board, start, end, x_move):
    """
    helper function for is_blocked
    :param board: ship board
    :param start: starting Position object
    :param end: ending Position object
    :param x_move: True if x is NOT moving (e.g. y direction change only)
    :return: True
    """
    if x_move:
        for y in range(min(start.y, end.y), max(start.y, end.y)+1):
            if board[start.x][y] != UNKNOWN:  # empty cells are UNKNOWN (0)
                return True
    else:
        for x in range(min(start.x, end.x), max(start.x, end.x)+1):
            if board[x][start.y] != UNKNOWN:
                return True
    return False


class Board:
    def __init__(self):
        self.board = [[UNKNOWN for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]

    @staticmethod
    def out_of_bounds(position):
        """
        checks if the position is out of bounds
        :param position: Position object to check
        :return: True if position is out of bounds, False otherwise
        """
        x = position.x
        y = position.y
        return x < 0 or x >= BOARD_SIZE or y < 0 or y >= BOARD_SIZE

    def print_board(self):
        """
        utility for printing the board
        """
        for row in self.board:
            for elem in row:
                sys.stdout.write(str(elem) + '\t')
            sys.stdout.write('\n')


class GuessBoard(Board):
    def __init__(self):
        super(GuessBoard, self).__init__()


class ShipBoard(Board):
    def __init__(self):
        super(ShipBoard, self).__init__()

    def place_ship(self, ship):
        """
        places the ship on the player's own ship board, used when initializing the game
        :param ship: the ship to be placed
        :return: True if the ship can be placed at its position parameters, False otherwise
        """
        start_pos = ship.start_position
        end_pos = ship.end_position
        if Board.out_of_bounds(start_pos) or Board.out_of_bounds(end_pos):
            return False

        if start_pos.x != end_pos.x and start_pos.y != end_pos.y:
            return False
        is_block, dist = is_blocked(self.board, start_pos, end_pos)
        min_x = min(start_pos.x, end_pos.x)
        max_x = max(start_pos.x, end_pos.x)
        min_y = min(start_pos.y, end_pos.y)
        max_y = max(start_pos.y, end_pos.y)
        if not is_block and ship.length == dist:
            for x in range(min_x, max_x+1):
                for y in range(min_y, max_y+1):
                    self.board[x][y] = ship.get_ship()
            return True

        return False
