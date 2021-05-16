#CREATING THE DISPLAY GRID - not actually useful yet, shows x and y coords for test purposes
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
        row += ("|" + x + "," + y)
    print(row)

def createGrid(size, row, x, y, line):
    headerLine(size, row, blank)
    counter = 1
    for r in range(size):
        createLine(size, row, line)
        createRow(size, row, x, y, counter)
        counter +=1


blank = "   "
line = "----"
row = ""
size = 5
x = "1"
y = "1"
counter = 1

createGrid(size, row, x, y, line)
