# The main file. The raw script data was converted into a fresh database
# (python dictionary) which this file can use to generate stuff.

############## CHECK OUT THE BOTTOM OF THIS FILE FOR THE MAIN CODE ##############

######################################################################
######################################################################
#################### UTILITY / BUILDING BLOCKS #######################
######################################################################
######################################################################

import random
import ast

deviationCount = 0;
deviationLog = ""
debug = False;


# displays the next words of a word with their probabilities, used for
# debugging GUI. "NoneType" was chosen to be a magic morpheme representing the end of a quote.
def nextWordData(futureValProb):
    r = " (" + str(futureValProb[0]) + " possibilities) ==>\n           "
    for futureWord in futureValProb[1:]:
        term = futureWord[0];
        if term == None:
            term = "NoneType"
        r += "[" + term + "  " + str(futureWord[1]) + "] "
    return r
    


# randomly choose a potential word n from the database depending on words n-2 and n-1.
def nextWord(nd2, nd1):
    values = database[(nd2, nd1)]
    total = values[0];
    # if there exist only ONE case of word n to follow on n-2 and n-1
    if (total == 1):
        return values[1][0]
    
    # if several possibilities exist

    # See ReadME for more informations on this debugging stuff. They help visualise the algorithm.
    if (debug):
        global deviationCount;
        deviationCount += 1;
        global deviationLog;
        deviationLog += "\n\n" + "  \"" + nd2 + " " + nd1 + "\"" + nextWordData(values)
    
    pick = random.randint(1, values[0])
    word = 1;
    while True:
        pick -= values[word][1]
        if (pick <= 0):
            break;
        word += 1


    return values[word][0]
        
        
   


# generate 1 of the requested messages  
def generateMessage():
    funny = ""
    while(len(funny) < 120):
        funny += generateQuote()
    print(">>>", funny, "\n")
    if (debug):
       print(deviationCount, "context deviations mid-sentence at best.\n", deviationLog, "\n")

# generate 1 quote (a set of sentences). Ranging from 1 to potentially a lot more sentences
# the quote ends when it reaches an original quote ending.
def generateQuote():

    sentences = ""    
    initial2Words = random.choice(startKeys)
    # any word starting with a capitalized letter is eligible for being first word of the sentence
    nd2 = initial2Words[0]
    # the 2nd word of the sentence -if it exists- is a simple Makrov of order 1. Any word w which ever followed the first word is eligible.
    # this if case covers the 1-morpheme sentences (sentences with only 1 word)
    if initial2Words[1] == None:
        return nd2 + " "

    # if sentence contains more than 1 morpheme (most cases) :
    else:
        nd1 = initial2Words[1]
        sentences += (nd2 + " " + nd1)

        while True:
            tmp = nd1
            nd1 = nextWord(nd2, nd1)
            if (nd1 == None):
                return sentences + " "
            sentences += " " + nd1
            nd2 = tmp











######################################################################
######################################################################
########################### MAIN PROGRAM #############################
######################################################################
######################################################################


nb = input("How much messages to generate?\nA message is a small but variable amount of quotes mixed together.\n")
# See ReadME for informations about debug
while (nb == 'debug'):
    debug = True
    nb = input("Debug mode enabled to keep track of the algorithm. \nHow much messages to generate?\n")
print("")



 

with open('parserOutput.in', 'r') as file:
    database = file.read().replace('\n', '')

database = ast.literal_eval(database)

keys = list(database.keys())


startKeys = []
# startKeys is a subset of the database words tuples, it only contains
# tuples with a first term starting with a caps (words which can start a sentence)
for key in keys:
    # key[0][0] ==> the first character of the first string in a key tuple.
    if key[0][0].isupper():
        startKeys.append(key)




# generate nb messages, as requested by the user
for abc in range(int(nb)):
    generateMessage()
    deviationCount = 0
    deviationLog = ""
