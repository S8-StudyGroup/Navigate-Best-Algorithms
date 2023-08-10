# [BOJ] 5639. 이진 검색 트리
# 소요 시간 : 60분
import sys
sys.setrecursionlimit(10000)

tree = []
while True:
    try:
        num = int(input())
        tree.append(num)
    except:
        break


def postorder(first, end):
    if first > end:
        return
    mid = end + 1
    for i in range(first + 1, end + 1):
        if tree[first] < tree[i]:
            mid = i
            break
    postorder(first + 1, mid - 1)
    postorder(mid, end)
    print(tree[first])


postorder(0, len(tree)-1)
