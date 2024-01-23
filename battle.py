import board
import recorder
#import pointPlayer
import randomPlayer
#import inputPlayer
import time
import os
from multiprocessing import Process, Queue

counter = 1000
threads = 1

totalBattles = counter * threads

whitePlayer = randomPlayer.randomPlayer(board.Board.white)   
blackPlayer = randomPlayer.randomPlayer(board.Board.black)   

def battle(mainBoard,blackPlayer,whitePlayer,queue,count,print_board=False):
    currentColor = mainBoard.white
    record = recorder.Recorder()
    altTotal = 0.0
    normalTotal = 0.0
    if print_board:
        mainBoard.printBoard()
    while mainBoard.isGameOver(): 
        currentColor = mainBoard.reverse(currentColor)
        if currentColor == mainBoard.black:
            altStart = time.time()
            li = mainBoard.altGetNextCandidate(currentColor)
            altEnd = time.time()
            altTotal += (altEnd - altStart)

            normalStart = time.time()
            li = mainBoard.getNextCandidate(currentColor)
            normalEnd = time.time()
            normalTotal += (normalEnd - normalStart)

            if not li == None:
                x,y = blackPlayer.getNext(mainBoard,currentColor)
                mainBoard.putNext((x,y),currentColor)
                record.record((x,y),currentColor)
                if print_board:
                    print (f'● : put ({x},{y})')
            else:
                if print_board:
                    print (f'● : pass!!')
        else:    
            altStart = time.time()
            li = mainBoard.altGetNextCandidate(currentColor)
            altEnd = time.time()
            altTotal += (altEnd - altStart)

            normalStart = time.time()
            li = mainBoard.getNextCandidate(currentColor)
            normalEnd = time.time()
            normalTotal += (normalEnd - normalStart)
            
            if not li == None:
                x,y = whitePlayer.getNext(mainBoard,currentColor)
                mainBoard.putNext((x,y),currentColor)
                record.record((x,y),currentColor)
                if print_board:
                    print (f'○ : put ({x},{y})')
            else:
                if print_board:
                    print (f'○ : pass!!')
        if print_board:        
            mainBoard.printBoard()
    if print_board:
        mainBoard.printResult()
    print(f'noemal = {normalTotal}, alt = {altTotal}')
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
