# [BOJ] 20924. 트리의 기둥과 가지
# 소요 시간 : 00분

import sys
sys.setrecursionlimit(10**9)

import sys
from collections import defaultdict

input = sys.stdin.readline


def find_root_to_giga(node, length):
    if (
        not tree[node]
        or (node != R and len(tree[node]) == 1)
        or (node == R and len(tree[node]) > 1)
        or len(tree[node]) > 2
    ):
        return node, length
    else:
        for child in tree[node]:
            if not visited[child[0]]:
                visited[child[0]] = True
                return find_root_to_giga(child[0], length + child[1])


def find_max_length(parent, length):
    if len(tree[parent]) == 1:
        global max_length
        max_length = max(max_length, length)
        return

    for child, len_child in tree[parent]:
        if not visited[child]:
            visited[child] = True
            find_max_length(child, length + len_child)
            visited[child] = False


N, R = map(int, input().split())
tree = defaultdict(list)

for _ in range(N - 1):
    a, b, d = map(int, input().split())
    tree[a].append((b, d))
    tree[b].append((a, d))

visited = defaultdict(bool)
visited[R] = True

node, length_root_to_giga = find_root_to_giga(R, 0)

max_length = 0

find_max_length(node, 0)

print(length_root_to_giga, max_length)
