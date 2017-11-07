import src.battleship.Board as Board


class Player:
    def __init__(self, turn):
        """
        constructor to make a new player
        :param turn: player's number
        """
        self.guess_board = Board.GuessBoard()
        self.ship_board = Board.ShipBoard()
        self.turn = turn
        self.ships = list()
        self.name = 'Player 1' if turn == 1 else 'Player 2'

    def add_ship(self, ship):
        """
        :param ship: ship to be added to player's list
        """
        self.ships.append(ship)

    def make_guess(self, position, opponent):
        """
        current player (self) guesses a position on the opponent board
        :param position: the guessed Position
        :param opponent: the player whose ship the current player is trying to guess
        :return: string containing either 'HIT', 'MISS', or 'SUNK' to indicate the result of the guess
        """
        result, result_str = opponent.mark_board(position)
        self.guess_board.board[position.x][position.y] = result
        return result_str

    def mark_board(self, position):
        """
        utility function for marking opponent's ship board
        :param position: Position to be marked
        :return: see get_ship_type
        """
        x = position.x
        y = position.y
        return self.get_ship_type(self.ship_board.board[x][y], self)

    @staticmethod
    def get_ship_type(ship_num, player):
        """
        utility for mark_board
        :param ship_num: the unique integer identifying the ship type (see Ship)
        :param player: the player to get the ship board for
        :return: a tuple containing two strings, first is for the board and second is for the user
        """
        ship_class = None
        for ship in player.ships:
            if ship.get_ship() == ship_num:
                ship_class = ship
                break

        if ship_class is None:
            return 'M', 'MISS'

        ship_class.hits += 1
        if ship_class.hits == ship_class.length:
            # print(ship_class, 'sunk')
            ship_class.sunk = True
            return 'S', 'SUNK'
        return 'H', 'HIT'
