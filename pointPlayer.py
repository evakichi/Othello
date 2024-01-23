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
            self.oppPoints = np.load(os.path.join(self.homeDir,f'.othellodata/black.{iter}.npy'))
        elif self.ownColor == board.Board.black:
            self.ownPoints = np.load(os.path.join(self.homeDir,f'.othellodata/black.{iter}.npy'))
            self.oppPoints = np.load(os.path.join(self.homeDir,f'.othellodata/white.{iter}.npy'))

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

    def getOppPoint(self,position):
        if position == None:
            return None
        x,y = position
        return self.oppPoints[x,y]

    def nodePoint(self,currentBoard):
        pos = currentBoard.getNextPos()
        if currentBoard.getNextColor() == self.ownColor:
            return self.getOwnPoint(pos)
        else:
            return self.getOppPoint(pos)

    def minMax(self,currentBoard,maxDepth,currentDepth,p,color):

        nextCandidate = currentBoard.getNextCandidate(color)

        if currentDepth == 0 and nextCandidate == None:
            return None
        
        if currentDepth == 0:
            maxPos = nextCandidate[0]
            nextBoard = currentBoard.copyAndNext(maxPos,color)
            maxPoint = self.nodePoint(nextBoard)
            for nc in nextCandidate:
                nextBoard = currentBoard.copyAndNext(nc,color)
                mm = self.minMax(nextBoard,maxDepth,currentDepth + 1,nc,color)
                if mm != None and mm[1] > maxPoint:
                    maxPos,maxPoint = mm      
            return maxPos,maxPoint

        if currentDepth == maxDepth:
            return p,self.nodePoint(currentBoard)

        if currentBoard.isGameOver():
            black,white = currentBoard.result(0)
            if color == currentBoard.black: 
                if black > white:
                    return p,1.0
                if white > black:
                    return p,-1.0
                else:
                    return p,0.0
            if color == currentBoard.white: 
                if black < white:
                    return p,1.0
                if white < black:
                    return p,-1.0
                else:
                    return p,0.0

        pos = (-1,-1)
        point = sys.float_info.max

        if nextCandidate != None:
            nextBoard = currentBoard.copyAndNext(nextCandidate[0],color)
            pos,point = (nextCandidate[0],self.nodePoint(nextBoard))
        else:
            if color == self.ownColor:
                point = -1 * point

        if nextCandidate != None:
            for nc in nextCandidate:
                nextBoard = currentBoard.copyAndNext(nc,color)
                mm = self.minMax(nextBoard,maxDepth,currentDepth + 1,p,color * -1)
                if mm != None and color == self.ownColor and mm[1] > point:
                    pos,point = mm
                if mm != None and color != self.ownColor and mm[1] < point:
                    pos,point = mm
            return pos,point
        return p,point


    def getNext(self,currentBoard):
        m = self.minMax(currentBoard,1,0,(-1,-1),self.ownColor)
        if m == None:
            return None
        return m[0]

    def setResult(self,black,white,record):
        if self.ownColor == board.Board.black and black > white:
            self.ownWinCount += 1
        if self.ownColor == board.Board.white and black < white:
            self.ownWinCount += 1 