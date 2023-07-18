# [BOJ] 10836. 여왕벌
# 소요 시간 : 00분
import sys
input = sys.stdin.readline

size, n = map(int, input().split())

worm = [1]*(2*size-1)

for day in range(n):
    a, b, c = map(int, input().split())
    for idx in range(a, a+b):
        worm[idx] += 1
    for idx in range(a+b, 2*size-1):
        worm[idx] += 2

right = ' '.join(map(str, worm[size:]))
for idx in range(size-1,-1,-1):
    print(worm[idx], right)