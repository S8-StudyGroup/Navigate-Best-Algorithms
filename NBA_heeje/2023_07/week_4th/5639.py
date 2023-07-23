# [BOJ] 5639. 이진 검색 트리
# 소요 시간 : 70분

import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)

def post_order(start, end):
    if start >= end:
        print(pre_order[start])
        return
    
    # 한쪽 가지만 있는 경우
    if pre_order[start] > pre_order[end] or pre_order[start] < pre_order[start + 1]:
        post_order(start + 1, end)
        print(pre_order[start])
        return

    mid = end + 1
    for i in range(start + 1, end + 1):
        if pre_order[start] < pre_order[i]:
            mid = i
            break
    
    post_order(start + 1, mid - 1)
    post_order(mid, end)
    print(pre_order[start])


tree = [[0] * 2 for _ in range(10001)]
pre_order = []
while True:
    try:
        pre_order.append(int(input()))
    except:
        break


post_order(0, len(pre_order) - 1)
