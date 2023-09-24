# [Programmers] 12946. 하노이의 탑
# 소요 시간 : 00분
def solution(n):
    def dp(n, start, through, end):
        if n == 1:
            return [[start, end]]
        result = []
        result.extend(dp(n - 1, start, end, through))
        result.append([start, end])
        result.extend(dp(n - 1, through, start, end))
        return result

    return dp(n, 1, 2, 3)
