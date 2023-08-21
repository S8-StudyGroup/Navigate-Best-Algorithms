# [BOJ] 2343. 기타 레슨
# 소요 시간 : 00분

from sys import stdin

readline = lambda : list(map(int, stdin.readline().split()))

num, div = readline()
lectures = readline()

end = sum(lectures)
start = max(lectures)

minval = 0
while end >= start:
    size = (start + end)//2
    now = 0
    cnt = 1
    for i in range(num):
        now += lectures[i]
        if now > size:
            cnt += 1
            now = lectures[i]
            if cnt > div:
                start = size + 1
                break
    else:
        minval = size
        end = size - 1
print(minval)