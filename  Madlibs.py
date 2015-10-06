from Filters import *
from Menu import *
from Story1 import *

def madlibs():
    print "Welcome to Madlibs"
    print "    by Chris Spooner"
    print
    gameOver = False
    while not gameOver:
        option = menu()
        if option in ["1", "animal", "animal story"]:
            print story1()
            print
            raw_input("press enter to continue")
        elif option in ["q", "quit"]:
            gameOver = True
    print "Good bye"
    
madlibs()
