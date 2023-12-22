import board
import recorder
import points
import random

blackPoints = points.Points()
whitePoints = points.Points()
counter = 1000000

for count in range(0,counter):
    MainBoard = board.Board()
    #MainBoard.print()
    color = MainBoard.white
    record = recorder.Recorder()
    while MainBoard.isGameOver(): 
        color = MainBoard.reverse(color)
        li = MainBoard.getEmpty(color)
#        MainBoard.printEmptyList(color)
        if not li == None:
            rand = random.randint(0,len(li)-1)
            x,y = li[rand]
            MainBoard.put(x,y,color)
            record.record((x,y),color)

    black,white =MainBoard.result()
#    record.printRetsult()

    if black < white:
        whitePoint = white/(black+white)
        blackPoint = -1*black/(black+white)
    elif  black > white:
        whitePoint = -1*white/(black+white)
        blackPoint = black/(black+white)
    else:
        whitePoint = 1.0
        blackPoint = 1.0

    recordList = record.getResult()
    for li in recordList:
        color,x,y = li
        if color == MainBoard.black:
            blackPoints.setPoint(x,y,blackPoint)
        else:
            whitePoints.setPoint(x,y,whitePoint)


print('black')
blackPoints.printPoint()
blackPoints.save("/home/evakichi/othellodata/"+str(counter)+"_black.dat")

print('white')
whitePoints.printPoint()
whitePoints.save("/home/evakichi/othellodata/"+str(counter)+"_white.dat")
