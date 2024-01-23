import player
import board

import os
import numpy as np


class pointPlayer(player.player):

    def __init__(self,color) -> None:
        super().__init__(color)

    def load(self,iter):
        if self.ownColor == board.Board.white:
            self.ownPoints = np.load(os.path.join(self.homeDir,f'.othellodata/white.{iter}.npy'))
            self.opponentPoints = np.load(os.path.join(self.homeDir,f'.othellodata/black.{iter}.npy'))
        elif self.ownColor == board.Board.black:
            self.ownPoints = np.load(os.path.join(self.homeDir,f'.othellodata/black.{iter}.npy'))
            self.opponentPoints = np.load(os.path.join(self.homeDir,f'.othellodata/white.{iter}.npy'))

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
        
    def getOwnPoint(self,position):
        x,y = position
        return self.ownPoints[x,y]

    def getOpponentPoint(self,position):
        x,y = position
        return self.opponentPoints[x,y]

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
    
    def nodePoint(self,currentBoard,color):
        if color == self.ownColor:
            li = currentBoard.getNextCandidate(self.ownColor)
            if not li == None:
                for i,l in enumerate(li):
                    if i == 0:
                        maxPosition = l
                        maxPoint = self.getOwnPoint(l)
                    elif maxPoint <= self.getOwnPoint(l):
                        maxPoint = self.getOwnPoint(l)
                        maxPosition=l
                return maxPosition
            return None
        else:
            li = currentBoard.getNextCandidate(self.ownColor * -1)
            if not li == None:
                for i,l in enumerate(li):
                    if i == 0:
                        minPosition = l
                        minPoint = self.getOpponentPoint(l)
                    elif minPoint >= self.getOpponentPoint(l):
                        minPoint = self.getOpponentPoint(l)
                        minPosition=l
                return minPosition
            return None



    def minMax(self,currentBoard,maxDepth,currentDepth,color):
        if maxDepth == currentDepth:
            return self.nodePoint(currentBoard,color * -1)
        
    def getNext(self,currentBoard):
        self.minMax(currentBoard,0,0,-1*self.ownColor)

    def setResult(self,black,white,record):
        if self.ownColor == board.Board.black and black > white:
            self.ownWinCount += 1
        if self.ownColor == board.Board.white and black < white:
            self.ownWinCount += 1 