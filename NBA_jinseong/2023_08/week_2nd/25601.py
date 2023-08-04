# [BOJ] 25601. 자바의 형변환
# 소요 시간 : 20분
from collections import deque
import sys

n = int(sys.stdin.readline())
rel = dict()
for i in range(n - 1):
    child, parent = sys.stdin.readline().split()
    if parent not in rel:
        rel[parent] = [child]
    elif child not in rel[parent]:
        rel[parent].append(child)

one, two = sys.stdin.readline().split()
ans = 0


def bfs(node, o): # node에서 넓이우선으로 child 탐색
    queue = deque()
    queue.extend(rel[node])
    while queue:
        now = queue.popleft()
        if now == o:
            return True
        if now in rel:
            queue.extend(rel[now])
    return False


if one in rel:
    if bfs(one, two):
        ans = 1
if two in rel:
    if bfs(two, one):
        ans = 1
print(ans)