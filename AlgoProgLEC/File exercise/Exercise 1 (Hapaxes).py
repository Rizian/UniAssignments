"""
A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a language, the works of an author, or in a single text.
Define a function that given the file name of a text will return all its hapaxes.
"""
import string
import os
import unicodedata

def removePunc(s):
    #transforms the string into lowercase
    s = s.lower()
    #normalizes accented characters
    s = str.casefold(s)
    #normalizes the unicode encoding
    s = unicodedata.normalize('NFC', s)
    #removes the punctuation in the string
    out = s.translate(str.maketrans('â€”', ' - ', string.punctuation))
    return out

def getHapax(filename):
    #stores and counts the individual words in WordList
    wordDict = {}
    #list for storing hapaxes
    hapaxList = []
    #appends the text file with the extension and reads it
    file = open(filename+".txt", "r")
    #separates the individual words into a list
    filewords = removePunc(file.read())
    wordList = filewords.split()
    file.close()

    for word in wordList:
        wordDict[word] = wordDict.get(word, 0)+1

    for key, value in wordDict.items():
        if  value == 1:
            hapaxList.append(key)
    
    return hapaxList

def main():
    #Changes the working directory to the directory as this program
    directory = os.path.dirname(__file__)
    os.chdir(directory)
    print(os.getcwd())
    filename = str(input("Which text file would you like to access?\n(make sure the file is in the same folder as this program)\n>> ",))
    hapaxList = getHapax(filename)
    newFile = open("hapaxes.txt", "w")
    for word in hapaxList:
        #prints the results both in console and into a txt file
        print(word)                 #console
        print(word, file=newFile)   #txt file
    newFile.close()

if __name__ == "__main__":
    main()