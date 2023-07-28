# [BOJ] 15900. 나무 탈출
# 소요 시간 : 60분

# 루트에서 각 리프가는 간선 수
# 또는
# 반대 수를 체크해서 홀짝
import sys
sys.setrecursionlimit(500000)

node_num = int(input())
edges = [[] for _ in range(node_num + 1)]
for _ in range(node_num - 1):
    a, b = map(int, sys.stdin.readline().split())
    edges[a].append(b)
    edges[b].append(a)
cnt = 0
passed = [False for _ in range(node_num + 1)]


def find_leaf(n, count):
    global cnt
    passed[n] = True
    if not edges[n]:
        cnt += count
        return
    temp_cnt = 0
    for c in edges[n]:
        if not passed[c]:
            find_leaf(c, count + 1)
        else:
            temp_cnt += 1
    if temp_cnt == len(edges[n]):
        cnt += count
        return


find_leaf(1, 0)
if cnt % 2 == 0:
    print('No')
else:
    print('Yes')