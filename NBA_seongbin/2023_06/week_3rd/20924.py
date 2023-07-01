# [BOJ] 20924. 트리의 기둥과 가지
# 소요 시간 : 00분
import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find_pole_length(node):
    global G, pole
    visited[node] = True

    # leaf node
    if len(tree[node]) == 1 and visited[tree[node][0][0]]:
        G = node

    # giga node
    if len(tree[node]) > 2 or (len(traee[node]) == 2 and node == R):
        G = node
        return

    # find pole
    for next_node, length in tree[node]:
        if not visited[next_node]:
            pole += length
            find_pole_length(next_node)


def find_max_branch_length(node, length):
    global branch

    # 종료 조건
    if len(tree[node]) == 1 and visited[tree[node][0][0]]:
        branch = max(branch, length)
        return

    # 재귀
    for next_node, next_length in tree[node]:
        if not visited[next_node]:
            visited[next_node] = True
            find_max_branch_length(next_node, length + next_length)
            visited[next_node] = False


N, R = map(int, input().split())
tree = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
G = R
pole = 0
branch = 0

for _ in range(N - 1):
    a, b, d = map(int, input().split())
    tree[a].append((b, d))
    tree[b].append((a, d))

find_pole_length(R)
find_max_branch_length(G, 0)
print(pole, branch)
