# The parser takes "raw data" and turn it into a structure the algorithm can use.
# Concretly, it produces a dictionary.
# They key is a tuple (w1, w2) which represent two words w1 and w2, w2
# being positionned right after w1.

# The value of each key is [x, [x1, m], [x2, n], [x3, o], [x4, p]...]
# [x1, m] represents the fact the sequence of word "w1 w2 x1" existed m times
# in the raw data.
# [x2, n] indicates the sequence w1 w2 x2 occured n times. [x3, o] indicates
# the sequence w1 w2 x3 occured o times. And so on.
# the x variable is just the sum of occurances. x = m + n + o + p....
# (that's just some complexity improvement shenanigans)


# The data is parsed from the scripts (located in the data/dataSets folder)
# to parserOutput.in in this file's folder.


import fileinput
import os


# increase newVal's possibility of being selected after curVal
# used in Markov Chain dictionary building process when a key already exists
def newMarkov(curVal, newVal):
    for i in range(1, len(curVal)):
        if curVal[i][0] == newVal:
            curVal[i][1] += 1;
            curVal[0] += 1
            return curVal;

    # this block runs if the key is already present, but newVal is a new possible value
    curVal.append([newVal, 1])
    curVal[0] += 1
    return curVal

# Parse original data into list of strings
entree_str = [line.strip() for line in fileinput.input("data\dataSets\s4ep1.in")]
entree_str2 = [line.strip() for line in fileinput.input("data\dataSets\generalQuotes.in")]
entree_str.extend(entree_str2)

# separate each quote whenever a space (blank) is encountered. A morpheme is thus defined depending on spaces.
entree_str = [sentence.split(" ") for sentence in entree_str]

database = {}

for i in range(len(entree_str)):
    quote = entree_str[i];
    quoteSize = len(quote)
        
    for j in range(quoteSize):
        solo = False;
        try:
            key = tuple([quote[j], quote[j+1]]);
        except: # IndexError out of bounds : 1-morpheme quote case
            solo = True
            #print("1-morpheme quote found.")
            key = tuple([quote[j], None]);
            
        
    # add a new instance of a morpheme sequence to the database    
    # case 1: if it's the first time this word is encountered
        if not(key in database):           
            # case 1A: end of a sentence
            if (j+2 == quoteSize) or solo:
                database[key] = [1, [None, 1]];
            
            # case 1B: not the end of a sentence
            else:
                database[key] = [1, [quote[j+2], 1]];

    # case 2: if the word was already encountered
    # kind of complex so it's done in a separate function
        else:
            
            # case 2A: end of a sentence
            if (j+2 == quoteSize) or solo:
                newVal = None
            # case 2B : not end of a sentence
            else: 
                newVal = quote[j+2];


            database[key] = newMarkov(database[key], newVal)

        if (j == quoteSize-2):
            break;

# erase the previous parserOutput.in to make sure we're working clean
try:
    os.remove("parserOutput.in")
except FileNotFoundError:
    pass

f = open("parserOutput.in", "a")
f.write(str(database))
f.close()
print("Usable data was successfully parsed into parserOutput.in.")
