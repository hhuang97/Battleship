import src.battleship.Ship as Ship
from src.battleship.Position import Position
from src.battleship.Player import Player
from src.battleship.Board import BOARD_SIZE


def game_end(player1, player2):
    """
    checks if the game has ended (e.g. one player has no ships remaining)
    :param player1: first player
    :param player2: second player
    :return: 0 if the game has not ended, 1 if player1 won, 2 if player2 won
    """
    player1_sunk = True
    player2_sunk = True
    for ship in player1.ships:
        player1_sunk &= ship.sunk
    for ship in player2.ships:
        player2_sunk &= ship.sunk
    return 2 if player1_sunk else (1 if player2_sunk else 0)


def get_ship_placement(player, ship_type):
    """
    gets input from user for (x,y) coordinates to place the ship_type for the player
    :param player: the player to set up ships for
    :param ship_type: Ship subclass object
    """
    ship_str = ship_type.__class__.to_str()
    invalid = True
    while invalid:
        ship_start = input('Enter start position for ' + ship_str + ': ')
        ship_end = input('Enter end position for ' + ship_str + ': ')
        start_x = int(ship_start.split(',')[0])
        start_y = int(ship_start.split(',')[1])
        end_x = int(ship_end.split(',')[0])
        end_y = int(ship_end.split(',')[1])

        ship_type.start_position = Position(start_x, start_y)
        ship_type.end_position = Position(end_x, end_y)

        if player.ship_board.place_ship(ship_type):
            player.add_ship(ship_type)
            invalid = False
        if invalid:
            print('invalid placement, try again')


def place_all_ships(player):
    """
    wrapper function that handles player name setting and placement of all ships
    :param player: current player to set up the name and ships for
    """
    name_input = input('Enter player name (leave blank for default): ')
    player.name = name_input if name_input != '' else player.name
    # get_ship_placement(player, Ship.Carrier(None, None))
    # get_ship_placement(player, Ship.Battleship(None, None))
    # get_ship_placement(player, Ship.Cruiser(None, None))
    get_ship_placement(player, Ship.Submarine(None, None))
    get_ship_placement(player, Ship.PatrolBoat(None, None))


def print_player_info(player):
    """
    prints helpful information for the current player's turn
    :param player: player to print the info for
    """
    print(player.name + '\'s turn')
    print(player.name, 'ship board')
    player.ship_board.print_board()
    print('\n', player.name, 'guess board')
    player.guess_board.print_board()
    print('\n')


def parse_guess(guess_str):
    """
    utility function to parse the coordinates for a guess
    :param guess_str: string to parse
    :return: tuple containing x and y integer coordinates
    """
    coordinates = guess_str.replace(' ', '').split(',')
    x = int(coordinates[0])
    y = int(coordinates[1])
    out_of_bounds = x < 0 or x >= BOARD_SIZE or y < 0 or y >= BOARD_SIZE
    return x, y, out_of_bounds


def play_turn(curr_player, opponent):
    """
    Takes one guess for the current player
    :param curr_player: the current player taking the turn
    :param opponent: the defending player
    """
    print_player_info(curr_player)
    while True:
        guess = input('Make a guess (input format: x,y): ')
        x, y, out_of_bounds = parse_guess(guess)
        if not out_of_bounds:
            break
    guess_result = curr_player.make_guess(Position(x, y), opponent)
    print(guess_result, 'at', guess)


def main():
    """
    driver to launch the game and play it through
    """
    player1 = Player(1)
    player2 = Player(2)
    curr_player = player1
    opponent = player2
    salvo_input = input("Do you want to play the salvo variant (y/n)? ")
    salvo = True if 'y' in salvo_input.lower() or 'yes' in salvo_input.lower() else False
    place_all_ships(player1)
    place_all_ships(player2)
    while game_end(player1, player2) == 0:
        # number of guesses varies based on remaining ships in salvo variant
        num_guesses = len(curr_player.ships) if salvo else 1
        for i in range(num_guesses):
            play_turn(curr_player, opponent)
            if game_end(player1, player2) == 0:
                break
        curr_player = player1 if curr_player == player2 else player2
        opponent = player1 if curr_player == player2 else player2

    game_result = game_end(player1, player2)
    print(player1.name if game_result == player1.turn else player2.name, 'wins!')


if __name__ == '__main__':
    main()
