import board

class Recorder:
    
    def __init__(self) -> None:
        self.li = list()

    def record (self,pos,color):
        self.li.append(pos+(color,))
    
    def printRetsult (self):
        for i,l in enumerate(self.li):
            x,y,color = l
            print (f'{i + 1} : {board.Board.getColorString(color)} {x},{y}')

    def getResult (self):
        return self.li