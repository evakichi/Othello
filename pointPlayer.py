import player
import board
import points

import os
import numpy as np


class pointPlayer(player.player):

    def __init__(self) -> None:
        pass
    
    def setTotalBattles(self,totalBattles):
        self.points = points.Points(totalBattles)


    def load(self):
        self.points.load(os.path.join(self.homeDir,f'.othellodata/{self.points}.dat'))

    def save(self):
        self.points.save(os.path.join(self.homeDir,f'.othellodata/{self.points}.dat'))

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
 