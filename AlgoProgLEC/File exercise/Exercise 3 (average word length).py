"""
Write a program that will calculate the average word length of a text stored in a file
(i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens).
"""
import os
import string

def removePunc(s):
    #transforms the string into lowercase
    s = s.lower()

    #removes the punctuation in the string
    out = s.translate(str.maketrans('', '', string.punctuation))
    return out

def averageWordLength(filename):
    #appends the text file with the extension and reads it
    file = open(filename+".txt", "r")
    filewords = removePunc(file.read())
    wordlist = filewords.split()

    #counters for characters and words
    charcount = 0
    wordcount = 0

    for word in wordlist:
        charcount += len(word)
        wordcount += 1

    #calculates the average word length
    wordlength = charcount / wordcount
    file.close()
    print(wordlist)
    return wordlength


def main():
    #Changes the working directory to the directory as this program
    directory = os.path.dirname(__file__)
    os.chdir(directory)
    print(os.getcwd())

    filename = str(input("Which text file would you like to access?\n(make sure the file is in the same folder as this program)\n>> ",))
    wordlen = averageWordLength(filename)

    print(f"The average word length in this text file is {wordlen:.2f} characters.")

if __name__ == "__main__":
    main()