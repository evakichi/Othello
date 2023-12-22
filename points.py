import recorder
import numpy as np

class Points:

    def __init__(self) -> None:
        self.point = np.zeros((8,8))

    def printPoint(self):
        for x in range(0,8):
            for y in range(0,8):
                print (f'{x},{y}={self.point[x][y]}')

    def getPoint(self,x,y):
        return self.point[x][y]

    def setPoint(self,x,y,point):
        self.point[x][y] += point
    
    def save(self,fname):
        np.save(fname,self.point)