import board
import recorder
import points
import pointPlayer
import randomPlayer
import inputPlayer

import os
from multiprocessing import Process, Queue


totalPoints = points.Points()

counter = 5
threads = 10

pointPlayers = pointPlayer.pointPlayer()
#pointPlayers.load("/home/evakichi/othellodata_random_","1000000")
randomPlayers = randomPlayer.randomPlayer()   
inputPlayers = inputPlayer.inputPlayer()

def humanBattle(mainBoard,blackPlayer,whitePlayer,count):
    color = mainBoard.white
    record = recorder.Recorder()
    while mainBoard.isGameOver(): 
        color = mainBoard.reverse(color)
        mainBoard.printBoard()
        if color == mainBoard.black:
            li = mainBoard.getNextCandidate(color)
            if not li == None:
                x,y = blackPlayer.getNext(mainBoard,color)
                mainBoard.put((x,y),color)
                record.record((x,y),color)
        else:    
            li = mainBoard.getNextCandidate(color)
            if not li == None:
                x,y = whitePlayer.getNext(mainBoard,color)
                mainBoard.put((x,y),color)
                record.record((x,y),color)
    return mainBoard.result(count)+(record,)

#humanBattle(board.Board(),inputPlayers,inputPlayers,1)

def comBattle(mainBoard,blackPlayer,whitePlayer,queue,count):
    color = mainBoard.white
    record = recorder.Recorder()
    while mainBoard.isGameOver(): 
        color = mainBoard.reverse(color)
#        mainBoard.printBoard()
        if color == mainBoard.black:
            li = mainBoard.getNextCandidate(color)
            if not li == None:
                x,y = blackPlayer.getNext(mainBoard,color)
                mainBoard.put((x,y),color)
                record.record((x,y),color)
        else:    
            li = mainBoard.getNextCandidate(color)
            if not li == None:
                x,y = whitePlayer.getNext(mainBoard,color)
                mainBoard.put((x,y),color)
                record.record((x,y),color)
    result = mainBoard.result(count)+(record,)
    queue.put(result)

if __name__ =='__main__':
    results = list()
    for count in range(counter):
        mainBoards=list()
        processes = list()
        queue = list()
        for t in range(threads):
            mainBoards.append(board.Board())
            queue.append(Queue())
            processes.append(Process(target=comBattle,args=(mainBoards[t],randomPlayers,randomPlayers,queue[t],threads*count+t)))
        for t in range(threads):
            processes[t].start()
        for t in range(threads):
            processes[t].join()
        for q in queue:
            black,white,record = q.get()
            totalPoints.setResult(black,white,record.getResult())
#    record.printRetsult()
    totalPoints.setCount(counter*threads)
    totalPoints.printPoint()
    totalPoints.printWinCount()
    datadir = os.getcwd()+"/data/random/"
    os.makedirs(datadir)
    totalPoints.save(datadir,str(counter*threads))
