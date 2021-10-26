row = ["1","2","3","4","5","6","7","8"]
col = ["A","B","C","D","E","F","G","H"]

for i in row[::-1]:
    for j in col:
        print(j+i, end=" ")
    print()
