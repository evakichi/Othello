import numpy as np
import board
import os
import recorder

class Points:

    def __init__(self) -> None:
        self.blackCount = 0
        self.blackPoint = np.zeros((8,8))
        self.whiteCount = 0
        self.whitePoint = np.zeros((8,8))
        self.drawCount  = 0

    def printPoint(self):
        for x in range(0,8):
            for y in range(0,8):
                print (f'{x},{y}={self.blackPoint[x,y]},{self.whitePoint[x,y]}')

    def printWinCount(self):
        print (f'total {self.drawCount+self.blackCount+self.whiteCount}, black:{self.blackCount}, white{self.whiteCount}, draw:{self.drawCount}')

    def getPoint(self,x,y,color):
        if color == board.Board.black:
            return self.blackPoint[x][y]
        elif color == board.Board.white:
            return self.whitePoint[x][y]
    
    def save(self,prefix,suffix):
        np.save(os.path.join(prefix,suffix+"_black"),self.blackPoint)
        np.save(os.path.join(prefix,suffix+"_white"),self.whitePoint)
    
    def load(self,prefix,suffix):
        self.blackPoint = np.load(os.path.join(prefix,suffix+"_black.npy"))
        self.whitePoint = np.load(os.path.join(prefix,suffix+"_white.npy"))

    def setCount(self,count):
        self.blackPoint /= count
        self.whitePoint /= count

    def setResult(self,black,white,record):
        if black < white:
            self.whiteCount += 1
            for r in record:
                x,y,color = r
                if color == board.Board.white:
                    self.whitePoint[x][y] += white/(black+white)
                else:
                    self.blackPoint[x][y] -= black/(black+white)
            return board.Board.white
        elif  black > white:
            self.blackCount += 1
            for r in record:
                x,y,color = r
                if color == board.Board.white:
                    self.whitePoint[x][y] -= white/(black+white)
                else:
                    self.blackPoint[x][y] += black/(black+white)
            return board.Board.black
        else:
            self.drawCount += 1
            for r in record:
                x,y,color = r
                if color == board.Board.white:
                    self.whitePoint[x][y] += white/(black+white)
                else:
                    self.blackPoint[x][y] += black/(black+white)
            return board.Board.empty