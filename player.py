import board
import recorder
import points
import random
import pointPlayer

blackPoints = points.Points()
whitePoints = points.Points()

counter = 1000000
pointPlayers = pointPlayer.pointPlayer()

counter = 10000
blackWin = 0
draw = 0
whiteWin = 0

for count in range(0,counter):
    MainBoard = board.Board()
    #MainBoard.print()
    color = MainBoard.white
    record = recorder.Recorder()
    while MainBoard.isGameOver(): 
        color = MainBoard.reverse(color)
        if color == MainBoard.black:
            li = MainBoard.getEmpty(color)
            if not li == None:
                for i,l in enumerate(li):
                    if i == 0:
                        maxPosition = l
                        maxPoint = pointPlayers.getPoint(maxPosition,color)
                    elif maxPoint <= pointPlayers.getPoint(l,color):
                        maxPoint = pointPlayers.getPoint(l,color)
                        maxPosition=l
                MainBoard.put(maxPosition,color)
                record.record(maxPosition,color)                
        else:    
            li = MainBoard.getEmpty(color)
    #        MainBoard.printEmptyList(color)
            if not li == None:
                rand = random.randint(0,len(li)-1)
                l = li[rand]
                MainBoard.put(l,color)
                record.record(l,color)

    black,white =MainBoard.result()
    if black < white:
        whiteWin += 1
    elif black > white:
        blackWin += 1
    else:
        draw += 1
    
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

print (f'black:{blackWin},white:{whiteWin},draw:{draw}')

#print('black')
#blackPoints.printPoint()
#blackPoints.save("/home/evakichi/othellodata/"+str(counter)+"_black.dat")

#print('white')
#whitePoints.printPoint()
#whitePoints.save("/home/evakichi/othellodata/"+str(counter)+"_white.dat")
