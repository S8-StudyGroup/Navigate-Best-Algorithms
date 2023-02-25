# [SWEA] 1238. Contact
# 소요 시간 : 20분

from collections import deque

def bfs(start):
    visited = [0] * 101
    visited[start] = 1
    queue = deque()
    queue.append((start, 1))

    while queue:
        v, cnt_contact = queue.popleft()
        for w in adj_list[v]:
            if visited[w] == 0:
                visited[w] = cnt_contact + 1
                queue.append((w, cnt_contact + 1))

    # 가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람 탐색
    ans, last_contact = 0, 0
    for i in range(100, -1, -1):
        if visited[i] > last_contact:
            last_contact = visited[i]
            ans = i
    
    return ans


for tc in range(1, 11):
    length_of_data_list, start = map(int, input().split())
    data_list = list(map(int, input().split()))
    adj_list = [[] for _ in range(101)]

    for i in range(0, length_of_data_list, 2):
        if data_list[i + 1] not in adj_list[data_list[i]]:      # 중복 제거
            adj_list[data_list[i]].append(data_list[i + 1])

    print(f"#{tc} {bfs(start)}")