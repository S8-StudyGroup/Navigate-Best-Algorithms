# [Programmers] 131127. 할인 행사
# 소요 시간 : 00분
def solution(want, number, discount):
    answer = 0
    w = len(want)
    d = len(discount)
    want_list = sorted([want[i] for i in range(w) for _ in range(number[i])])

    for i in range(d - 9):
        cur_want = sorted(discount[i:i+10])
        if cur_want == want_list:
            answer += 1

    return answer
