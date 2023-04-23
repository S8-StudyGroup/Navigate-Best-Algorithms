# [Programmers 2023 KAKAO BLIND TEST] 4. 표현 가능한 이진트리
# 소요 시간 : 00분

# 포화이진트리 노드 개수
node_cnts = [1]
height = 1
node_cnt = 1
while node_cnt <= 50:
    node_cnt = 2 ** (height + 1) - 1
    node_cnts.append(node_cnt)
    height += 1


def mybinary(number):
    '''
    @params
        number : 숫자
    @return
        포화 이진트리를 만들수 있을 만큼 앞에 0이 붙은 이진수
    '''
    bin_num = bin(number)[2:]
    bin_len = len(bin_num)

    for node_cnt in node_cnts:
        diff =  bin_len - node_cnt

        if diff > 0:
            continue
        else:
            bin_num = '0'*-diff + bin_num
            break

    return bin_num


def treeable(bin_num):
    layers = [bin_num]
    bintree = [1]

    while len(layers[0]) > 2:
        next_layers = []
        for layer in layers:
            mid_idx = len(layer) // 2
            bintree.append(layer[mid_idx])
            next_layers.append(layer[:mid_idx])
            next_layers.append(layer[mid_idx+1:])
        layers = next_layers

    while layers:
        layer = layers.pop(0)
        for num in layer:
            bintree.append(num)

    for idx, tree_node in enumerate(bintree):
        if tree_node == '1' and bintree[idx//2] == '0':
            return 0
    return 1


def solution(numbers):
    answer = []
    for number in numbers:
        bin_num = mybinary(number)
        answer.append(treeable(bin_num))
    return answer


print(solution([63]))