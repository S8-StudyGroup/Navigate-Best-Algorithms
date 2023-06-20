# [BOJ] 20924. 트리의 기둥과 가지
# 소요 시간 : 00분
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def find_pole_length(node):
    global pole, G
    if not tree[node] or len(tree[node]) > 1:
        G = node
        return

    pole += tree[node][0][1]
    find_pole_length(tree[node][0][0])


def find_max_branch_length(node, cur_length):
    global branch

    if not tree[node]:
        if cur_length > branch:
            branch = cur_length
        return

    for next_node, length in tree[node]:
        find_max_branch_length(next_node, cur_length + length)


N, R = map(int, input().split())
tree = [[] for _ in range(N+1)]
G = 0
pole = 0
branch = 0

for _ in range(N-1):
    a, b, d = map(int, input().split())
    tree[a].append((b, d))

find_pole_length(R)

find_max_branch_length(G, 0)

print(pole, branch)
