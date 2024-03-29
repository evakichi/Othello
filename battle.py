import board
import recorder
import pointPlayer
import randomPlayer
import inputPlayer
import time
import os
import sys
from multiprocessing import Process, Queue

counter = 1
threads = 1
printFlag = True
debugFlag = False

totalBattles = counter * threads

whitePlayer = randomPlayer.randomPlayer(board.Board.white)   
blackPlayer = randomPlayer.randomPlayer(board.Board.black)   
#blackPlayer = pointPlayer.pointPlayer(board.Board.black)   

#blackPlayer.load(2000)
#blackPlayer.setMaxDepth(3)

def battle(mainBoard,blackPlayer,whitePlayer,queue,count,pFlag=False,dFlag=False):
    currentColor = mainBoard.white
    record = recorder.Recorder()

    if pFlag:
        mainBoard.printBoard()
    while not mainBoard.isGameOver(): 
        currentColor = mainBoard.reverse(currentColor)
        pos = None
        if currentColor == mainBoard.black:
            pos = blackPlayer.getNext(mainBoard,pFlag,dFlag)
            if pFlag:
                if pos == None:
                    print (f'black : Pass!!')                    
                else:
                    x,y = pos
                    print (f'black : put ({x},{y})')
        elif currentColor == mainBoard.white:
            pos = whitePlayer.getNext(mainBoard,pFlag,dFlag)
            if pFlag:
                if pos == None:
                    print (f'white : Pass!!')                    
                else:
                    x,y = pos
                    print (f'white : put ({x},{y})')
                
        if pos != None:
            if not mainBoard.isAvailable(pos,currentColor):
                print("Vioration")
            mainBoard.putNext(pos,currentColor)
            record.record(pos,currentColor)
        else:
            if pFlag:
                if currentColor == mainBoard.black:
                    print (f'black : pass!!')
                elif currentColor == mainBoard.white:
                    print (f'white : pass!!')

        if pFlag:        
            mainBoard.printBoard()

#    if pFlag:
    mainBoard.printResult(count)

    queue.put(mainBoard.result(count)+(record,))

if __name__ =='__main__':
    results = list()
    for count in range(counter):
        mainBoards=list()
        processes = list()
        queue = list()
        for t in range(threads):
            mainBoards.append(board.Board())
            queue.append(Queue())
            processes.append(Process(target=battle,args=(mainBoards[t],blackPlayer,whitePlayer,queue[t],threads*count+t,printFlag,debugFlag)))
        for t in range(threads):
            processes[t].start()
        for t in range(threads):
            processes[t].join()
        for q in queue:
            black,white,record = q.get()
            blackPlayer.setResult(black,white,record)
            whitePlayer.setResult(black,white,record)

    blackPlayer.summarize(totalBattles)
    whitePlayer.summarize(totalBattles)
            #randomPlayerRecorder.setResult(black,white,record.getResult())
#    record.printRetsult()
#    randomPlayerRecorder.setCount(counter*threads)
#    blackPlayer.printPoint()
#    whitePlayer.printPoint()
    blackPlayer.printWinCount()
    whitePlayer.printWinCount()
    blackPlayer.save(totalBattles)
    whitePlayer.save(totalBattles)
#    randomPlayerRecorder.printWinCount()
#    randomPlayerRecorder.save(datadir,str(counter*threads))
