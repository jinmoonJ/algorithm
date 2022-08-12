def strlen(a):
    str = 0 # 문자열 개수 정해줄 변수
    
    while a[str] != "\0":
        str += 1
    return str

a = ["a", "b", "c", "\0"]
print(strlen(a))