# [BOJ] 2533. 사회망 서비스(SNS)
# 소요 시간 : 00분
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

# Input
node_cnt = int(input())
graph = [[] for _ in range(node_cnt + 1)]
for _ in range(node_cnt - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# dfs, dp
# 어답터일경우, 아닐경우
dp = [[0, 0] for _ in range(node_cnt + 1)]
visited = [False] * (node_cnt + 1)


def dfs(node=1):
    visited[node] = True
    dp[node][0] = 1
    for child_node in graph[node]:
        if not visited[child_node]:
            dfs(child_node)
            dp[node][0] += min(dp[child_node][0], dp[child_node][1])
            dp[node][1] += dp[child_node][0]


dfs()

# Output
answer = min(dp[1][0], dp[1][1])
print(answer)













### 다른사람풀이

import sys
input = sys.stdin.readline

n = int(input())

edge = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)

selectVertex = set()
visited = [0] + [0] * n

queue = []

for i in range(1, n+1):
    if(len(edge[i]) == 1): # 연결된 edge가 하나라면
        queue.append(i)
        
while(queue):
    cur = queue.pop()

    if(visited[cur]):
        continue

    sVertex = edge[cur][0]
    selectVertex.add(sVertex)

    for v in edge[sVertex] + []:
        edge[sVertex].remove(v)
        edge[v].remove(sVertex)
        
        if(len(edge[v]) == 1 and visited[v] == 0):
            queue.append(v)
        
        if(len(edge[v]) == 0):
            visited[v] = 1
    
    visited[sVertex] = 1


print(len(selectVertex))
