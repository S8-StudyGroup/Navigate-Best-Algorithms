# [BOJ] 14620. 꽃길
# 소요 시간 : 00분
from itertools import combinations

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def cal_cost(r, c):
    '''
    좌표(r, c)에 꽃을 심었을 때 필요한 대여비용
    '''
    cost = board[r][c]
    for di in range(4):
        nr = r + dr[di]
        nc = c + dc[di]
        cost += board[nr][nc]
    return cost


def diag(a, b):
    '''
    좌표 a, 좌표 b 서로 대각선에 있을 때 == 꽃이 죽는 경우
    '''
    ar, ac = a
    br, bc = b
    if abs(ar - br) + abs(ac - bc) <= 2:
        return True
    return False


flower_cnt = 3
size = int(input())
board = [list(map(int, input().split())) for _ in range(size)]
cost_rc = []

for r in range(1, size-1):
    for c in range(1, size-1):
        cost_rc.append((cal_cost(r, c), (r, c)))

cost_rc.sort()
costsum= 1e9

# 모든 경우에 대해서
for case in combinations(cost_rc, 3):
    a, b, c = case

    # 겹쳐서 안될경우 패스
    if diag(a[1], b[1]) or diag(b[1], c[1]) or diag(a[1], c[1]):
        continue
    
    # 총합
    cost = a[0] + b[0] + c[0]
    if cost < costsum:
        costsum = cost
    
print(costsum)