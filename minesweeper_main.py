import random

#local imports
# import handle_input
import store as s
import visibility as v
import grid as g


#generate the mine coordinates - all unique
def createMineCoords(mines, size):
    mineCoords = []
    while len(mineCoords) < mines:
        mineX = random.randint(0,size-1)
        mineY = random.randint(0,size-1)
        if (mineX, mineY) not in mineCoords:
            mineCoords.append((mineX, mineY))

    return mineCoords


def setUpMines(mines, size):
    store = s.Store()
    mineCoords = createMineCoords(mines, size)
    
    for coord in mineCoords:
        store.addMine(coord)

    return mineCoords


#testing
#tests mine coord generation, checks they're all unique and that there are enough of them
def testCreateMineCoords():
    mines = 5
    size = 5

    result = createMineCoords(mines, size)
    
    assert(len(set(result)) == mines)

#TODO make this test work
def testSetUpMines():
    store = s.Store()
    mines = 1
    size = 5
    
    #act
    minesList = setUpMines(mines, size)
    print(minesList)
    
    for mine in minesList:
        if store.isMine(mine) == True:
            print("true")
        else:
            print("false")
    print(store.mines)


    # result = store.isMine()
    # print(result)
    
    # assert(result == 1)

#testing add mines - it IS adding mines here
def testAddMine():
    #arrange
    store = s.Store()
    coord = (1, 2)

    #act
    store.addMine(coord)

    #assert
    result = store.isMine(coord)
    print(store.mines)
    assert(result)


def main():
    #game variables
    size = 5
    mines = 5

    testAddMine()
    testSetUpMines()
    testCreateMineCoords()


    # #input variables
    # selection = input("Select your coordinates (x, y): ")
    # stripped = sanitiseInput(selection)
    # chosenX, chosenY = convertInputToInt(stripped)
    # convertIntToKey(chosenX, chosenY)



if __name__ == "__main__":
    main()
