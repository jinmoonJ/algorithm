def itoa(a):
    b = len(a)
    print(b)
    n = " "
    for i in range(b):
        n += chr(a[i])
    return n

a = 100
print(itoa(a))