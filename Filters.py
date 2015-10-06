def getWord(prompt):
    goodWord = False
    while not goodWord:
        word = raw_input(prompt)
        if isSwear(word):
            goodWord = False
            print "OH NO! What bad language you have!"
            print "Polite words only"
        else:
            goodWord = True
    return word

def getNumber(prompt, minimum=None, maximum=None):
    numbers = "0123456789."
    goodNumber = False
    while not goodNumber:
        number = raw_input(prompt)
        goodNumber = True
        for c in number:
            if goodNumber:
                if c not in numbers:
                    goodNumber = False
                    print number + " is not a number!"
        if goodNumber:
            number = float(number)
            if not (minimum == None):
                if number < minimum:
                    goodNumber = False
                    print "Number must be bigger than " + str(minimum)
            if not (maximum == None):
                if number > maximum:
                    goodNumber = False
                    print "Number must be smaller than " + str(maximum)
    return str(number)
        
        

def isSwear(word):
    swearList = ["fuck",
                 "shit",
                 "fucked"]
    if word.lower() in swearList:
        return True
    else:
        return False
