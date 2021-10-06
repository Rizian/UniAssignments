#Score grade output

score = input("Insert score value: ")

if score == 100:
    print("A+")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
elif score >= 50:
    print("E")
elif score < 50:
    print("F")
else:
    print("Invalid Score")