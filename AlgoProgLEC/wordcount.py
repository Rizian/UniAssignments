"""
Writes a program that counts the number of times a word occured in a sentence.
"""

def getWord(sentence = str):
    wordDict = {}
    words = sentence.split()

    for word in words:
        wordDict[word] = wordDict.get(word, 0)+1

    return wordDict
    
sentence = input("Enter a sentence:\n")

wordCount = getWord(sentence)

for key in sorted(wordCount):
    print(f"{wordCount[key]}: {key}")