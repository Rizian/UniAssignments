'''
Chessboard 2: Knight's move Boogaloo
Outputs a chessboard layout and then asks user to place a knight unit
Then highlights the square where the knight is and its possible moves.
'''
row = ["1","2","3","4","5","6","7","8"]
col = ["A","B","C","D","E","F","G","H"]

li = []
posMove = []

#This is to reset the chessboard every time
#clears the list and then remakes the predetermined board layout
def resetBoard():
    li.clear()
    for i in range(8):
        li.append([])
        for j in range(8):
            li[i].append(col[j]+row[7-i])
    posMove.clear()

#prints the chessboard
#prints the list values as strings
def printBoard():
    for k in range(8):
        print(" ".join(li[k]))

resetBoard()
printBoard()

while True:
    knight = input("On which square do you want to place a knight >> ").upper()

    #creates a list of possible knight's move positions on the board
    posMove.append(chr(ord(knight[0])-1) + chr(ord(knight[1])+2))
    posMove.append(chr(ord(knight[0])+1) + chr(ord(knight[1])+2))
    posMove.append(chr(ord(knight[0])-2) + chr(ord(knight[1])+1))
    posMove.append(chr(ord(knight[0])+2) + chr(ord(knight[1])+1))
    posMove.append(chr(ord(knight[0])-1) + chr(ord(knight[1])-2))
    posMove.append(chr(ord(knight[0])+1) + chr(ord(knight[1])-2))
    posMove.append(chr(ord(knight[0])-2) + chr(ord(knight[1])-1))
    posMove.append(chr(ord(knight[0])+2) + chr(ord(knight[1])-1))

    #Validates the input of {knight}
    if knight not in li[0] and knight not in li[1] and knight not in li[2] and knight not in li[3] and knight not in li[4] and knight not in li[5] and knight not in li[6] and knight not in li[7]:
        print("Please select a valid chessboard square...")
        posMove.clear()
        continue

    for i in li:
        #Specifies and Highlights the knight's position
        if knight in i:
            j = list(i).index(knight)
            i[j] = "N" + knight
        #highlights the positions of possible knight's moves if found
        for k in i:
            l = list(i).index(k)
            if k in posMove:
                i[l] = f"({k})"
    #prints the new board layout with highlighted squares
    printBoard()
    #continues and resets the program if yes
    again = input("Would you like to select another chessboard tile? (Y/N) >> ").upper()
    if again == "Y":
        resetBoard()
        printBoard()
        continue
    else:
        break
