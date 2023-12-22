import random


class Board:
    black = -1
    white = 1
    empty = 0

    def __init__(self) -> None:
        self.board = [[ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 1,-1, 0, 0, 0],
                [ 0, 0, 0,-1, 1, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]]

    def reverse(self,color):
        return -1*color
    
    def getColorString(color):
        if color == -1:
            return '○'
        elif color == 1:
            return '●'
        else:
            return '-'

    def printBoard(self):
        print (" ",end="")
        for j in range(0,8):
            print (f'|{j}',end="")
        print ("|")
        for i in range(0,8):
            print (f'{i}',end="")
            for j in range(0,8):
                if self.board[i][j]==self.black:
                    print ("|○",end="")
                elif self.board[i][j]==self.white:
                    print ("|●",end="")
                else:
                    print ("| ",end="")
            print ("|")


    def get (self,x,y):
        return self.board[x][y]

    def isAvailable(self,x,y,color):
        
        if not self.board[x][y] == self.empty:
            return False
        
        for xi in range(x + 1,8):
            if self.get(xi,y) == self.reverse(color):
                continue
            elif self.get(xi,y) == color and xi > x+1 and xi < 8:
                return True
            else:
                break
        
        for xi in range(x - 1,-1,-1):
            if self.get(xi,y) == self.reverse(color):
                continue
            elif self.get(xi,y) == color and xi < x-1 and xi >=0:
                return True
            else:
                break
        
        for yi in range(y + 1,8):
            if self.get(x,yi) == self.reverse(color):
                continue
            elif self.get(x,yi) == color and yi > y+1 and yi < 8:
                return True
            else:
                break
        
        for yi in range(y - 1,-1,-1):
            if self.get(x,yi) == self.reverse(color):
                continue
            elif self.get(x,yi) == color and yi < y-1 and yi >=0:
                return True
            else:
                break
        
        flag = False
        for xi in range(x + 1,8):
            for yi in range(y + 1,8):
                if xi - x == yi - y and self.get(xi,yi) == self.reverse(color):
                    continue
                elif xi - x == yi - y and self.get(xi,yi) == color and xi > x + 1 and xi < 8 and yi > y + 1 and yi < 8:
                    return True
                elif  xi - x == yi - y:
                    flag = True
                    break
            if  flag:
                break
        
        flag = False
        for xi in range(x - 1,-1,-1):
            for yi in range(y - 1,-1,-1):
                if x - xi == y - yi and self.get(xi,yi) == self.reverse(color):
                    continue
                elif x - xi == y - yi and self.get(xi,yi) == color and xi < x - 1 and xi >=0 and yi < y - 1 and yi >=0:
                    return True
                elif  x - xi == y - yi:
                    flag = True
                    break
            if  flag:
                break
        
        flag = False
        for xi in range(x - 1,-1,-1):
            for yi in range(y + 1,8):
                if x - xi == yi - y and self.get(xi,yi) == self.reverse(color):
                    continue
                elif x - xi == yi - y and self.get(xi,yi) == color and xi < x - 1 and xi >= 0 and yi > y + 1 and yi < 8:
                    return True
                elif  x - xi == yi - y:
                    flag = True
                    break
            if  flag:
                break

        flag = False
        for xi in range(x + 1,8):
            for yi in range(y - 1,-1,-1):
                if xi - x == y - yi and self.get(xi,yi) == self.reverse(color):
                    continue
                elif xi - x == y - yi and self.get(xi,yi) == color and xi > x + 1 and xi < 8 and yi < y - 1 and yi >=0:
                    return True
                elif  xi - x == y - yi:
                    flag = True
                    break
            if  flag:
                break

        return False

    def getEmpty(self,color):
        l = list()
        for x in range(0,8):
            for y in range(0,8):
                if self.isAvailable(x,y,color):
                    l.append((x,y))
        if len(l) == 0:
            return None
        return l
            
    def printEmptyList(self,color):
        li = self.getEmpty(color)
        if not li == None:
            for l in li:
                print (f'{l}')


    def printRecord(self,x,y,color):
        if color == self.black:
            print (f'○:put{x},{y}')
        else:
            print (f'●:put{x},{y}')

    def put(self,x,y,color):
        if self.isAvailable(x,y,color):
            self.board[x][y] = color
#            self.printRecord(x,y,color)
            for i in range(x+1,8):
                if self.get(i,y) == self.reverse(color):
                    continue
                elif self.get(i,y) == color:
                    for ii in range(x+1,i):
                        self.board[ii][y]=color
                    break
                else:
                    break

            for i in range(x-1,-1,-1):
                if self.get(i,y) == self.reverse(color):
                    continue
                elif self.get(i,y) == color:
                    for ii in range(x-1,i-1,-1):
                        self.board[ii][y]=color
                    break
                else:
                    break

            for i in range(y+1,8):
                if self.get(x,i) == self.reverse(color):
                    continue
                elif self.get(x,i) == color:
                    for ii in range(y+1,i):
                        self.board[x][ii]=color
                    break
                else:
                    break

            for i in range(y-1,-1,-1):
                if self.get(x,i) == self.reverse(color):
                    continue
                elif self.get(x,i) == color:
                    for ii in range(y-1,i-1,-1):
                        self.board[x][ii]=color
                    break
                else:
                    break

            flag = False
            for xi in range(x + 1,8):
                for yi in range(y + 1,8):
                    if xi - x == yi - y and self.get(xi,yi) == self.reverse(color):
                        continue
                    elif xi - x == yi - y and self.get(xi,yi) == color:
                        flag = True
                        for xii in range(x+1,xi):
                            for yii in range(y+1,yi):
                                if xii - x == yii - y:
                                    self.board[xii][yii]=color
                        break
                    else:
                        flag = True
                        break
                if flag:
                    break

            flag = False
            for xi in range(x - 1,-1,-1):
                for yi in range(y - 1,-1,-1):
                    if x - xi == y - yi and self.get(xi,yi) == self.reverse(color):
                        continue
                    elif x - xi == y - yi and self.get(xi,yi) == color:
                        flag = True
                        for xii in range(x - 1 ,xi - 1,-1):
                            for yii in range( y - 1,yi - 1,-1):
                                if x - xii == y - yii:
                                    self.board[xii][yii]=color
                        break
                    else:
                        flag = True
                        break
                if flag:
                    break

            flag = False
            for xi in range(x - 1,-1,-1):
                for yi in range(y + 1,8):
                    if x - xi == yi - y and self.get(xi,yi) == self.reverse(color):
                        continue
                    elif x - xi == yi - y and self.get(xi,yi) == color:
                        flag = True
                        for xii in range(x - 1,xi - 1,-1):
                            for yii in range(y + 1,yi):
                                if x - xii == yii - y:
                                    self.board[xii][yii]=color
                        break
                    else:
                        flag = True
                        break
                if flag:
                    break

            flag = False
            for xi in range(x+1,8):
                for yi in range(y - 1,-1,-1):
                    if xi - x == y - yi and self.get(xi,yi) == self.reverse(color):
                        continue
                    elif xi - x == y - yi and self.get(xi,yi) == color:
                        flag = True
                        for xii in range(x + 1 ,xi):
                            for yii in range( y - 1,yi - 1,-1):
                                if xii - x == y - yii:
                                    self.board[xii][yii]=color
                        break
                    else:
                        flag = True
                        break
                if flag:
                    break

#            self.printBoard()
        else:
            print("Err!!")

    def isGameOver(self):
      return not self.getEmpty(self.black) == None or not self.getEmpty(self.white) == None
    
    def result(self):
        white = 0
        black = 0
        for x in range(0,8):
            for y in range(0,8):
                if self.board[x][y]==self.black:
                    black += 1
                elif self.board[x][y]==self.white:
                    white += 1
        print (f'black = {black}, white = {white}')
        if white == black:
            print ("draw")
        elif white > black:
            print ("white win")
        else:
            print ("black win")
        return black,white
