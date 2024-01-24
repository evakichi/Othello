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

    def setMaxDepth(self,depth):
        self.maxDepth = depth

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

    def termiateEvaluate(self,currentBoard,pFlag=False,dFlag=False):
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

    def normalEvaluate(self,currentBoard,pFlag=False,dFlag=False):
        pos = currentBoard.getNextPos()
        if currentBoard.getNextColor() == self.ownColor:
            if dFlag:
                print (f'normalEvaluate(Own):{self.getOwnPoint(pos)}')
            if pos == None:
                return -sys.float_info.max
            return self.getOwnPoint(pos)
        else:
            if dFlag:
                print (f'normalEvaluate(Opp):{self.getOppPoint(pos)}')
            if pos == None:
                return sys.float_info.max
            return self.getOppPoint(pos)
    
    def minSelect(self,currentBoard,depth,position,color,pFlag=False,dFlag=False):

        nextCandidate = currentBoard.getNextCandidate(color)
        pos,point = None,sys.float_info.max

        if nextCandidate == None: 
            if currentBoard.getNextCandidate(-color) == None:        
                if dFlag:
                    print (f'{depth}:{board.Board.getColorString(color)}:return minSelect:{position}:{self.termiateEvaluate(currentBoard)}')
                return position,self.termiateEvaluate(currentBoard,pFlag,dFlag)
            else:
                if dFlag:
                    print (f'pass')
                    currentBoard.printBoard()
                if depth == 0:
                    return position,self.normalEvaluate(currentBoard.copyNextPass(color),pFlag,dFlag)
                else:
                    return self.maxSelect(currentBoard.copyNextPass(color),depth -1,position,-color,pFlag,dFlag)
            

        if depth == 0:
            for i,nc in enumerate(nextCandidate):
                v = self.normalEvaluate(currentBoard.copyAndNext(nc,color),pFlag,dFlag)
                if dFlag:
                    print (f'{depth}:{board.Board.getColorString(color)}:minSelect:{position}:{nc}:{v}')
                if i == 0  or v < point:
                    pos,point = position,v
            if dFlag:
                print (f'{depth}:{board.Board.getColorString(color)}:return minSelect:{position}:{point}')
            return pos,point

        for i,nc in enumerate(nextCandidate):
            p,v = self.maxSelect(currentBoard.copyAndNext(nc,color),depth -1,position,-color,pFlag,dFlag)
            if dFlag:
                print (f'{depth}:{board.Board.getColorString(color)}:minSelect:{position}:{v}')
            if i == 0 or point > v:
                pos,point = p,v
        if dFlag:
            print (f'{depth}:{board.Board.getColorString(color)}:return minSelect:{pos}:{point}')
        return pos,point

    
    def maxSelect(self,currentBoard,depth,position,color,pFlag=False,dFlag=False):

        nextCandidate = currentBoard.getNextCandidate(color)
        pos,point = None,-sys.float_info.max

        if nextCandidate == None:
            if currentBoard.getNextCandidate(-color) == None:        
                if dFlag:
                    print (f'{depth}:{board.Board.getColorString(color)}:return maxSelect:{position}:{self.termiateEvaluate(currentBoard)}')
                return position,self.termiateEvaluate(currentBoard)
            else:
                if dFlag:
                    print(f'pass')
                    currentBoard.printBoard
                if depth == 0:
                    return position,self.normalEvaluate(currentBoard.copyNextPass(color),pFlag,dFlag)
                else:
                    return self.minSelect(currentBoard.copyNextPass(color),depth -1,position,-color,pFlag,dFlag)
            
        if depth == 0:
            for i,nc in enumerate(nextCandidate):
                v = self.normalEvaluate(currentBoard.copyAndNext(nc,color),pFlag,dFlag)
                if dFlag:
                    print (f'{depth}:{board.Board.getColorString(color)}:maxSelect:{position}:{nc}:{v}')
                if i == 0  or v > point:
                    pos,point = position,v
            if dFlag:
                print (f'{depth}:{board.Board.getColorString(color)}:return maxSelect:{pos}:{point}')
            return pos,point

        for i,nc in enumerate(nextCandidate):
            p,v = self.minSelect(currentBoard.copyAndNext(nc,color),depth -1,position,-color,pFlag,dFlag)
            if dFlag:
                print (f'{depth}:{board.Board.getColorString(color)}:maxSelect:{position}:{v}')
            if i == 0 or point < v:
                pos,point = p,v            
        if dFlag:
            print (f'{depth}:{board.Board.getColorString(color)}:return maxSelect:{pos}:{point}')
        return pos,point

    def minMax(self,currentBoard,depth,color,pFlag=False,dFlag=False):
        nextCandidate = currentBoard.getNextCandidate(color)
        pos,point = None,-sys.float_info.max

        if nextCandidate == None:            
            return None
            
        if depth == 0:
            for i,nc in enumerate(nextCandidate):
                v = self.normalEvaluate(currentBoard.copyAndNext(nc,color),pFlag,dFlag)
                if dFlag:
                    print (f'{depth}:{board.Board.getColorString(color)}:minMax:{nc}:{v}')
                if i == 0  or v > point:
                    pos,point = nc,v
            if dFlag:
                print (f'{depth}:{board.Board.getColorString(color)}:return minMax:{pos}:{point}')
            return pos

        if nextCandidate != None:
            p,v = None,-sys.float_info.max
            for i,nc in enumerate(nextCandidate):
                if nc != None:
                    p,v = self.minSelect(currentBoard.copyAndNext(nc,color),depth -1,nc,-color,pFlag,dFlag)
                if i == 0 or v > point:
                    pos,point = (p,v)
        if dFlag:
            print (f'{depth}:{board.Board.getColorString(color)}:return minMax:{pos}:{point}')
        return pos
    
    def getNext(self,currentBoard,pFlag=False,dFlag=False):
        pos = self.minMax(currentBoard,self.maxDepth,self.ownColor,pFlag,dFlag)
        if dFlag:
            print("\n\n")
        if pos == None:
            return None
        return pos

    def setResult(self,black,white,record):
        if self.ownColor == board.Board.black and black > white:
            self.ownWinCount += 1
        if self.ownColor == board.Board.white and black < white:
            self.ownWinCount += 1 