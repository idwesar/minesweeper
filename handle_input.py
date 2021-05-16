BAD_CHARS = "()[]"

#sanitising the input
def sanitiseInput(selection):
    stripped = selection.strip()
    stripped = stripped.replace(" ", "")
    stripped = stripped.strip(BAD_CHARS)

    return stripped

#convert the input to integers
def convertInputToInt(stripped):
    values = stripped.split(",")
    chosenX = int(values[0])
    chosenY = int(values[1])

    return chosenX, chosenY

#convert integer to datastore key
''' this can be edited, thats not how the datastore works anymore'''
def convertIntToKey(chosenX, chosenY):
    chosenX -= 1
    chosenY -= 1
    key = [chosenX, chosenY]
    print(key)


#coord converter
# def convertCoords():
    #take the input string and split it into ints for x and y value, then -1 to each, that's your database reference

#need to allow for when the user inputs an invalid string - if you cant get 2 ints from the input then ask them to input it again

#write some tests