
CARRIER_LENGTH = 5
BATTLESHIP_LENGTH = 4
CRUISER_LENGTH = 3
SUBMARINE_LENGTH = 2
PATROL_LENGTH = 1

CARRIER = 9
BATTLESHIP = 8
CRUISER = 7
SUBMARINE = 6
PATROL = 5
UNDEFINED = -1


class Ship:
    def __init__(self, start_position, end_position, length):
        """
        superclass constructor
        :param start_position: Position object for starting location (inclusive)
        :param end_position: Position object for ending location (inclusive)
        :param length: length of the ship, implemented in each subclass
        """
        self.start_position = start_position
        self.end_position = end_position
        self.length = length
        self.sunk = False
        self.hits = 0

    def get_ship(self):
        """
        identifies a player's own ship on the board

        :return: unique integer for ship class
        """
        return UNDEFINED


class Carrier(Ship):
    def __init__(self, start_position, end_position):
        super(Carrier, self).__init__(start_position, end_position, CARRIER_LENGTH)

    def get_ship(self):
        return CARRIER

    @staticmethod
    def to_str():
        """
        :return: string representation of the class
        """
        return 'carrier'


class Battleship(Ship):
    def __init__(self, start_position, end_position):
        super(Battleship, self).__init__(start_position, end_position, BATTLESHIP_LENGTH)

    def get_ship(self):
        return BATTLESHIP

    @staticmethod
    def to_str():
        return 'battleship'


class Cruiser(Ship):
    def __init__(self, start_position, end_position):
        super(Cruiser, self).__init__(start_position, end_position, CRUISER_LENGTH)

    def get_ship(self):
        return CRUISER

    @staticmethod
    def to_str():
        return 'cruiser'


class Submarine(Ship):
    def __init__(self, start_position, end_position):
        super(Submarine, self).__init__(start_position, end_position, SUBMARINE_LENGTH)

    def get_ship(self):
        return SUBMARINE

    @staticmethod
    def to_str():
        return 'submarine'


class PatrolBoat(Ship):
    def __init__(self, start_position, end_position):
        super(PatrolBoat, self).__init__(start_position, end_position, PATROL_LENGTH)

    def get_ship(self):
        return PATROL

    @staticmethod
    def to_str():
        return 'patrol'
