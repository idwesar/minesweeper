class Visibility:
    def __init__(self):
        #this will make the set that stores the visibility data. the coords for all the visible cells (i.e. everything that has already been chosen)
        self.viz = []

    def isVisible(self, x, y):
        #this will check the coords in the visibility set. if they're there, then the cell 'is visible'
        if (x, y) in self.viz:
            return True
        else:
            return False

    def makeVisible(self, x, y):
        #this will add the coords passed to it into the visibility set
        self.viz.append((x, y))


#unit testing
def testVisibilityExists():
    #arrange
    visibility = Visibility()

    x = 1
    y = 3

    #act
    visibility.makeVisible(x, y)

    #assert
    result = visibility.isVisible(x, y)
    assert(result)


def testVisibilityNotExist():
    #arrange
    visibility = Visibility()

    x = 2
    y = 4

    #act
    visibility.makeVisible(x, y)

    #assert
    result = visibility.isVisible(x+1, y+1)
    assert(not result)


def main():
    testVisibilityExists()
    testVisibilityNotExist()
    

if __name__ == "__main__":
    main()
