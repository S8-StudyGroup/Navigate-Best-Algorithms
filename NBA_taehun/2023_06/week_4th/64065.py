# [Programmers] 64065. 튜플
# 소요 시간 : 15분


def solution(s):
    s = s[2:-2]
    # 원소의 개수를 기준으로 정렬
    arr = sorted(
        list(map(lambda x: set(x.split(",")), s.split("},{"))), key=lambda x: len(x)
    )
    old_v = arr[0]
    result = [list(old_v)[0]]

    for v in arr[1:]:
        now_v = v - old_v
        result += list(now_v)
        old_v = v

    return list(map(int, result))


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
