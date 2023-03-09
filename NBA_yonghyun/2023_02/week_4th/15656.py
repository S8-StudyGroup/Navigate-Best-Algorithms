# [BOJ] 15656. N과 M (7)
# 소요 시간 : 00분

from collections import deque

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def sequence(arr=[]):
    if len(arr) == m:
        print(*arr)
        return
    for num in nums:
        arr.append(num)
        sequence(arr)
        arr.pop()


sequence()