# [BOJ] 10799. 쇠막대기
# 소요 시간 : 20분
# 아이디어 1. 여는 괄호면 쇠막대기 추가
# 아이디어 2. 닫는 괄호면 쇠막대기 하나 제거
# 아이디어 2-1. 레이저면 쇠막대기 수만큼 answer 추가
# 아이디어 2-2. 쇠막대기 끝이면 쇠막대기 1개만 추가

brackets = list(input().strip())
answer = 0
iron = 0

for index, bracket in enumerate(brackets):
    if bracket == '(':
        iron += 1
    else:
        iron -= 1
        if brackets[index-1] == '(':
            answer += iron
        else:
            answer += 1

print(answer)
