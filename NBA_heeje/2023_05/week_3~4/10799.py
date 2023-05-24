# [BOJ] 10799. 쇠막대기
# 소요 시간 : 10분

brackets = input()

cnt_stick = 0
dup_stick = 0

for bracket in brackets:

    # 여는 괄호일 때 쇠막대기 겹침
    if bracket == "(":
        dup_stick += 1
        last = bracket
    
    # 닫는 괄호일 때
    else:
        
        # 레이저면 쇠막대기 자르고 cnt_stick에 추가
        if last == "(":
            cnt_stick += dup_stick - 1
            last = bracket

        # 레이저가 아니면 cnt_stick에 1 추가
        else:
            cnt_stick += 1
        
        dup_stick -= 1

print(cnt_stick)