# The main file. The raw script data was converted into a fresh database
# (python dictionary) which this file can use to generate stuff.

import random
import ast

nb = input("How much sentences to generate?\n")
print("")

def nextWord(last):
    values = database[last]
    total = values[0];
    if (total == 1):
        return values[1][0]
    
    pick = random.randint(1, values[0])

    #print("picked value ", pick)

    word = 1;
    while True:
        #print("current word : ", word, " current pick : ", pick)
        pick -= values[word][1]
        if (pick <= 0):
            break;
        word += 1

    #print("return time! return ", values[word][0])
    return values[word][0]
        
        
    

with open('parserOutput.in', 'r') as file:
    database = file.read().replace('\n', '')

database = ast.literal_eval(database)

startKeys = list(database.keys())
# removing the eventual empty string word which shouldn't happen
#startKeys.remove("")

for key in startKeys:
    if not(key[0].isupper()):
        startKeys.remove(key)

for abc in range(int(nb)):

    funny = random.choice(startKeys)
    last = funny

    endSentence = False;
    while len(funny) < 120:# or not(endSentence):
        endSentence = False
        last = nextWord(last)
        if (last == None):
            last = random.choice(startKeys)
            endSentence = True
            
        funny += " " + last



    print(">>>", funny, "\n")
