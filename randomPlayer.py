import random
import board

class randomPlayer:

    def __init__(self) -> None:
        pass

    def getNext(self,currentBoard,color):
        li = currentBoard.getEmpty(color)
        position = random.randint(0,len(li)-1)
        return li[position]