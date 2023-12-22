import board

class Recorder:
    
    def __init__(self) -> None:
        self.li = list()

    def record (self,pos,color):
        self.li.append((color,)+pos)
    
    def printRetsult (self):
        for i,l in enumerate(self.li):
            color,x,y = l
            print (f'{i + 1} : {board.Board.getColorString(color)} {x},{y}')

    def getResult (self):
        return self.li