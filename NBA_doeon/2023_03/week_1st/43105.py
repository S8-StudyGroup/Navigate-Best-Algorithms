# [Programmers] 43105. 정수 삼각형
# 소요 시간 : 40분

def solution(triangle):
    answer = 0
    sum_case = [[triangle[0]]]
    
    for i in range(1, len(triangle)):
        row = []
        for j in range(len(triangle[i])):
            upper = sum_case[i - 1]
            here_case = []
            if j - 1 >= 0:
                a = max(upper[j - 1])
                here_case.append(a + triangle[i][j])
            if j < len(upper):
                b = max(upper[j])
                here_case.append(b + triangle[i][j])
            
            row.append(here_case)
        sum_case.append(row)
    
    floor = sum_case[-1]
    max_value = 0
    
    for idx in range(len(floor)):
        for length in range(len(floor[idx])):
            if floor[idx][length] > max_value:
                max_value = floor[idx][length]
                
    answer = max_value
    
    return answer