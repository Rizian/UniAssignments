"""
A sentence splitter is a program capable of splitting a text into sentences. The standard set of heuristics for sentence splitting includes (but isn't limited to) the following rules:
Sentence boundaries occur at one of "." (periods), "?" or "!", except that .
Periods followed by whitespace followed by a lower case letter are not sentence boundaries.
a) Periods followed by a digit with no intervening whitespace are not sentence boundaries.
b) Periods followed by whitespace and then an upper case letter, but preceded by any of short list of titles are not sentence boundaries.
c) Sample titles include Mr., Mrs., Dr., and so on.
d) Periods internal to a sequence of letters with no adjacent whitespace are not sentence boundaries
e) (for example, www.aptex.com, or e.g).
f) Periods followed by certain kinds of punctuation (notably comma and more periods) are probably not sentence boundaries.
"""
import os

titles = ["Mr.", "Ms.", "Mrs.", "Dr.", "Prof."]

def splitSentence(filename):
    #appends the text file with the extension and reads it
    file = open(filename+".txt", "r")
    filedata = file.read()
    words = filedata.split()    #Splits the sentences into a list of words/strings
    
    count = 0   #incremented counter to indicate the index of list 'words
    #for loop to check and apply spaces and newlines where appropriate. Excludes the last word as it is unecessary to format.
    for i in words[:-1]:
        if i in titles or i.endswith("..."):
            words[count] = i + " "
        elif i.endswith(".") or i.endswith("?") or i.endswith("!"):
            if words[count + 1][0].isupper():
                words[count] = i + "\n"
            else:
                words[count] = i + " "
        else:
            words[count] = i + " "
        count += 1

    file.close()    #closes the file

    return ''.join(words)   #joins the list together into a string

def main():
    #Changes the working directory to the directory as this program
    directory = os.path.dirname(__file__)
    os.chdir(directory)
    print(os.getcwd())

    #lets the user enter the file name, no need to input the file extension in the input
    filename = str(input("Which text file would you like to access?\n(make sure the file is in the same folder as this program)\n>> ",))

    print(splitSentence(filename))


if __name__ == "__main__":
    main()