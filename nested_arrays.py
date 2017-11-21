import random

class GameBoard():
    def __init__(self):
        self.board = []
        for i in range(4):
            self.board.append(list(random.sample(range(1, 101), 4)))

    def printboard(self):
        for rows in self.board:
            print(rows)

    def getRow(self,n):
        print(self.board[n])

    def getCol(self,n):
        collist = []
        for rows in self.board:
            collist.append(rows[n])
        print(collist)

    def getCoords(self, target):
        for rows in self.board:
            for elements in rows:
                if elements == target:
                    return'{}, {}'.format(self.board.index(rows),rows.index(elements))
        else:
            return False
    def getSurround(self,x, y):
        r = [y-1,y,y+1]
        c = [x-1,x,x+1]
        surround_list = []
        for rows in self.board:
            for elements in rows:
                if rows.index(elements) in r and self.board.index(rows) in c:
                    surround_list.append(elements)
        print(surround_list)

if __name__ == '__main__':
    GB = GameBoard()

    # printboard() test
    GB.printboard()

    # getRow test
    GB.getRow(3)

    # getCol test
    GB.getCol(0)

    # getCoords test
    x = GB.getCoords(50)
    print(x)

    # get Surrounds test
    GB.getSurround(1,1)