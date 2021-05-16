import random

#local imports
from handle_input import *
from store import *
from visibility import *

#for input sanitisation purposes
BAD_CHARS = "()[]"


#generate the mine coordinates
def createMineCoords(size):
    mineCoords = []
    for x in range(size):
        mineX = random.randint(0,size-1)
        mineY = random.randint(0,size-1)
        mineCoords.append((mineX, mineY))

    return mineCoords


def main():
    #game variables
    size = 5
    mines = 5

    #grid creation variables
    mineDisplay = "X"

    #dict creation variables
    defaultData = 0
    defaultBool = False


    #input variables
    selection = input("Select your coordinates (x, y): ")


    #create the datastore dict and the visibility dict
    numberStore = Datastore(size, defaultData)
    visibilityStore = Datastore(size, defaultBool)
    
    
    #generate mine coordinates and place the mines in the datastore
    mineCoords = createMineCoords(size)
    numberStore.placeMines(mineCoords, mineDisplay)

    stripped = sanitiseInput(selection)
    chosenX, chosenY = convertInputToInt(stripped)
    convertIntToKey(chosenX, chosenY)


if __name__ == "__main__":
    main()