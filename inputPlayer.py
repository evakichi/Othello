import board

class inputPlayer:
    def getNext(currentBoard,color):
        li = currentBoard.getNextCandidate(color)
        if not li == None:
            x = int(input('x:'))
            y = int(input('y:'))
            while not currentBoard.isAvailable(x,y,color):
                print ('Err')
                x = int(input('x:'))
                y = int(input('y:'))
        else:
            print("Pass")
        return x,y                
