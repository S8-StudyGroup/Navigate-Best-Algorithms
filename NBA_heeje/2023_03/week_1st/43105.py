# [Programmers] 43105. 정수 삼각형
# 소요 시간 : 20분

def solution(triangle):

    memo = [[0] * (i + 1) for i in range(len(triangle))]
    memo[0][0] = triangle[0][0]

    for i in range(len(memo) - 1):
        for j in range(len(memo[i])):

            # 현재까지의 합과 아래 칸 숫자를 합해주고, 저장되어 있는 값과 비교하여 최댓값으로 갱신
            memo[i + 1][j] = max(memo[i + 1][j], memo[i][j] + triangle[i + 1][j])

            # 현재까지의 합과 대각선 아래 칸 숫자를 합해주고, 저장되어 있는 값과 비교하여 최댓값으로 갱신
            memo[i + 1][j + 1] = max(memo[i + 1][j + 1], memo[i][j] + triangle[i + 1][j + 1])

    # print(memo)

    return max(memo[-1])

# print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))