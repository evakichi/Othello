import player
import board

import os
import numpy as np


class pointPlayer(player.player):

    def __init__(self,color) -> None:
        super().__init__(color)

    def load(self,iter):
        if self.ownColor == board.Board.white:
            self.points = np.load(os.path.join(self.homeDir,f'.othellodata/white.{iter}.npy'))
        elif self.ownColor == board.Board.black:
            self.points = np.load(os.path.join(self.homeDir,f'.othellodata/black.{iter}.npy'))

    def save(self,iter):
        pass

    def printPoint(self):
        pass

    def printWinCount(self):
        print(board.Board.getColorString(self.ownColor)+":"+str(self.getWinCount()))

    def incrementWinCount(self):
        self.ownWinCount += 1

    def getWinCount(self):
        return self.ownWinCount
    
    def getPoint(self):
        pass
    
    def summarize(self,totalCounts):
        pass 

    def getPoint(self):
        pass
        
    def getPoint(self,position):
        x,y = position
        return self.points[x,y]
        
    def getNext(self,currentBoard):
        nextBoard = currentBoard.copy()
        li = nextBoard.getNextCandidate(self.ownColor)
        if not li == None:
            for i,l in enumerate(li):
                if i == 0:
                    maxPosition = l
                    maxPoint = self.getPoint(maxPosition)
                elif maxPoint <= self.getPoint(l):
                    maxPoint = self.getPoint(l)
                    maxPosition=l
            return maxPosition
        return None
    
    def setResult(self,black,white,record):
        if self.ownColor == board.Board.black and black > white:
            self.ownWinCount += 1
        if self.ownColor == board.Board.white and black < white:
            self.ownWinCount += 1 