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

    def termiateEvaluate(self,currentBoard,pFlag=False):
        color = currentBoard.getNextColor()
        black,white = currentBoard.result(0)
        if color == currentBoard.black: 
            if black > white:
                return 1.0
            if white > black:
                return -1.0
            else:
                return 0.0
        if color == currentBoard.white: 
            if black < white:
                return 1.0
            if white < black:
                return -1.0
            else:
                return 0.0

    def normalEvaluate(self,currentBoard,pFlag=False):
        pos = currentBoard.getNextPos()
        if currentBoard.getNextColor() == self.ownColor:
            return self.getOwnPoint(pos)
        else:
            return self.getOppPoint(pos)
    
    def minSelect(self,currentBoard,depth,position,color,pFlag=False):

        nextCandidate = currentBoard.getNextCandidate(color)
        pos,point = None,sys.float_info.max

        if nextCandidate == None:        
            if pFlag:
                print (f'{depth}:{board.Board.getColorString(color)}:return minSelect:{position}:{self.termiateEvaluate(currentBoard)}\n')
            return position,self.termiateEvaluate(currentBoard,pFlag)

        if depth == 0:
            for i,nc in enumerate(nextCandidate):
                v = self.normalEvaluate(currentBoard.copyAndNext(nc,color),pFlag)
                if pFlag:
                    print (f'{depth}:{board.Board.getColorString(color)}:minSelect:{position}:{nc}:{v}')
                if i == 0  or v < point:
                    pos,point = position,v
            if pFlag:
                print (f'{depth}:{board.Board.getColorString(color)}:return minSelect:{position}:{point}\n')
            return pos,point

        for i,nc in enumerate(nextCandidate):
            position,v = self.maxSelect(currentBoard.copyAndNext(nc,color),depth -1,position,-color,pFlag)
            if pFlag:
                print (f'{depth}:{board.Board.getColorString(color)}:minSelect:{position}:{v}')
            if i == 0 or point > v:
                pos,point = position,v
        if pFlag:
            print (f'{depth}:{board.Board.getColorString(color)}:return minSelect:{pos}:{point}\n')
        return position,point

    
    def maxSelect(self,currentBoard,depth,position,color,pFlag=False):

        nextCandidate = currentBoard.getNextCandidate(color)
        pos,point = None,-sys.float_info.max

        if nextCandidate == None:        
            if pFlag:
                print (f'{depth}:{board.Board.getColorString(color)}:return maxSelect:{position}:{self.termiateEvaluate(currentBoard)}\n')
            return position,self.termiateEvaluate(currentBoard)
            
        if depth == 0:
            for i,nc in enumerate(nextCandidate):
                v = self.normalEvaluate(currentBoard.copyAndNext(nc,color),pFlag)
                if pFlag:
                    print (f'{depth}:{board.Board.getColorString(color)}:maxSelect:{position}:{nc}:{v}')
                if i == 0  or v > point:
                    pos,point = position,v
            if pFlag:
                print (f'{depth}:{board.Board.getColorString(color)}:return maxSelect:{pos}:{point}\n')
            return pos,point

        for i,nc in enumerate(nextCandidate):
            p,v = self.minSelect(currentBoard.copyAndNext(nc,color),depth -1,position,-color,pFlag)
            if pFlag:
                print (f'{depth}:{board.Board.getColorString(color)}:maxSelect:{p}:{v}')
            if i == 0 or point < v:
                pos,point = p,v            
        print (f'{depth}:{board.Board.getColorString(color)}:return maxSelect:{pos}:{point}\n')
        return position,point

    def minMax(self,currentBoard,depth,color,pFlag=False):
        nextCandidate = currentBoard.getNextCandidate(color)
        pos,point = None,-sys.float_info.max

        if nextCandidate == None:
            return None
            
        if depth == 0:
            for i,nc in enumerate(nextCandidate):
                v = self.normalEvaluate(currentBoard.copyAndNext(nc,color),pFlag)
                if pFlag:
                    print (f'{depth}:{board.Board.getColorString(color)}:minMax:{nc}:{v}')
                if i == 0  or v > point:
                    pos,point = nc,v
            if pFlag:
                print (f'{depth}:{board.Board.getColorString(color)}:return minMax:{pos}:{point}\n')
            return pos

        if nextCandidate != None:
            for i,nc in enumerate(nextCandidate):
                p,v = self.minSelect(currentBoard.copyAndNext(nc,color),depth -1,nc,-color,pFlag)
                if i == 0 or v > point:
                    pos,point = (p,v)
        if pFlag:
            print (f'{depth}:{board.Board.getColorString(color)}:return minMax:{pos}:{point}\n')
        return pos
    
    def getNext(self,currentBoard,pFlag=False):
        pos = self.minMax(currentBoard,2,self.ownColor,pFlag)
        if pFlag:
            print("\n\n\n\n\n\n\n\n")
        if pos == None:
            return None
        return pos

    def setResult(self,black,white,record):
        if self.ownColor == board.Board.black and black > white:
            self.ownWinCount += 1
        if self.ownColor == board.Board.white and black < white:
            self.ownWinCount += 1 