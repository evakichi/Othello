import player
import board

class inputPlayer(player.player):
    def __init__(self):
        pass

    def getNext(self,currentBoard,color):
        if color == board.Board.white:
            print ('input:○')
        else:
            print ('input:●')
        li = currentBoard.getNextCandidate(color)
        if not li == None:
            xInput = input('x:')
            try:
                x = int(xInput)
            except Exception as e:
                print (e)
                x = -1
            yInput = input('y:')
            try:
                y = int(yInput)
            except Exception as e:
                print (e)
                y = -1
            while not currentBoard.isAvailable(x,y,color):
                print ('Err')
                xInput = input('x:')
                try:
                    x = int(xInput)
                except Exception as e:
                    print (e)
                    x = -1
                yInput = input('y:')
                try:
                    y = int(yInput)
                except Exception as e:
                    print (e)
                    y = -1
        else:
            print("Pass")
        return x,y                
