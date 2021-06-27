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
def createRow(size, row, cell, counter):
    row = str(counter) + " "
    for r in range(size):
        row += ("|" + cell)
    print(row)

def createGrid(size, row, cell, line):
    headerLine(size, row, blank)
    counter = 1
    for r in range(size):
        createLine(size, row, line)
        createRow(size, row, cell, counter)
        counter +=1

def main():
    createGrid(size, row, cell, line)

blank = "   "
line = "----"
row = ""
size = 5
cell = "   "
counter = 1


#TODO: how to test?

if __name__ == "__main__":
    main()


