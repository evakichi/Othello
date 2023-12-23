import board
import recorder
import points
import pointPlayer
import randomPlayer
import inputPlayer

totalPoints = points.Points()

counter = 1

pointPlayers = pointPlayer.pointPlayer()
pointPlayers.load("/home/evakichi/othellodata","100000")
randomPlayers = randomPlayer.randomPlayer()   
inputPlayers = inputPlayer.inputPlayer()

for count in range(0,counter):
    mainBoard = board.Board()
    color = mainBoard.white
    record = recorder.Recorder()
    while mainBoard.isGameOver(): 
        color = mainBoard.reverse(color)
        mainBoard.printBoard()
        if color == mainBoard.black:
            li = mainBoard.getNextCandidate(color)
            if not li == None:
                x,y = pointPlayers.getNext(mainBoard,color)
                mainBoard.put((x,y),color)
                record.record((x,y),color)
        else:    
            li = mainBoard.getNextCandidate(color)
            if not li == None:
                x,y = inputPlayer.inputPlayer.getNext(mainBoard,color)
                mainBoard.put((x,y),color)
                record.record((x,y),color)

    black,white =mainBoard.result(count)
#    record.printRetsult()
    recordList = record.getResult()
    totalPoints.setResult(black,white,recordList)
totalPoints.printPoint()
totalPoints.printWinCount()
#totalPoints.save("/home/evakichi/othellodata",str(counter))
