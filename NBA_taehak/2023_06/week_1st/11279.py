# [BOJ] 11279. 최대 힙
# 소요 시간 : 00분
import sys
from heapq import heappop, heappush
input = sys.stdin.readline


cal_cnt = int(input())
nums = []

for _ in range(cal_cnt):
    num = int(input())

    if num == 0:
        if nums:
            print(-heappop(nums))
        else:
            print(0)
    else:
        heappush(nums, -num)
