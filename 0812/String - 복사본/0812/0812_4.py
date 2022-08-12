str1 = "abcd"
str2 = "efg"
print(my_strcmp(str1, str2))


\
def my_strcmp(str1, str2):
    if str1 == str2:
        return 0
    for i in len(str1):
        for j in len(str2):