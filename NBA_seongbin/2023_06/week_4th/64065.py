# [Programmers] 64065. 튜플
# 소요 시간 : 00분
def solution(s):
    answer = []

    # 문자 s를 리스트로 변경
    s = list(s[2:-2].split('},{'))

    # 집합의 길이 순으로 정렬
    sorted_s = sorted(s, key=lambda x: len(x))

    # 요소의 가장 마지막 값을 반환
    for i in sorted_s:
        # answer이 비어있지 않을 경우
        if answer:
            i = i.split(',')
            for j in i:
                if int(j) in answer:
                    continue
                else:
                    answer.append(int(j))
        else:
            answer.append(int(i))

    return answer
