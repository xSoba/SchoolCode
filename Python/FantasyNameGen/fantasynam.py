#numpy used for arrays, removing limitations in base python
import random
from unicodedata import name
import numpy as np
import cfg as cfg

def init():
    #Initialising Module: Sets our cfg.syllable lists and sends a welcome message
    print("Welcome to Fantasy Name Generator 3000 where we generate totally normal names for a race of your choice!")
    
def select():
    #This is where the user will select what race, gender and status they want to be. As well as selecting amount of syllables in their name
 selectVerify('What race would you like your name to originate from? \n 1.Human \n 2.Orc \n 3.Elf \n Please enter the corresponding number \n')
 selectVerify('What Gender would you like you name be oriented to? \n 1.Male \n 2.Female \n Please enter the corresponding number \n')
 selectVerify('Please enter the amount of syllables you would like for your name to be consisted of \n')

def generation():
    retrieve()
    #Checking if the amount of syllables given needs a middle syllable
    if cfg.opt[2] - 2 != 0:
        cfg.pos = cfg.pos + 1
        #Setting a loop for the amount of middles syllables that need to be added
        for i in range(cfg.opt[2] - 2):
            transport(cfg.pos)
        cfg.pos = cfg.pos + 1
        transport(cfg.pos)
    
    else:
        #Adding the end syllable if the amount of syllables wanted is less than 2
        cfg.pos = cfg.pos + 2
        transport(cfg.pos)
    polish()
    
def polish():
    #Sorts the array to make the order First Syllable, Middle Syllables, End Syllable
    np.sort(cfg.name)
    cfg.name = cfg.name.tolist()
    #Joins the string items together, forming a name
    print(''.join(cfg.name))
                    
def transport(x):
    cfg.name = np.append(
    #Array we are appending to
    cfg.name,
    #Array we are appending from
    cfg.races
    #Specifying which sub arrays to pull data from
    [cfg.opt[0] - 1]
    [cfg.opt[1] - 1][x]
    #generating a random integer that will act as the position for the element that will be retrieved
    [random.randint
    (0, cfg.races
        [cfg.opt[0] - 1]
        [cfg.opt[1] - 1]
        [x].size - 1)])

def retrieve():
    transport(cfg.pos)

def selectVerify(x: str):
    #Setting an infinite loop, so the program doesnt end due to an invalid input
    while True : 
        tempstore = 0
        tempstore = input(print(f'{x}'))
        try:
            if int(tempstore) > 0 and int(tempstore) < 4:
                #Checking whether given values are within exceptable ranges
                cfg.opt = np.append(cfg.opt, int(tempstore))
                print("Value Accepted")
                #escaping loop once everything has been validated
                break
            else:
                print("Invalid Input, Please enter a different value")
        except ValueError:
            #If a string has been given this except statement will catch the Error
            print("ERROR: Value entered was not suitable data type")
        
init()
select()
generation()