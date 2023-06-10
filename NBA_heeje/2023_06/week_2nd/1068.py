# [BOJ] 1068. 트리
# 소요 시간 : 60분

import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def sol():
    def bfs(root, del_node):

        # 루트 노드가 삭제되는 경우
        if root == del_node:
            return 0
        
        queue = deque()
        queue.append(root)
        cnt_leaf = 0

        while queue:
            parent = queue.popleft()

            if nodes[parent]:
                # 자식 노드가 1개이고, 삭제되는 경우
                if nodes[parent] == [del_node]:
                    cnt_leaf += 1
                else:
                    for child in nodes[parent]:

                        # 삭제할 노드가 아닌 경우
                        if child != del_node:
                            queue.append(child)
            
            # 리프 노드인 경우
            else:
                cnt_leaf += 1

        return cnt_leaf

    N = int(input())
    nodes = defaultdict(list)
    for idx, node in enumerate(list(map(int, input().split()))):
        if node == -1:
            root = idx
        nodes[node].append(idx)

    print(bfs(root, int(input())))

sol()
