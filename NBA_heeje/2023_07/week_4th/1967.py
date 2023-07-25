# [BOJ] 1967. 트리의 지름
# 소요 시간 : 00분

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10100)

def find_max_length(n, length):
    if not tree[n]:
        return length
    lengths = []
    for child, weight in tree[n]:
        lengths.append(find_max_length(child, weight))
    
    lengths.sort()
    global max_length
    max_length = max(max_length, sum(lengths[-2:]))
    return lengths[-1] + length


n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))

max_length = 0
find_max_length(1, 0)

print(max_length)
    