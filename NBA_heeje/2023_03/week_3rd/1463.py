# [BOJ] 1463. 1로 만들기
# 소요 시간 : 20분

from collections import deque

def bfs():
    visited = set()
    visited.add(N)
    queue = deque()
    queue.append((N, 0))

    while queue:
        num, cnt = queue.popleft()
        
        # 1이 되면 횟수 반환
        if num == 1:
            return cnt
        
        # 세 가지 방법으로 연산 진행
        for calculate in calculation:
            cal_num = calculate(num)
            
            # 양수이고 아직 본 적 없는 숫자일 때만 진행
            if cal_num > 0 and cal_num not in visited:
                visited.add(cal_num)
                queue.append((cal_num, cnt + 1))

# 3 또는 2로 나누어 떨어지지 않을 때는 0을 반환하여 "양수" 부분에서 걸러지게끔 구현
calculation = [
    lambda x: x // 3 if x % 3 == 0 else 0,
    lambda x: x // 2 if x % 2 == 0 else 0,
    lambda x: x - 1,
]

N = int(input())

print(bfs())

