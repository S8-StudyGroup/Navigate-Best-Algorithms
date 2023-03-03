# [Programmers] 43105. 정수 삼각형
# 소요 시간 : 00분

def solution(triangle):
    answer = 0

    for row in range(1, len(triangle)):
        for idx in range(len(triangle[row])):
            if idx == 0:
                triangle[row][idx] += triangle[row-1][0]
            elif idx == len(triangle[row]) - 1:
                triangle[row][idx] += triangle[row-1][-1]
            else:
                triangle[row][idx] += max(triangle[row-1][idx-1], triangle[row-1][idx])

    answer = max(triangle[-1])

    return answer