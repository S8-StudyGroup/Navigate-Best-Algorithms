# [Programmers] 64065. 튜플
# 소요 시간 : 30분

def solution(s):
    answer = []
    tuple_dict = {}
    idx = 1
    while idx < len(s) - 1:
        if s[idx] == "{":
            idx += 1
            s_set = set()
            num = ""
            while True:
                
                # 숫자일 때
                if s[idx] not in [",", "}"]:
                    num += s[idx]
                else:
                    s_set.add(int(num))
                    num = ""
                    
                if s[idx] == "}":
                    break
                idx += 1
            tuple_dict[len(s_set)] = s_set
        idx += 1

    answer.append(list(tuple_dict[1])[0])

    # 현재 set과 이전 set을 빼고 남은 것을 answer에 추가
    for i in range(2, len(tuple_dict) + 1):
        remainder = tuple_dict[i] - tuple_dict[i - 1]
        answer.append(list(remainder)[0])
    return answer