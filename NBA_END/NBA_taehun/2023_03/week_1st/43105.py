# [Programmers] 43105. 정수 삼각형
# 소요 시간 : 00분

# 점점 누적하면서 찾기
def solution(triangle):
    global arr
    L = len(triangle)
    for row in range(L-1):
        arr = triangle[row]
        for idx, value in enumerate(triangle[row + 1]):
            prev_idx1, prev_idx2 = idx - 1, idx
            
            prev_v1, prev_v2 = check_range(row, prev_idx1, prev_idx2)
            
            # 더 큰값 선택
            triangle[row+1][idx] = max(value + prev_v1, value + prev_v2)
    return max(triangle[-1])

# 범위를 벗어나는 경우 확인
def check_range(row, prev_idx1, prev_idx2):
    if prev_idx1 < 0:
        prev_v1 = 0
    else:
        prev_v1 = arr[prev_idx1]
    if row < prev_idx2:
        prev_v2 = 0
    else:
        prev_v2 = arr[prev_idx2]
    return prev_v1, prev_v2

    

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))