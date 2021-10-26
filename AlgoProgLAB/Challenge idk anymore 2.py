'''
Addition by specific base-value for value <=10
'''
def base_add(k = 10, x = int, *args):
    convert = []
    sum = x
    for y in args:
        sum += y
    while True:
        if sum >= k:
            i = sum % k
            convert.append(str(i))
            sum //= k
            continue
        break
    convert.append(str(sum))
    convert.reverse()
    z = ''.join(convert)
    print(z)