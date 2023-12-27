import player
import board
import random

import os
import numpy as np

class randomPlayer(player.player):

    def __init__(self,color) -> None:
        super().__init__(color)
        self.ownWinCount = 0
        self.ownPoint = np.zeros((8,8))
        self.drawCount  = 0

    def getNext(self,currentBoard,color):
        li = currentBoard.getNextCandidate(color)
        position = random.randint(0,len(li)-1)
        return li[position]
    
    def printPoint(self):
        print(board.Board.getColorString(self.ownColor))
        for x in range(0,8):
            for y in range(0,8):
                print (f'{x},{y}={self.ownPoint[x,y]}')

    def incrementWinCount(self):
        self.ownWinCount += 1

    def getWincount(self):
        return self.ownWinCount
    
    def getPoint(self):
        return self.ownPoint

    def save(self,totalCounts):
        if self.ownColor == board.Board.black:
            np.save(os.path.join(self.dataDir,"black."+str(totalCounts)),self.ownPoint)
        elif self.ownColor == board.Board.white:
            np.save(os.path.join(self.dataDir,"white."+str(totalCounts)),self.ownPoint)
    
    def load(self,prefix,suffix):
        pass

    def summarize(self,totalCounts):
        self.ownPoint /= totalCounts

    def setResult(self,black,white,record):
        if self.ownColor == board.Board.black and black > white:
            self.ownWinCount += 1
        if self.ownColor == board.Board.white and black < white:
            self.ownWinCount += 1
        for r in record.getResult():
            x,y,color = r
            if black > white:
                if color == self.ownColor:
                    if color == board.Board.black:
                        self.ownPoint[x][y] += black / (black + white)
                    else:
                        self.ownPoint[x][y] -= white / (black + white)
                else:
                    if color == board.Board.white:
                        self.ownPoint[x][y] -= black / (black + white)
                    else:
                        self.ownPoint[x][y] += white / (black + white)
            if black < white:
                if color == self.ownColor:
                    if color == board.Board.black:
                        self.ownPoint[x][y] -= white / (black + white)
                    else:
                        self.ownPoint[x][y] += black / (black + white)
                else:
                    if color == board.Board.white:
                        self.ownPoint[x][y] += white / (black + white)
                    else:
                        self.ownPoint[x][y] -= black / (black + white)