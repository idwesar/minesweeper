#CREATING THE GRID
#creating the header line 
def headerLine(size, row, blank):
    for a in range(size):
        row += blank + str(a + 1)
    print(row)
    
#creating the divider line between cells
def createLine(size, row, line):
    for b in range(size+1):
        row += line
    print(row)

#creating the actual rows
def createRow(size, row, x, y, counter):
    row = str(counter) + " "
    for r in range(size):
        row += "|" + x + "," + y
    print(row)

def createGrid(size, row, x, y, line):
    headerLine(size, row, blank)
    counter = 1
    for w in range(size):
        createLine(size, row, line)
        createRow(size, row, x, y, counter)
        counter +=1

#creating the dictionaries
def createDatastore(name, size, coords, x, y, data):
    for x in range(size):
        for y in range(size):
            name[x, y] = [cell]

            
#coord converter
# def convertCoords():
    #take the input string and split it into ints for x and y value, then -1 to each, that's your database reference


#game variables
size = 5

#grid creation variables
blank = "   "
line = "----"
row = ""

#dict creation variables
x = 1
y = 1
coords = str([x, y])
cell = ""
datastore = {}
visibility = {}


createDatastore(datastore, size, coords, x, y, cell)
createDatastore(visibility, size, coords, x, y, cell)

print(datastore)
