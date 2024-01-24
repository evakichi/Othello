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
        self.nextColor = 0
        self.nextPos = (-1,-1)

    def copy(self):
        b = Board()
        for x in range(8):
            for y in range(8):
                b.put(x,y,self.get(x,y))
        return b

    def copyNextPass(self,color):
        c = self.copy()
        c.setNextPos(None)
        c.setNextColor(color)
        return c

    def reverse(self,color):
        return -1*color
    
    def setNextPos(self,pos):
        self.nextPos = pos

    def setNextColor(self,color):
        self.nextColor = color

    def getColorString(color):
        if color == Board.black:
            return 'B'
        elif color == Board.white:
            return 'W'
        else:
            return '-'

    def put (self,x,y,color):
        self.board[x][y] = color

    def get (self,x,y):
        return self.board[x][y]

    def isEmpty(self,x,y):
        return self.get(x,y) == self.empty

    def isReverse(self,x,y,color):
        return self.get(x,y) == self.reverse(color)

    def isNormal(self,x,y,color):
        return self.get(x,y) == color

    def printBoard(self):
        print (" ",end="")
        for j in range(0,8):
            print (f'|{j}',end="")
        print ("|")
        for i in range(0,8):
            print (f'{i}',end="")
            for j in range(0,8):
                if self.get(i,j)==self.black:
                    print ("|B",end="")
                elif self.get(i,j)==self.white:
                    print ("|W",end="")
                else:
                    print ("| ",end="")
            print ("|")


    def isAvailable(self,p,nextColor):
        if p == None:
            return False
        x,y = p
        if not self.isEmpty(x,y):
            return False

        if x < 6 and self.isReverse(x + 1,y,nextColor):
            for e in range(2, 8 - x):
                if self.isReverse(x + e,y,nextColor):
                    continue
                elif self.isNormal(x + e,y,nextColor):
                    return True
                else:
                    break

        if x > 1 and self.isReverse(x - 1,y,nextColor):
            for e in range(2, x + 1):
                if self.isReverse(x - e,y,nextColor):
                    continue
                elif self.isNormal(x - e,y,nextColor):
                    return True
                else:
                    break

        if y < 6 and self.isReverse(x,y + 1,nextColor):
            for e in range(2, 8 - y):
                if self.isReverse(x,y + e,nextColor):
                    continue
                elif self.isNormal(x,y + e,nextColor):
                    return True
                else:
                    break

        if y > 1 and self.isReverse(x,y - 1,nextColor):
            for e in range(2, y + 1):
                if self.isReverse(x,y - e,nextColor):
                    continue
                elif self.isNormal(x,y - e,nextColor):
                    return True
                else:
                    break

        minValue = min(7 - x,7 - y)
        if minValue > 1 and self.isReverse(x + 1,y + 1,nextColor):
            for e in range(2, minValue + 1):
                if self.isReverse(x + e,y + e,nextColor):
                    continue
                elif self.isNormal(x + e,y + e,nextColor):
                    return True
                else:
                    break

        minValue = min(7 - x,y)
        if minValue > 1 and self.get(x + 1,y - 1) == self.reverse(nextColor):
            for e in range(2, minValue + 1):
                if self.isReverse(x + e,y - e,nextColor):
                    continue
                elif self.isNormal(x + e,y - e,nextColor):
                    return True
                else:
                    break

        minValue = min(x,y)
        if minValue > 1 and self.isReverse(x - 1,y - 1,nextColor):
            for e in range(2, minValue + 1):
                if self.isReverse(x - e,y - e,nextColor):
                    continue
                elif self.isNormal(x - e,y - e,nextColor):
                    return True
                else:
                    break

        minValue = min(x,7 - y)
        if minValue > 1 and self.isReverse(x - 1,y + 1,nextColor):
            for e in range(2, minValue + 1):
                if self.isReverse(x - e,y + e,nextColor):
                    continue
                elif self.isNormal(x - e,y + e,nextColor):
                    return True
                else:
                    break

        return False

    def altIsAvailable(self,pos,color):
        x,y = pos
        if not self.isEmpty(x,y):
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
                if self.isAvailable((x,y),color):
                    l.append((x,y))
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
            print (f'B:put{x},{y}')
        else:
            print (f'W:put{x},{y}')

    def getNextPos(self):
        return self.nextPos

    def getNextColor(self):
        return self.nextColor

    def copyAndNext(self,p,color):
        c = self.copy()
        c.putNext(p,color)
        return c

    def putNext(self,nextPos,nextColor):

        if nextPos == None:
            return False
        
        self.setNextPos(nextPos)
        self.setNextColor(nextColor)

        x,y = nextPos

        if not self.isEmpty(x,y):
            return False
        
        self.put(x,y,nextColor)

        if x < 6 and self.isReverse(x + 1,y,nextColor):
            for e in range(2, 8 - x):
                if self.isReverse(x + e,y,nextColor):
                    continue
                elif self.isNormal(x + e,y,nextColor):
#                    print(f'a:↓:{e}')
                    for ee in range(1,e):
#                        print(f'a:put({x+ee},{y})')
                        self.put(x + ee,y,nextColor)
                    break
                else:
                    break

        if x > 1 and self.isReverse(x - 1,y,nextColor):
            for e in range(2, x + 1):
                if self.isReverse(x - e,y,nextColor):
                    continue
                elif self.isNormal(x - e,y,nextColor):
#                    print(f'a:↑:{e}')
                    for ee in range(1,e):
#                        print(f'a:put({x-ee},{y})')
                        self.put(x - ee,y,nextColor)
                    break
                else:
                    break

        if y < 6 and self.isReverse(x,y + 1,nextColor):
            for e in range(2, 8 - y):
                if self.isReverse(x,y + e,nextColor):
                    continue
                elif self.isNormal(x,y + e,nextColor):
#                    print(f'a:→:{e}')
                    for ee in range(1,e):
#                        print(f'a:put({x},{y+ee})')
                        self.put(x,y + ee,nextColor)
                    break
                else:
                    break

        if y > 1 and self.isReverse(x,y - 1,nextColor):
            for e in range(2, y + 1):
                if self.isReverse(x,y - e,nextColor):
                    continue
                elif self.isNormal(x,y - e,nextColor):
#                    print(f'a:←:{e}')
                    for ee in range(1,e):
#                        print(f'a:put({x},{y-ee})')
                        self.put(x,y - ee,nextColor)
                    break
                else:
                    break

        minValue = min(7 - x,7 - y)
        if minValue > 1 and self.isReverse(x + 1,y + 1,nextColor):
            for e in range(2, minValue + 1):
                if self.isReverse(x + e,y + e,nextColor):
                    continue
                elif self.isNormal(x + e,y + e,nextColor):
#                    print(f'a:↘:{e}')
                    for ee in range(1,e):
#                        print(f'a:put({x + ee},{y + ee})')
                        self.put(x + ee,y + ee,nextColor)
                    break
                else:
                    break

        minValue = min(7 - x,y)
        if minValue > 1 and self.get(x + 1,y - 1) == self.reverse(nextColor):
            for e in range(2, minValue + 1):
                if self.isReverse(x + e,y - e,nextColor):
                    continue
                elif self.isNormal(x + e,y - e,nextColor):
#                    print(f'a:↙:{e}')
                    for ee in range(1,e):
#                        print(f'a:put({x + ee},{y - ee})')
                        self.put(x + ee,y - ee,nextColor)
                    break
                else:
                    break

        minValue = min(x,y)
        if minValue > 1 and self.isReverse(x - 1,y - 1,nextColor):
            for e in range(2, minValue + 1):
                if self.isReverse(x - e,y - e,nextColor):
                    continue
                elif self.isNormal(x - e,y - e,nextColor):
#                    print(f'a:↖:{e}')
                    for ee in range(1,e):
#                        print(f'a:put({x - ee},{y - ee})')
                        self.put(x - ee,y - ee,nextColor)
                    break
                else:
                    break

        minValue = min(x,7 - y)
        if minValue > 1 and self.isReverse(x - 1,y + 1,nextColor):
            for e in range(2, minValue + 1):
                if self.isReverse(x - e,y + e,nextColor):
                    continue
                elif self.isNormal(x - e,y + e,nextColor):
#                    print(f'a:↗:{e}')
                    for ee in range(1,e):
#                        print(f'a:put({x - ee},{y + ee})')
                        self.put(x - ee,y + ee,nextColor)
                    break
                else:
                    break

        return False
    

    def altPutNext(self,pos,color):
        x,y = pos
        if self.isAvailable(x,y,color):
            self.put(x,y,color)
#            self.printRecord(x,y,color)
            for i in range(x+1,8):
                if self.get(i,y) == self.reverse(color):
                    continue
                elif self.get(i,y) == color:
                    for ii in range(x+1,i):
#                        print(f'n:put({ii},{y})')
                        self.put(ii,y,color)
                    break
                else:
                    break

            for i in range(x-1,-1,-1):
                if self.get(i,y) == self.reverse(color):
                    continue
                elif self.get(i,y) == color:
                    for ii in range(x-1,i-1,-1):
#                        print(f'n:put({ii},{y})')
                        self.put(ii,y,color)
                    break
                else:
                    break

            for i in range(y+1,8):
                if self.get(x,i) == self.reverse(color):
                    continue
                elif self.get(x,i) == color:
                    for ii in range(y+1,i):
#                        print(f'n:put({x},{ii})')
                        self.put(x,ii,color)
                    break
                else:
                    break

            for i in range(y-1,-1,-1):
                if self.get(x,i) == self.reverse(color):
                    continue
                elif self.get(x,i) == color:
                    for ii in range(y-1,i-1,-1):
#                        print(f'n:put({x},{ii})')
                        self.put(x,ii,color)
                    break
                else:
                    break

            minValue = min(8 - x, 8 - y)
            for i in range(1,minValue):
                if self.get(x + i,y + i) == self.reverse(color):
                    continue
                elif self.get(x + i,y + i) == color:
                    for ii in range(1, i):
#                        print(f'n:put({x + ii},{y + ii})')
                        self.put(x + ii,y + ii,color)
                    break
                else:
                    break

            minValue = min(8 - x,y + 1)
            for i in range(1,minValue):
                if self.get(x + i,y - i) == self.reverse(color):
                    continue
                elif self.get(x + i,y - i) == color:
                    for ii in range(1, i):
#                        print(f'n:put({x + ii},{y - ii})')
                        self.put(x + ii,y - ii,color)
                    break
                else:
                    break

            minValue = min(x + 1,y + 1)
            for i in range(1,minValue):
                if self.get(x - i,y - i) == self.reverse(color):
                    continue
                elif self.get(x - i,y - i) == color:
                    for ii in range(1, i):
#                        print(f'n:put({x - ii},{y - ii})')
                        self.put(x - ii,y - ii,color)
                    break
                else:
                    break

            minValue = min(x + 1,8 - y)
            for i in range(1,minValue):
                if self.get(x - i,y + i) == self.reverse(color):
                    continue
                elif self.get(x - i,y + i) == color:
                    for ii in range(1, i):
#                        print(f'n:put({x - ii},{y + ii})')
                        self.put(x - ii,y + ii,color)
                    break
                else:
                    break

#            self.printBoard()
        else:
            print("Err!!")

    def isGameOver(self):
      return self.getNextCandidate(self.black) == None and self.getNextCandidate(self.white) == None
    
    def result(self,count):
        white = 0
        black = 0
        for x in range(0,8):
            for y in range(0,8):
                if self.get(x,y)==self.black:
                    black += 1
                elif self.get(x,y)==self.white:
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
