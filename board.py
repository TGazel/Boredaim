import piece
import numpy as np

class Board: 
    """
    Board class for storage and handling of board attributes and status, Obstacle and Players
    

    Notes: only one piece per cell 
    """  

    def __init__(self, size = (8,8)):
        self.gamestatus = 0

        self.size = size
        sizex,sizey = size 
        self.cellstatus = np.ones(size, dtype='i') 
        self.boardstatus = -1*np.ones((sizex,sizey, 2), dtype='i') #player (0 is Obstacle, -1 is None), piece 

        # creation of player and item tracking 
        self.players = []
        self.obstacles = []
        
    # Creation tools
    def addplayer(self, playerinit = {}):
        self.players.append(Player(**playerinit))

    def addobstacle(self, iteminit = {}):
        self.obstacles.append(piece.Obstacle(**iteminit))

    def addpiece(self, player, pieceinit = {}):
        self.players[player].addpiece(pieceinit)

    # Check tools
    def isvalidcell(self, position) -> bool:
        for s, p in zip(self.size, self.position):
            if p<0 or p>=s: return False
        return True

    def isemptycell(self, position) -> bool: 
        if not self.isvalidcell(position): return False
        pass

    def updateboardstatus(self):
        pass


class Player:
    """Player class """  
    def __init__(self):
        self.pieces = []
        pass

    def addpiece(self, pieceinit = {}):
        self.pieces.append(piece.Piece(**pieceinit))