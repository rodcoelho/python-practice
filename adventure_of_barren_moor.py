import random, math, time

#Adventure of the Barren Moor

# magic compass that tells the player how far away the next feature of interest is.
# The player can choose north, south, east or west every move towards the feature.

class GameBoard():
    def __init__(self):
        self.board = []
        data_list = list(range(1,145))
        i = 0
        while i < len(data_list):
            self.board.append(data_list[i:i + 12])
            i += 12

    def printboard(self):
        for rows in self.board:
            print(rows)

    def targetlocation(self):
        row = random.choice(self.board)
        element = random.choice(row)
        return element

    def beginninglocation(self):
        row = random.choice(self.board)
        element = random.choice(row)
        return element

    def check_distance(self,user,target):
        board = self.board
        def getCoords(self, point):
            for rows in board:
                for elements in rows:
                    if elements == point:
                        return [board.index(rows),rows.index(elements)]
        user = getCoords(board,user)
        target = getCoords(board,target)
        dist = math.hypot(user[0] - target[0], user[1] - target[1])
        return user,target, dist

if __name__ == '__main__':

    GB = GameBoard()

    # initialize user and target
    user = GB.beginninglocation()
    target = GB.targetlocation()
    # print('User is {} and target is {}'.format(user,target))

    # user location and target location test
    uloc, tloc, distance = GB.check_distance(user,target)
    # print('User loc is {} and Target loc is {}'.format(uloc,tloc))
    print('The dial reads: {: .2f} m'.format(distance))
    print()
    def buttons(uloc,tloc):
        uloc, tloc, distance = GB.check_distance(user, target)
        x = 0
        while x == 0:
            inp = input('n, s, e, or w ?')
            if inp == 'n':
                uloc[0]-= 1
            elif inp == 's':
                uloc[0] += 1
            elif inp == 'e':
                uloc[1]+= 1
            elif inp == 'w':
                uloc[1] -= 1
            else:
                print('{} is not a valid direction!'.format(inp))
            distaa = math.hypot(uloc[0] - tloc[0], uloc[1] - tloc[1])
            print('The dial reads {: .2f}'.format(distaa))
            if distaa < 1:
                x += 1
        print()
        time.sleep(1)
        print()
        print('You see a box sitting on the plain')
        time.sleep(1)
        print()
        print('The box is filled with treasure!')
        time.sleep(1)
        print()
        print('You win!')
        time.sleep(.5)
        print()
        print('THE END')
        print()
    buttons(uloc,tloc)