# [BOJ] 1967. 트리의 지름
# 소요 시간 : 00분
import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))


def dfs(node, visited, path):
    global answer, leaf_node

    # leaf node
    if len(tree[node]) == 1 and node != leaf_node:
        if path > answer:
            leaf_node = node
            answer = path
        return

    for next_node, value in tree[node]:
        if next_node not in visited:
            visited.add(next_node)
            dfs(next_node, visited, path + value)
            visited.remove(next_node)


answer = 0
leaf_node = 1

visited = set()
visited.add(1)
dfs(1, visited, 0)

visited = set()
visited.add(leaf_node)
dfs(leaf_node, visited, 0)

print(answer)
