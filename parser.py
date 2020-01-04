# This parser makes an association between a word and a list of
# couple [words, probability] which can potentially follow it.
# Also the list of couples starts with a number : the total
# amount of occurence (just some complexity improving shenanigans)

# The data is parsed from the scripts in the data/dataSets folder


import fileinput


def newMarkov(curVal, newVal):

    for i in range(1, len(curVal)):
        if curVal[i][0] == newVal:
            curVal[i][1] += 1;
            curVal[0] += 1
            return curVal;

    curVal.append([newVal, 1])
    curVal[0] += 1
    return curVal

# On récupère les lignes de l'entrée en supprimant les caractères blancs :
entree_str = [line.strip() for line in fileinput.input("data\dataSets\s4ep1.in")]

# space division
entree_str = [sentence.split(" ") for sentence in entree_str]

database = {}

for i in range(len(entree_str)):
    quote = entree_str[i];
    quoteSize = len(quote)
    for j in range(quoteSize):
        key = quote[j];
        
        # if the word was already encountered
        # kind of complex so it's done in a separate function
        if key in database:
            
            # end of a sentence
            if j+1 == quoteSize:
                newVal = None
            else:
                newVal = quote[j+1];


            database[key] = newMarkov(database[key], newVal)
            
        
        # if it's the first time this word is encountered
        else:
            
            # end of a sentence
            if j+1 == quoteSize:
                database[key] = [1, [None, 1]];
            
            # not the end of a sentence
            else:
                database[key] = [1, [quote[j+1], 1]];



#print(entree_str)

f = open("parserOutput.in", "a")
f.write(str(database))
f.close()
