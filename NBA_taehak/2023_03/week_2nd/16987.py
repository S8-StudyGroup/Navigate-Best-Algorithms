# [BOJ] 16987. 계란으로 계란치기
# 소요 시간 : 00분
n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
result = 0


def check(egg_num):
    global result
    # 종료 조건 1: 가장 끝 계란
    if egg_num == n:
        break_cnt = 0
        for idx in range(n):
            if eggs[idx][0] <= 0:
                break_cnt += 1
        result = max(result, break_cnt)
        return
    
    # 깨진 경우는 다음 계란으로
    if eggs[egg_num][0] <= 0:
        check(egg_num + 1)
        return

    # 종료 조건 2: 1개 빼고 다 깨진경우
    nomore = True
    for idx in range(n):
        if idx == egg_num:
            continue
        if eggs[idx][0] > 0:
            nomore = False
            break
    if nomore:
        result = max(result, n - 1)
        return
    
    # 때려보기
    for target_idx in range(n):
        if target_idx == egg_num:
            continue
        if eggs[target_idx][0] <= 0:
            continue
        eggs[egg_num][0] -= eggs[target_idx][1]
        eggs[target_idx][0] -= eggs[egg_num][1]
        check(egg_num + 1)
        eggs[egg_num][0] += eggs[target_idx][1]
        eggs[target_idx][0] += eggs[egg_num][1]
        

check(0)
print(result)