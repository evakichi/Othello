import board
import points
import numpy as np


class pointPlayer:

    def __init__(self) -> None:
        self.points=points.Points()
    
    def load(self,prefix,suffix):
        self.points.load(prefix,suffix)

    def getPoint(self,position,color):
        x,y = position
        return self.points.getPoint(x,y,color)
        
    def getNext(self,currentBoard,color):
        li = currentBoard.getNextCandidate(color)
        if not li == None:
            for i,l in enumerate(li):
                if i == 0:
                    maxPosition = l
                    maxPoint = self.getPoint(maxPosition,color)
                elif maxPoint <= self.getPoint(l,color):
                    maxPoint = self.getPoint(l,color)
                    maxPosition=l
        return maxPosition
 