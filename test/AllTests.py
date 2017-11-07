import src.battleship.Ship as Ship
from src.battleship.Position import Position
import src.battleship.Board as Board
import unittest


class PositionTest(unittest.TestCase):

    def test_constructor(self):
        pos = Position(1, 2)
        self.assertTrue(pos is not None)
        self.assertTrue(pos.x == 1)
        self.assertTrue(pos.y == 2)


class BoardTest(unittest.TestCase):

    def test_constructors(self):
        board = Board.Board()
        ship_board = Board.ShipBoard()
        guess_board = Board.GuessBoard()
        self.assertIsNotNone(board)
        self.assertIsNotNone(ship_board)
        self.assertIsNotNone(guess_board)
        self.assertEqual(len(ship_board.board), Board.BOARD_SIZE)

    def test_out_of_bounds(self):
        self.assertTrue(Board.Board().__class__.out_of_bounds(Position(Board.BOARD_SIZE, 0)))

    def test_place_ship(self):
        ship_board = Board.ShipBoard()
        invalid = ship_board.place_ship(Ship.Submarine(
            Position(Board.BOARD_SIZE-1, 0), Position(Board.BOARD_SIZE, 0)))
        valid = ship_board.place_ship(Ship.Submarine(Position(0, 0), Position(1, 0)))
        self.assertFalse(invalid)
        self.assertTrue(valid)

    def test_blocked(self):
        ship_board = Board.ShipBoard()
        ship_board.place_ship(Ship.Submarine(Position(0, 0), Position(1, 0)))
        self.assertTrue(Board.is_blocked(ship_board.board, Position(0, 0), Position(0, 1))[0])
        self.assertTrue(Board.is_blocked(ship_board.board, Position(0, 0), Position(1, 0))[0])
        self.assertFalse(Board.is_blocked(ship_board.board, Position(0, 1), Position(0, 1))[0])


def setup():
    carrier = Ship.Carrier(Position(1, 5), Position(5, 5))
    battleship = Ship.Battleship(Position(0, 0), Position(0, 3))
    cruiser = Ship.Cruiser(Position(5, 0), Position(3, 0))
    submarine = Ship.Submarine(Position(2, 2), Position(2, 3))
    patrol = Ship.PatrolBoat(Position(3, 4), Position(3, 4))
    return carrier, battleship, cruiser, submarine, patrol


class ShipTest(unittest.TestCase):

    def test_constructors(self):
        carrier, battleship, cruiser, sub, patrol = setup()
        self.assertIsNotNone(carrier)
        self.assertIsNotNone(battleship)
        self.assertIsNotNone(cruiser)
        self.assertIsNotNone(sub)
        self.assertIsNotNone(patrol)

    def test_lengths_nums_str(self):
        carrier, battleship, cruiser, sub, patrol = setup()

        self.assertEqual(carrier.length, Ship.CARRIER_LENGTH)
        self.assertEqual(carrier.get_ship(), Ship.CARRIER)
        self.assertEqual(carrier.__class__.to_str(), 'carrier')

        self.assertEqual(battleship.length, Ship.BATTLESHIP_LENGTH)
        self.assertEqual(battleship.get_ship(), Ship.BATTLESHIP)
        self.assertEqual(battleship.__class__.to_str(), 'battleship')

        self.assertEqual(cruiser.length, Ship.CRUISER_LENGTH)
        self.assertEqual(cruiser.get_ship(), Ship.CRUISER)
        self.assertEqual(cruiser.__class__.to_str(), 'cruiser')

        self.assertEqual(sub.length, Ship.SUBMARINE_LENGTH)
        self.assertEqual(sub.get_ship(), Ship.SUBMARINE)
        self.assertEqual(sub.__class__.to_str(), 'submarine')

        self.assertEqual(patrol.length, Ship.PATROL_LENGTH)
        self.assertEqual(patrol.get_ship(), Ship.PATROL)
        self.assertEqual(patrol.__class__.to_str(), 'patrol')


if __name__ == '__main__':
    unittest.main()
