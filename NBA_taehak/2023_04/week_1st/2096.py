# [BOJ] 2096. 내려가기
# 소요 시간 : 00분
rowCnt = int(input())

x0 = x1 = x2 = 0
n0 = n1 = n2 = 0

for _ in range(rowCnt):
    a, b, c = map(int, input().split())

    nn0 = a + min(n0, n1)
    nn1 = b + min(n0, n1, n2)
    nn2 = c + min(n1, n2)
    nx0 = a + max(x0, x1)
    nx1 = b + max(x0, x1, x2)
    nx2 = c + max(x1, x2)

    n0 = nn0
    n1 = nn1
    n2 = nn2
    x0 = nx0
    x1 = nx1
    x2 = nx2

print(max(x0, x1, x2), min(n0, n1, n2))