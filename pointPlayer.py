import player
import board
import sys
import os
import numpy as np
import time

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
        if position == None:
            return None
        x,y = position
        return self.ownPoints[x,y]

    def getOpponentPoint(self,position):
        if position == None:
            return None
        x,y = position
        return self.opponentPoints[x,y]

    def nodePoint(self,currentBoard):
        if currentBoard.getNextColor() == self.ownColor:
            return self.getOwnPoint(currentBoard.getNextPos())
        else:
            return self.getOpponentPoint(currentBoard.getNextPos())

    def minMax(self,currentBoard,maxDepth,currentDepth,p,color):

        nextCandidate = currentBoard.getNextCandidate(color)

        if currentDepth == 0 and nextCandidate == None:
            return None
        
        if currentDepth == 0:
            maxPos = nextCandidate[0]
            nextBoard = currentBoard.copy()
            nextBoard.putNext(maxPos,color)
            maxPoint = self.nodePoint(nextBoard)
            for nc in nextCandidate:
                nextBoard = currentBoard.copy()
                nextBoard.putNext(nc,color)
                mm = self.minMax(nextBoard,maxDepth,currentDepth + 1,nc,color)
                if mm != None and mm[1] > maxPoint:
                    maxPos,maxPoint = mm      
            print (maxPos,maxPoint)
            return maxPos,maxPoint

        if currentDepth == maxDepth:
            return p,self.nodePoint(currentBoard)

        if color == self.ownColor:
            maxPos = (-1,-1)
            maxPoint = -1*sys.float_info.max
            if nextCandidate != None:
                for nc in nextCandidate:
                    nextBoard = currentBoard.copy()
                    nextBoard.putNext(nc,color)
                    mm = self.minMax(nextBoard,maxDepth,currentDepth + 1,p,color * -1)
                    if mm != None and mm[1] > maxPoint:
                        maxPos,maxPoint = mm
                return maxPos,maxPoint
            return p,maxPoint
        
        if color != self.ownColor:
            minPos = (-1,-1)
            minPoint = sys.float_info.max
            if nextCandidate != None:
                for nc in nextCandidate:
                    nextBoard = currentBoard.copy()
                    nextBoard.putNext(nc,color)
                    mm = self.minMax(nextBoard,maxDepth,currentDepth + 1,p,color * -1)
                    if mm != None and mm[1] <= minPoint:
                        minPos,minPoint = mm
                return minPos,minPoint
            return p,minPoint
        
    def getNext(self,currentBoard):
        m = self.minMax(currentBoard,6,0,(-1,-1),self.ownColor)
        if m == None:
            return None
        return m[0]

    def setResult(self,black,white,record):
        if self.ownColor == board.Board.black and black > white:
            self.ownWinCount += 1
        if self.ownColor == board.Board.white and black < white:
            self.ownWinCount += 1 