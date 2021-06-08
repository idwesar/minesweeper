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
#testing adding a mine and checking the mine - the cell is a mine
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

#when there are no adjacent mines
def testNoMines():
    #arrange
    store = Store()
    x = 2
    y = 5

    #act
    result = store.numAdjacentMines(x, y)

    #assert
    assert(result == 0)

#when there's one adjacent mine
def testOneMine():
    #arrange
    store = Store()
    x = 3
    y = 2

    store.addMine(x, y)

    #act
    result = store.numAdjacentMines(x+1, y)

    #assert
    assert(result == 1)

#when there are multiple adjacent mines
def testMultipleMines():
    #arrange
    store = Store()
    x = 4
    y = 3

    store.addMine(x-1, y)
    store.addMine(x, y+1)
    store.addMine(x+1, y+1)

    #act
    result = store.numAdjacentMines(x, y)

    #assert
    assert(result == 3)


def main():
    testAddMine()
    testNoMines()
    testOneMine()
    testMultipleMines()

if __name__ == "__main__":
    main()
