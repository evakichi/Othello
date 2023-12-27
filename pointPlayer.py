import player
import board
import points

import os
import numpy as np


class pointPlayer(player.player):

    def __init__(self,points) -> None:
        self.points = points.Points(points)
        self.homeDir = os.environ.get('HOME')
        self.dataDir = os.path.join(self.homeDir,'.othellodata')
        if not os.path.exists(self.dataDir)
            os.makedirs(self.dataDir)
    
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
 