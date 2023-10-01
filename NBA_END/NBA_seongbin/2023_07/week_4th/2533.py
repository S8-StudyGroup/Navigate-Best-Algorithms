# [BOJ] 2533. 사회망 서비스(SNS)
# 소요 시간 : 00분
import sys
sys.setrecursionlimit(10**9)
# sys.stdin = open('input.txt')
input = sys.stdin.readline


def dfs(node):
    visited[node] = True
    if len(graph[node]) == 0:
        dp[node][1] = 1
        dp[node][0] = 0
    else:
        for next_node in graph[node]:
            if not visited[next_node]:
                dfs(next_node)
                dp[node][1] += min(dp[next_node][0], dp[next_node][1])
                dp[node][0] += dp[next_node][1]
        dp[node][1] += 1


n = int(input())
graph = [[] for _ in range(n + 1)]
dp = [[0, 0] for i in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)

dfs(1)

print(min(dp[1][0], dp[1][1]))
