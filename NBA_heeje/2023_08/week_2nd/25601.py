# [BOJ] 25601. 자바의 형변환
# 소요 시간 : 20분

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def bfs(classes):
    queue = deque()
    queue.extend(classes)

    while queue:
        cls = queue.popleft()
        for s_class in adj_dict[cls]:
            if s_class in classes:
                return 1
            else:
                queue.append(s_class)
    
    return 0

N = int(input())
adj_dict = defaultdict(list)

for _ in range(N - 1):
    A, B = input().split()
    adj_dict[B].append(A)

classes = input().split()

print(bfs(classes))
