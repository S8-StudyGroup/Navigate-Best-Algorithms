# [BOJ] 5639. 이진 검색 트리
# 소요 시간 : 00분

import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

# Input
preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

# postorder
def postorder(root_idx, end_idx):

    if root_idx > end_idx:
        return
    
    mid = end_idx + 1

    for i in range(root_idx + 1, end_idx + 1):
        if preorder[i] > preorder[root_idx]:
            mid = i
            break

    postorder(root_idx + 1, mid - 1)    # 왼쪽
    postorder(mid, end_idx)             # 오른쪽
    print(preorder[root_idx])           # 루트

postorder(0, len(preorder) - 1)