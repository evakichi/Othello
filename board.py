import random


class Board:
    black = -1
    white = 1
    empty = 0

    def __init__(self) -> None:
        self.board = [
            [ 0, 0, 0, 0, 0, 0, 0, 0],
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
        if color == Board.black:
            return '●'
        elif color == Board.white:
            return '○'
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
                    print ("|●",end="")
                elif self.board[i][j]==self.white:
                    print ("|○",end="")
                else:
                    print ("| ",end="")
            print ("|")


    def get (self,x,y):
        return self.board[x][y]

    def altIsAvailable(self,x,y,color):
        if not self.board[x][y] == self.empty:
            return False

        if x < 6 and self.board[x + 1][y] == self.reverse(color):
            for e in range(2, 8 - x):
                if self.board[x + e][y] == self.reverse(color):
                    continue
                elif self.board[x + e][y] == color:
                    return True
                else:
                    break

        if x > 1 and self.board[x - 1][y] == self.reverse(color):
            for e in range(2, x + 1):
                if self.board[x - e][y] == self.reverse(color):
                    continue
                elif self.board[x - e][y] == color:
                    return True
                else:
                    break

        if y < 6 and self.board[x][y + 1] == self.reverse(color):
            for e in range(2, 8 - y):
                if self.board[x][y + e] == self.reverse(color):
                    continue
                elif self.board[x][y + e] == color:
                    return True
                else:
                    break

        if y > 1 and self.board[x][y - 1] == self.reverse(color):
            for e in range(2, y + 1):
                if self.board[x][y - e] == self.reverse(color):
                    continue
                elif self.board[x][y - e] == color:
                    return True
                else:
                    break


        xMax = max(x,8 - x)
        xMin = min(x,8 - x)
        yMax = max(y,8 - y)
        yMin = min(y,8 - y)

        maxValue = max(x,y)
        if maxValue < 6 and self.board[x + 1][y + 1] == self.reverse(color):
            for e in range(2, 8 - maxValue):
                if self.board[x + e][y + e] == self.reverse(color):
                    continue
                elif self.board[x + e][y + e] == color:
                    return True
                else:
                    break

        maxValue = max(x,7 - y)
        if maxValue < 6 and self.board[x + 1][y + 1] == self.reverse(color):
            for e in range(2, 8 - maxValue):
                if self.board[x + e][y + e] == self.reverse(color):
                    continue
                elif self.board[x + e][y + e] == color:
                    return True
                else:
                    break

        if max(xMin, yMin) < 6 and self.board[x + 1][y + 1] == self.reverse(color):
            for e in range(2,min(xMax,yMax)):
                if self.board[x + e][y + e] == self.reverse(color):
                    continue
                elif self.board[x + e][y + e] == color:
                    return True
                else:
                    break

        if max(xMin, yMin) < 6 and self.board[x + 1][y + 1] == self.reverse(color):
            for e in range(2,min(xMax,yMax)):
                if self.board[x + e][y + e] == self.reverse(color):
                    continue
                elif self.board[x + e][y + e] == color:
                    return True
                else:
                    break

        return False
    

    def isAvailable(self,x,y,color):
        
        if not self.board[x][y] == self.empty:
            return False
        
        for xi in range(x + 1,8):
            if self.get(xi,y) == self.reverse(color):
                continue
            elif self.get(xi,y) == color and xi > x + 1 and xi < 8:
                return True
            else:
                break
        
        for xi in range(x - 1,-1,-1):
            if self.get(xi,y) == self.reverse(color):
                continue
            elif self.get(xi,y) == color and xi < x - 1 and xi >=0:
                return True
            else:
                break
        
        for yi in range(y + 1,8):
            if self.get(x,yi) == self.reverse(color):
                continue
            elif self.get(x,yi) == color and yi > y + 1 and yi < 8:
                return True
            else:
                break
        
        for yi in range(y - 1,-1,-1):
            if self.get(x,yi) == self.reverse(color):
                continue
            elif self.get(x,yi) == color and yi < y - 1 and yi >=0:
                return True
            else:
                break
        
        minValue = min(8 - x,8 - y)
        for i in range(1,minValue):
            if self.get(x + i,y + i) == self.reverse(color):
                if x + i + 1 >= 8 or y + i + 1 >= 8:
                    break
                elif x + i + 1 < 8 and y + i + 1 < 8:
                    nextColor = self.get(x + i +1,y + i + 1)
                    if nextColor == self.reverse(color):
                        continue
                    elif nextColor == color:
                        return True
                    else:
                        break
                else:
                    break
            else:
                break
                    
        minValue = min(8 - x,y)
        for i in range(1,minValue):
            if self.get(x + i,y - i) == self.reverse(color):
                if x + i + 1 >= 8 or y - i - 1 < 0:
                    break
                elif x + i + 1 < 8 and y - i - 1 >=0 :
                    nextColor = self.get(x + i + 1,y - i - 1)
                    if nextColor == self.reverse(color):
                        continue
                    elif nextColor == color:
                        return True
                    else:
                        break
                else:
                    break
            else:
                break

        minValue = min(x,y)
        for i in range(1,minValue):
            if self.get(x - i,y - i) == self.reverse(color):
                if x - i - 1 < 0 or y - i - 1 < 0:
                    break
                elif x - i - 1 >= 0 and y - i - 1 >=0 :
                    nextColor = self.get(x - i - 1,y - i - 1)
                    if nextColor == self.reverse(color):
                        continue
                    elif nextColor == color:
                        return True
                    else:
                        break
                else:
                    break
            else:
                break

        minValue = min(x,8 - y)
        for i in range(1,minValue):
            if self.get(x - i,y + i) == self.reverse(color):
                if x - i - 1 < 0 or y + i + 1 >= 8 :
                    break
                elif x - i - 1 >= 0 and y + i + 1 < 8 :
                    nextColor = self.get(x - i - 1,y + i + 1)
                    if nextColor == self.reverse(color):
                        continue
                    elif nextColor == color:
                        return True
                    else:
                        break
                else:
                    break
            else:
                break

        return False

    def getNextCandidate(self,color):
        l = list()
        for x in range(0,8):
            for y in range(0,8):
                if self.isAvailable(x,y,color):
                    l.append((x,y))
                    if not self.altIsAvailable(x,y,color):
                        print ("Fail")
        if len(l) == 0:
            return None
        return l
            
    def printEmptyList(self,color):
        li = self.getNextCandidate(color)
        if not li == None:
            for l in li:
                print (f'{l}')


    def printRecord(self,x,y,color):
        if color == self.black:
            print (f'○:put{x},{y}')
        else:
            print (f'●:put{x},{y}')

    def put(self,pos,color):
        x,y = pos
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

            minValue = min(8 - x, 8 - y)
            for i in range(1,minValue):
                if self.get(x + i,y + i) == self.reverse(color):
                    continue
                elif self.get(x + i,y + i) == color:
                    for ii in range(1, i):
                        self.board[x + ii][y + ii]=color
                        break
                else:
                    break

            minValue = min(8 - x,y)
            for i in range(1,minValue):
                if self.get(x + i,y - i) == self.reverse(color):
                    continue
                elif self.get(x + i,y - i) == color:
                    for ii in range(1, i):
                        self.board[x + ii][y - ii]=color
                        break
                else:
                    break

            minValue = min(x,y)
            for i in range(1,minValue):
                if self.get(x - i,y - i) == self.reverse(color):
                    continue
                elif self.get(x - i,y - i) == color:
                    for ii in range(1, i):
                        self.board[x - ii][y - ii]=color
                        break
                else:
                    break

            minValue = min(x,8 - y)
            for i in range(1,minValue):
                if self.get(x - i,y + i) == self.reverse(color):
                    continue
                elif self.get(x - i,y + i) == color:
                    for ii in range(1, i):
                        self.board[x - ii][y + ii]=color
                        break
                else:
                    break

#            self.printBoard()
        else:
            print("Err!!")

    def isGameOver(self):
      return not self.getNextCandidate(self.black) == None or not self.getNextCandidate(self.white) == None
    
    def result(self,count):
        white = 0
        black = 0
        for x in range(0,8):
            for y in range(0,8):
                if self.board[x][y]==self.black:
                    black += 1
                elif self.board[x][y]==self.white:
                    white += 1
        return black,white

    def printResult(self,count):
        black, white = self.result(count)
        print (f'{count}: black = {black}, white = {white}, ',end="")
        if white == black:
            print ("draw")
        elif white > black:
            print ("white win")
        else:
            print ("black win")
