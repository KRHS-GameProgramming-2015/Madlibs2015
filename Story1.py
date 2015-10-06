from Filters import *

def story1():
    animal1 = getWord("Kind of animal? ")
    nameOfAnimal1 = getWord("A name? ")
    nameOfAnimal1 = nameOfAnimal1.capitalize()
    numberOfFriends = getNumber("A number between 2 and 20? ", 2, 20)
    
    output = ""
    output += "One day there was a "
    output += animal1
    output += " whose name was "
    output += nameOfAnimal1
    output += ". "
    output += nameOfAnimal1
    output += " had "
    output += numberOfFriends
    output += " friends. "
    
    return output

#print story1()
