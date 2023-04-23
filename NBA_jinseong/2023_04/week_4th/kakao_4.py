# [Programmers 2023 KAKAO BLIND TEST] 4. 표현 가능한 이진트리
# 소요 시간 : 60분

def half(binary: str):
    if len(binary) == 1:
        return True
    if '1' in binary:
        if binary[len(binary) // 2] == '1':
            return half(binary[:len(binary) // 2]) and half(binary[len(binary) // 2 + 1:])
        else:
            return False
    else:
        return True


def solution(numbers):
    answer = []
    for number in numbers:
        binary = ''
        while number > 0:
            temp = number % 2
            number = number // 2
            binary = str(temp) + binary
        for i in range(1, 15):
            if 2 ** i - 1 < len(binary) <= 2 ** (i + 1) - 1:
                temp = 2 ** (i + 1) - 1 - len(binary)
                binary = '0' * temp + binary
        if half(binary):
            answer.append(1)
        else:
            answer.append(0)

    return answer