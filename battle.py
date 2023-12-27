import board
import recorder
import points
import player
import pointPlayer
import randomPlayer
import inputPlayer

import os
from multiprocessing import Process, Queue


totalPoints = points.Points()

counter = 5
threads = 1

currentPoints = 10000000

pointPlayers = pointPlayer.pointPlayer(currentPoints)
#pointPlayers.load("/home/evakichi/othellodata_random_","1000000")
randomPlayers = randomPlayer.randomPlayer()   
inputPlayers = inputPlayer.inputPlayer()


def battle(mainBoard,blackPlayer,whitePlayer,queue,count,print_board=False):
    currentColor = mainBoard.white
    record = recorder.Recorder()
    if print_board:
        mainBoard.printBoard()
    while mainBoard.isGameOver(): 
        currentColor = mainBoard.reverse(currentColor)
        if currentColor == mainBoard.black:
            li = mainBoard.getNextCandidate(currentColor)
            if not li == None:
                x,y = blackPlayer.getNext(mainBoard,currentColor)
                mainBoard.put((x,y),currentColor)
                record.record((x,y),currentColor)
                if print_board:
                    print (f'● : put ({x},{y})')
            else:
                if print_board:
                    print (f'● : pass!!')
        else:    
            li = mainBoard.getNextCandidate(currentColor)
            if not li == None:
                x,y = whitePlayer.getNext(mainBoard,currentColor)
                mainBoard.put((x,y),currentColor)
                record.record((x,y),currentColor)
                if print_board:
                    print (f'○ : put ({x},{y})')
            else:
                if print_board:
                    print (f'○ : pass!!')
        if print_board:        
            mainBoard.printBoard()
    queue.put(mainBoard.result(count)+(record,))


battle(board.Board(),inputPlayers,inputPlayers,Queue(),0,print_board=True)

if __name__ =='__main__':
    results = list()
    for count in range(counter):
        mainBoards=list()
        processes = list()
        queue = list()
        for t in range(threads):
            mainBoards.append(board.Board())
            queue.append(Queue())
            processes.append(Process(target=battle,args=(mainBoards[t],inputPlayers,randomPlayers,queue[t],threads*count+t)))
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
    os.makedirs(datadir,exist_ok=True)
    totalPoints.save(datadir,str(counter*threads))
