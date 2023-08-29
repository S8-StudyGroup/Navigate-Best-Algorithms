# [BOJ] 2343. 기타 레슨
# 소요 시간 : 00분

# Input
lec_cnt, blue_cnt = map(int, input().split())
lectures = list(map(int, input().split()))

# 
answer = 0
left, right = max(lectures), sum(lectures)
while left <= right:
    mid = (left+right)//2

    count, sum = 0, 0
    for i in range(lec_cnt):
        if sum + lectures[i] > mid:
            count += 1
            sum = 0
        sum += lectures[i]
    if sum:
        count += 1

    if count > blue_cnt:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid

print(answer)