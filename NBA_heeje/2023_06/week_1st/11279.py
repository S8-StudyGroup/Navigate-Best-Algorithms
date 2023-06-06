# [BOJ] 11279. 최대 힙
# 소요 시간 : 00분(16:43 ~ )

import sys
input = sys.stdin.readline

# 노드 위치 교환 함수
def swap(parent, child, flow):
    if parent == 0 or child >= len(tree):
        return 0
    
    # 아래로 내려가면서(pop) 오른쪽 자식 노드가 있는 경우
    if flow == "down" and child + 1 < len(tree):
        if tree[child] > tree[child + 1]:
            if tree[child] > tree[parent]:
                tree[parent], tree[child] = tree[child], tree[parent]
                return child
        
        else:
            if tree[child + 1] > tree[parent]:
                tree[parent], tree[child + 1] = tree[child + 1], tree[parent]
                return child + 1
    
    else:
        if tree[child] > tree[parent]:
            tree[parent], tree[child] = tree[child], tree[parent]
            return child
        
    return 0

# 가장 큰 수 출력 및 제거 함수
def pop():
    if len(tree) == 1:
        answer.append(0)
        
    elif len(tree) == 2:
        answer.append(tree.pop())

    else:
        tree[1], tree[-1] = tree[-1], tree[1]
        answer.append(tree.pop())
        
        parent = 1
        child = 2
        while True:
            flag = swap(parent, child, "down")
            if flag != 0:
                parent = flag
                child = flag * 2
            else:
                break

def append(x):
        tree.append(x)
        child = len(tree) - 1
        parent = child // 2
        while True:
            flag = swap(parent, child, "up")
            if flag != 0:
                child = parent
                parent //= 2
            else:
                break

N = int(input())
tree = [0]
answer = []

for _ in range(N):
    x = int(input())
    if x == 0:
        pop()
    else:
        append(x)

print(*answer, sep="\n")