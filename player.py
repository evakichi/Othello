import board
import os

class player:

    def __init__(self,ownColor):
        self.ownColor = ownColor

        self.homeDir = os.environ.get('HOME')
        self.dataDir = os.path.join(self.homeDir,'.othellodata')
        if not os.path.exists(self.dataDir):
            os.makedirs(self.dataDir)
        self.ownWinCount = 0

    def getOwnColor(self):
        return self.ownColor

    def getNext(self,currentBoard):
        pass