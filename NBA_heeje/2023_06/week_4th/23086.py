# [BOJ] 23086. 두 반으로 나누기
# 소요 시간 : 90++분

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    visited = [False] * (N + 1)
    visited[1] = True
    cur_class = 0
    class_list = [set(), set()]
    queue = deque()
    queue.append(1)
    class_list[cur_class].add(1)
    
    while queue:
        cur_class = 0 if cur_class == 1 else 1
        for _ in range(len(queue)):
            node = queue.popleft()
            for c_node in adj_list[node]:
                if visited[c_node] and c_node not in class_list[cur_class]:
                    return []
                if not visited[c_node]:
                    visited[c_node] = True
                    class_list[cur_class].add(c_node)
                    queue.append(c_node)
    
    return class_list




N, M, K = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]
bf_list = []
remove_bf_list = []
remove_bf_set = set()
cnt_remove = K

for _ in range(M):
    u, v = map(int, input().split())
    bf_list.append((u, v))

for _ in range(K):
    R = int(input())
    remove_bf_list.append(R - 1)
    remove_bf_set.add(R - 1)

for idx, bf in enumerate(bf_list):
    if idx not in remove_bf_set:
        adj_list[bf[0]].append(bf[1])
        adj_list[bf[1]].append(bf[0])

class_list = bfs()
if class_list:
    for i in range(len(remove_bf_list) - 1, -1, -1):
        f1, f2 = bf_list[remove_bf_list[i]]
        if (f1 in class_list[0] and f2 in class_list[0]) or (f1 in class_list[1] and f2 in class_list[1]):
            break
        else:
            cnt_remove -= 1
    
    print(cnt_remove)
    print(*sorted(list(map(lambda x: len(x), class_list))))
else:
    print(-1)
