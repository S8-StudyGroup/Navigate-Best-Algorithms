# [BOJ] 16987. 계란으로 계란치기
# 소요 시간 : 00분


def dfs(idx, cnt_broken):
    # 모든 계란에 대하여 과정을 진행하였다면 종료
    if idx == N:
        global max_cnt_broken_egg
        max_cnt_broken_egg = max(max_cnt_not_broken_egg, cnt_broken)
        return

    # 집은 계란이 깨져있다면 생략   
    if egg_info_list[idx][0] <= 0:
        dfs(idx + 1, cnt_broken)
        return

    cnt = 0
    for egg_idx, egg_info in enumerate(egg_info_list):
        if egg_idx == idx or egg_info[0] <= 0:
            cnt += 1
            continue

        # 박치기 작업
        egg_info_list[egg_idx][0] -= egg_info_list[idx][1]
        egg_info_list[idx][0] -= egg_info_list[egg_idx][1]

        dfs(idx + 1, cnt_broken + int(egg_info_list[egg_idx][0] <= 0) + int(egg_info_list[idx][0] <= 0))

        # 박치기 작업 복구
        egg_info_list[egg_idx][0] += egg_info_list[idx][1]
        egg_info_list[idx][0] += egg_info_list[egg_idx][1]
    
    if cnt == N:
        max_cnt_not_broken_egg = max(max_cnt_not_broken_egg, N - 1)

N = int(input())
egg_info_list = [list(map(int, input().split())) for _ in range(N)]
max_cnt_broken_egg = 0

dfs(0, 0)
print(max_cnt_broken_egg)