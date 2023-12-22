import board
import numpy as np

class pointPlayer:

    def __init__(self) -> None:
        self.blackPoints = np.load("/home/evakichi/othellodata/1000000_black.dat.npy")
        self.whitePoints = np.load("/home/evakichi/othellodata/1000000_white.dat.npy")

    def getPoint(self,position,color):
        x,y = position
        if color == board.Board.black:
            return self.blackPoints[x,y]
        else:
            return self.whitePoints[x,y]