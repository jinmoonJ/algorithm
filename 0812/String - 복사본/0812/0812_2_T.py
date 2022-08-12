
# swap
def my_reverse(s):
    n = len(s)
    s_list = list(s)

    for i in range(n//2):
        s_list[i], s_list[n-1-i] = s_list[n-1-i], s_list[i]
        # new_s = "".join(s_list)
        new_s = ""
        for c in s_list:
            new_s += c
        return new_s

s = "abcdefg"
print(my_reverse(s))
