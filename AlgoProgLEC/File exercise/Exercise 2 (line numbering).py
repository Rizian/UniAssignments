"""
Write a program that given a text file will create a new text file in which all the lines from the original file are numbered from 1 to n (where n is the number of lines in the file).
"""
import os

def main():
    #Changes the working directory to the directory as this program
    directory = os.path.dirname(__file__)
    os.chdir(directory)
    print(os.getcwd())
    filename = str(input("Which text file would you like to access?\n(make sure the file is in the same folder as this program)\n>> ",))

    inputFile = open(filename+".txt", "r")
    #stores the list created by readlines()
    filelines = inputFile.readlines()

    #Creates a new txt file to output to
    outputFile = open("output.txt", "w")
    #Variable to indicate the line number in the output file
    linecount = 1

    #for loop to print all the lines in the filelines list into the new file preceeded by the line number
    for line in filelines:
        print(f"{linecount}. {line}", end="", file=outputFile)
        linecount += 1
    
    #closes both files after it is done
    inputFile.close()
    outputFile.close()

if __name__ == "__main__":
    main()