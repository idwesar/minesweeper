class Store:
    def __init__(self):
        self.mines = []
        self.counter = {}

    def numAdjacentMines(self, x, y):
        #look up those coords and tell me how many adj mines
        if (x, y) in self.counter:
            return self.counter[(x, y)]
        return 0
        
        
    def addMine(self, x, y):
        #add a mine to those coords
        self.mines.append((x, y))
        
        #add one to all the cells around the mine
        for xTemp in range(x-1, x+2):
            for yTemp in range(y-1, y+2):
                if x != xTemp or y != yTemp: 
                    coord = (xTemp, yTemp)
                    if coord in self.counter.keys():
                        self.counter[coord] += 1
                    else:
                        self.counter[coord] = 1


    def isMine(self, x, y):
        #check if its a mine
        return (x, y) in self.mines


#unit testing
def testAdjacent():
    #arrange
    store = Store()
    x = 2
    y = 5

    #act
    result = store.numAdjacentMines(x, y)

    #assert
    assert(result == 0)

#adjacentmines needs more testing - when the cell is a mine, when there are multiple mines, when there are no mines adjacent#

#when the cell is a mine
#set a mine at certain coords
#check those coords in the mine dict
'''need to make sure that the counter dict is only checked if the coords arent a part of the mine dict'''
#when you click on a mine its game over

#when there are multiple mines
#pick coords, set mines in the surrounding coords (alter the chosen coords)
#check no of mines in counter (make sure to check in mines dict first because thats how its going to work)
#should return a value above one

#when there are no mines
#dont set up any mines
#check the mines
#shoud tell you its not in the counter dict, i.e no mines nearby


#testing adding a mine and checking the mine
def testAddMine():
    #arrange
    store = Store()
    x = 1
    y = 3

    #act
    store.addMine(x, y)

    #assert
    result = store.isMine(x, y)
    assert(result)


def main():
    testAddMine()
    testAdjacent()

if __name__ == "__main__":
    main()
