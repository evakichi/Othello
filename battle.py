import board
import recorder
import pointPlayer
import randomPlayer
import inputPlayer
import time
import os
from multiprocessing import Process, Queue

counter = 1000
threads = 1

totalBattles = counter * threads

whitePlayer = randomPlayer.randomPlayer(board.Board.white)   
blackPlayer = pointPlayer.pointPlayer(board.Board.black)   

blackPlayer.load(2000)

def battle(mainBoard,blackPlayer,whitePlayer,queue,count,print_board=False):
    currentColor = mainBoard.white
    record = recorder.Recorder()

    if print_board:
        mainBoard.printBoard()
    while mainBoard.isGameOver(): 
        currentColor = mainBoard.reverse(currentColor)
        p = None
        if currentColor == mainBoard.black:
            p = blackPlayer.getNext(mainBoard)
            if print_board:
                x,y = p
                print (f'black : put ({x},{y})')
        elif currentColor == mainBoard.white:
            p = whitePlayer.getNext(mainBoard)
            if print_board:
                x,y = p
                print (f'white : put ({x},{y})')
                
        if p != None:
            if not mainBoard.isAvailable(p,currentColor):
                print("Vioration")
            mainBoard.putNext(p,currentColor)
            record.record(p,currentColor)
        else:
            if print_board:
                if currentColor == mainBoard.black:
                    print (f'black : pass!!')
                elif currentColor == mainBoard.white:
                    print (f'white : pass!!')

        if print_board:        
            mainBoard.printBoard()

    if print_board:
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
            processes.append(Process(target=battle,args=(mainBoards[t],blackPlayer,whitePlayer,queue[t],threads*count+t,False)))
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
    blackPlayer.printPoint()
    whitePlayer.printPoint()
    blackPlayer.printWinCount()
    whitePlayer.printWinCount()
    blackPlayer.save(totalBattles)
    whitePlayer.save(totalBattles)
#    randomPlayerRecorder.printWinCount()
#    randomPlayerRecorder.save(datadir,str(counter*threads))
