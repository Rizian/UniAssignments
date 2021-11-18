'''
Converts an int value to a different counting base
'''

def base_convert(base = 10, sum = int):
    convert = []
    while True:
        if sum >= base:
            i = sum % base
            sum //= base
            if i >= 10:
                i = chr(55+i)
            convert.append(str(i))
            continue
        break
    if sum >= 10:
        sum = chr(55+sum)
    convert.append(str(sum))
    convert.reverse()
    out = ''.join(convert)
    return out

base = int(input("Enter a base value:\n>> "))
num = int(eval(input("Enter a number here:\n(simple math calculations allowed (+,-,*,**,/,//))\n>> ")))

converted_num = base_convert(base, num)

print(f"base 10: {num}")
print(f"base {base}: {converted_num}")