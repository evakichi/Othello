import board
import random

MainBoard = board.Board()
MainBoard.print()
color = MainBoard.white

while MainBoard.isGameOver(): 
    color = MainBoard.reverse(color)
    li = MainBoard.getEmpty(color)
    MainBoard.printEmptyList(color)
    if not li == None:
        rand = random.randint(0,len(li)-1)
        x,y = li[rand]
        MainBoard.put(x,y,color)

