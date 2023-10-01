# [BOJ] 15900. 나무 탈출
# 소요 시간 : 00분
import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 아이디어 루트 노드 1에서 시작해서
# 모든 리프 노드까지의 거리의 합이 짝수이면 No
# 홀수이면 Yes


def bfs():
    distance = [0] * (n+1)
    total_distance_leaf = 0
    queue = deque([1])
    while queue:
        node = queue.popleft()
        child = 0
        for next_node in tree[node]:
            if distance[next_node] == 0 and next_node != 1:
                child += 1
                distance[next_node] = distance[node] + 1
                queue.append(next_node)

        if child == 0:
            total_distance_leaf += distance[node]

    return total_distance_leaf


distance = bfs()

print('No' if distance % 2 == 0 else 'Yes')
