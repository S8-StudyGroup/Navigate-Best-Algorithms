# [BOJ] 20365. 블로그2
# 소요 시간 : 20분

N = int(input())
info = input()

main = info[0]
current = info[0]
cnt = 1

for i in range(N):
    if info[i] != current:
        current = info[i]
        if info[i] != main:
            cnt += 1

print(cnt)
