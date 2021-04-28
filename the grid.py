#CREATING THE GRID
#creating the header line 
def headerLine(size, row, cell):
    for a in range(size):
        row += cell + str(a + 1)
    print(row)
    
#creating the divider line between cells
def createLine(size, row, line):
    for b in range(size+1):
        row += line
    print(row)

#creating the actual rows
def createRow(size, row, cell, counter):
    row = str(counter) + " "
    for r in range(size):
        row += "|" + cell
    print(row)

def createGrid(size, row, cell, line):
    headerLine(size, row, cell)
    counter = 1
    for w in range(size):
        createLine(size, row, line)
        createRow(size, row, cell, counter)
        counter +=1

#creating the dictionaries
def createDatastore(name, size, input)
for s in range(size):
    name[s] = []
    for i in range(size):
        name[s].append(inout)
        
#variables
size = 5
row = ""
cell = "     "
line = "-----"

createGrid(size, row, cell, line)

createDatastore(backend, size, cell)
createDatastore(frontend, size, cell)



#then need to make each cell of the pretty grid correspond to the dict cell






