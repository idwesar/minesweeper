class Store:
    def __init__(self):
        self.mines = []
        self.counter = {}


    def numAdjacentMines(self, coord):
        #look up those coords and tell me how many adj mines
        if (coord) in self.counter:
            return self.counter[coord]
        return 0
        
        
    def addMine(self, coord):
        #add a mine to those coords
        self.mines.append(coord)

        x = coord[0]
        y = coord[1]
        
        #add one to all the cells around the mine
        for xTemp in range(x-1, x+2):
            for yTemp in range(y-1, y+2):
                if x != xTemp or y != yTemp: 
                    coord = (xTemp, yTemp)
                    if coord in self.counter.keys():
                        self.counter[coord] += 1
                    else:
                        self.counter[coord] = 1


    def isMine(self, coord):
        #check if its a mine
        return (coord) in self.mines


#unit testing
#testing adding a mine and checking the mine - the cell is a mine
def testAddMine():
    #arrange
    store = Store()
    coord = (1, 2)

    #act
    store.addMine(coord)

    #assert
    result = store.isMine(coord)
    assert(result)

#when there are no adjacent mines
def testNoMines():
    #arrange
    store = Store()
    coord = (5, 2)

    #act
    result = store.numAdjacentMines(coord)

    #assert
    assert(result == 0)

#when there's one adjacent mine
def testOneMine():
    #arrange
    store = Store()
    coord = (3, 4)
    x = coord[0]
    y = coord[1]

    store.addMine(coord)

    #act
    result = store.numAdjacentMines((x+1, y))

    #assert
    assert(result == 1)

#when there are multiple adjacent mines
def testMultipleMines():
    #arrange
    store = Store()
    coord = (1, 5)
    x = coord[0]
    y = coord[1]

    store.addMine((x-1, y))
    store.addMine((x, y+1))
    store.addMine((x+1, y+1))

    #act
    result = store.numAdjacentMines(coord)

    #assert
    assert(result == 3)


def main():
    testAddMine()
    testNoMines()
    testOneMine()
    # testMultipleMines()

if __name__ == "__main__":
    main()
