# [BOJ] 20924. 트리의 기둥과 가지
# 소요 시간 : 00분
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

node_cnt, root_node = map(int, input().split())
graph = [[] for _ in range(node_cnt + 1)]
visited = [False] * (node_cnt + 1)
trunk = 0
branch_max = 0
giganode = root_node


for _ in range(node_cnt - 1):
    a_node, b_node, ab_len = map(int, input().split())
    graph[a_node].append((b_node, ab_len))
    graph[b_node].append((a_node, ab_len))


def get_giganode(node, len_sum=0):
    global trunk, giganode

    visited[node] = True
    trunk = len_sum

    if len_sum == 0 and len(graph[node]) == 2:
        return

    if len(graph[node]) > 2:
        giganode = node
        return

    for node_num, node_len in graph[node]:
        if visited[node_num]:
            continue

        get_giganode(node_num, len_sum + node_len)
        break


get_giganode(root_node)


def get_branch_max(node, len_sum=0):
    global branch_max

    visited[node] = True

    if len(graph[node]) == 1:
        branch_max = max(branch_max, len_sum)
        return

    for node_num, node_len in graph[node]:
        if visited[node_num]:
            continue

        get_branch_max(node_num, len_sum + node_len)


get_branch_max(giganode)
print(trunk, branch_max)