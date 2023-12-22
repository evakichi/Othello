import board
import recorder
import points
import pointPlayer
import randomPlayer

blackPoints = points.Points()
whitePoints = points.Points()

pointPlayers = pointPlayer.pointPlayer()
randomPlayers = randomPlayer.randomPlayer()

counter = 1
blackWin = 0
draw = 0
whiteWin = 0

class inputPlayer:
    def getNext(currentBoard,color):
        currentBoard.getEmpty(color)
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
   

for count in range(0,counter):
    mainBoard = board.Board()
    color = mainBoard.white
    record = recorder.Recorder()
#    mainBoard.printBoard()
    while mainBoard.isGameOver(): 
        color = mainBoard.reverse(color)
        if color == mainBoard.black:
            li = mainBoard.getEmpty(color)
            if not li == None:
                x,y = randomPlayers.getNext(mainBoard,color)
                mainBoard.put((x,y),color)
                record.record((x,y),color)
        else:    
            li = mainBoard.getEmpty(color)
            if not li == None:
                x,y = randomPlayers.getNext(mainBoard,color)
                mainBoard.put((x,y),color)
                record.record((x,y),color)
        mainBoard.printBoard()

    black,white =mainBoard.result(count)

    mainBoard.printBoard()
    record.printRetsult()

    if black < white:
        whiteWin += 1
        whitePoint = white/(black+white)
        blackPoint = -1*black/(black+white)
    elif  black > white:
        blackWin += 1
        whitePoint = -1*white/(black+white)
        blackPoint = black/(black+white)
    else:
        draw += 1
        whitePoint = 1.0
        blackPoint = 1.0

    recordList = record.getResult()
    for li in recordList:
        color,x,y = li
        if color == mainBoard.black:
            blackPoints.setPoint(x,y,blackPoint)
        else:
            whitePoints.setPoint(x,y,whitePoint)

print (f'black:{blackWin},white:{whiteWin},draw:{draw}')

#print('black')
#blackPoints.printPoint()
#blackPoints.save("/home/evakichi/othellodata/"+str(counter)+"_black.dat")

#print('white')
#whitePoints.printPoint()
#whitePoints.save("/home/evakichi/othellodata/"+str(counter)+"_white.dat")
