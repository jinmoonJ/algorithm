p = "is"
t = "This is a book~!" # 전체 텍스트
M = len(p) # 찾을 패턴의 길이
N = len(t) # 전체 텍스트의 길이

def BruteForce(p,t):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    while j < M and i < N:
        if t[i] != p[j]: # t인덱스가 P인덱스와 다르면
            i = i - j 
            j = -1
        i = i + 1
        j = j + 1
    if j == M : return i - M # 검색 성공
    else: return -1 # 검색 실패

print(BruteForce(p, t))