s1 = "abc"
s2 = "abc"
s3 = "def"
s4 = s1
s5 = s1[:2] + "c"

print(s1 is s2)
print(s1, s2)

print(s1 is s3)
print(s1, s3)

print(s1 is s4)
print(s1,s4)

print(s1 is s5)
print(s1,s5)

def my_strcmp(str1, str2):
    a = str1
    b = str2
    if a == b:
        return 0
    elif ord(a[0]) < ord(b[0]):
        return -1
    elif ord(a[0]) > ord(b[0]):
        return 1

