# [Programmers] 43105. 정수 삼각형
# 소요 시간 : 60분

# triangle => [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

def solution(triangle):

    max_line = [triangle[0][0]]
    n = 1
    while n < len(triangle):
        before = max_line[:]
        line = triangle[n][:]
        max_line = []
        i = 0
        while i <= n:
            if i == 0:
                max_line.append(line[0] + before[0])
            elif i == n:
                max_line.append(line[i] + before[i-1])
            else:
                max_line.append(line[i] + max(before[i-1:i+1]))
            i += 1
        n += 1
    ans = max(max_line)

    return ans