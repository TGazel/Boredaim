import board

class BoardItem:
    """General class for item on board"""
    def __init__(self, position):
        self.position = position

    def __get__(self):
        return self.position

class Obstacle(BoardItem):
    """Obstacle class for obstacle on board"""
    def __init__(self, position, movable = False, breakable = 1):
        BoardItem.__init__(self, position)
        self.movable = movable
        self.breakable = breakable

class Piece(BoardItem):
    """Piece class for player piece on board"""
    def __init__(self, position, player):
        BoardItem.__init__(self, position)
        self.player = player

    def move(self, position):
        self.position = position
        pass

class Shooter(Piece):
    def __init__(self, position, player):
        Piece.__init__(self, position, player)
        self.aim = 0
        pass

