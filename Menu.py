def getMenuOption(prompt, options):
    goodOption = False
    while not goodOption:
        option = raw_input(prompt)
        if option.lower() in options:
            goodOption = True
        else:
            print "Please make a valid selection from the menu"
    return option.lower()
    
def menu():
    print "------Madlibs Menu-------"
    print "| 1) Animal story       |"
    print "| 2) Story 2            |"
    print "| 3) Story 3            |"
    print "| Q) Quit               |"
    print "-------------------------"
    optionsList = ["1",
                   "2",
                   "3",
                   "animal",
                   "animal story",
                   "up down up down left right left right b a start",
                   "quit",
                   "q"]
    return getMenuOption("> ", optionsList)
