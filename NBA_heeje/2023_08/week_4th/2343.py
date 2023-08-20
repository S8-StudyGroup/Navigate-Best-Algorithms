# [BOJ] 2343. 기타 레슨
# 소요 시간 : 30분

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lessons = list(map(int, input().split()))

max_length = max(lessons)
start = 1
end = 10 ** 9
answer = end

while start <= end:
    mid = (start + end) // 2

    if mid < max_length:
        start = mid + 1
        continue

    sum = 0
    cnt = 1
    for i in range(N):
        if sum + lessons[i] > mid:
            cnt += 1
            sum = lessons[i]

            if cnt > M:
                start = mid + 1
                break
        
        else:
            sum += lessons[i]
    else:
        end = mid - 1
        answer = min(answer, mid)

print(answer)