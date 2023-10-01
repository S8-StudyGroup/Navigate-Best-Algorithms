# [BOJ] 11279. 최대 힙
# 소요 시간 : 00분
import sys
import heapq
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -x)
