import player
import board
import random

class randomPlayer(player.player):

    def __init__(self) -> None:
        pass

    def getNext(self,currentBoard,color):
        li = currentBoard.getNextCandidate(color)
        position = random.randint(0,len(li)-1)
        return li[position]