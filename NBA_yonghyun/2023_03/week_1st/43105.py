# [Programmers] 43105. 정수 삼각형
# 소요 시간 : 00분

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]


def solution(triangle):
    depth = 1
    while depth < len(triangle):
        for i in range(depth + 1):
            if i == 0:
                triangle[depth][0] += triangle[depth - 1][0]
            elif i == depth:
                triangle[depth][i] += triangle[depth - 1][i - 1]
            else:
                if triangle[depth - 1][i - 1] <= triangle[depth - 1][i]:
                    triangle[depth][i] += triangle[depth - 1][i]
                else:
                    triangle[depth][i] += triangle[depth - 1][i - 1]
        depth += 1
    return max(triangle[depth - 1])