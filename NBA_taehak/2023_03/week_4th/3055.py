# [BOJ] 3055. 탈출
# 소요 시간 : 00분
rsize, csize = map(int, input().split())
area = [input() for _ in range(rsize)]

result = 'KAKTUS'

for r in range(rsize):
    for c in range(csize):
        if area[r][c] == 'D':
            beaver = (r, c)
        elif area[r][c] == 'S':
            target = (r, c)
        elif area[r][c] == '*':
            water_source = (r, c)


def inrange(r, c):
    '''
    r: 행
    c: 열
    output: 범위안에 있으면 True 아니면 False
    '''
    if 0 <= r < rsize and 0 <= c < csize:
        return True
    else:
        return False


def bfs(beaver, target, water_source):
    beaver_visited = [[False] * csize for _ in range(rsize)]    
    water_visited = [[False] * csize for _ in range(rsize)]
