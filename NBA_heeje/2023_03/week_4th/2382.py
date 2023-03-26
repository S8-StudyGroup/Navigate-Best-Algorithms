# [SWEA] 2382. 미생물 격리
# 소요 시간 : 00분10:58

def move() -> None:
    """
    1시간마다 군집을 이동방향에 있는 다음 셀로 이동시켜주는 함수
    """
    dy = [0, -1, 1, 0, 0]
    dx = [0, 0, 0, -1, 1]

    for key, val in microbe_dict.items():
        microbe_dict[key][0] = val[0] + dy[val[3]]
        microbe_dict[key][1] = val[1] + dx[val[3]]


def check_corner() -> None:
    """
    미생물 군집이 약품이 칠해진 셀에 도착했을 경우를 처리해주는 함수
    """
    reverse_dir = [0, 2, 1, 4, 3]

    for key, val in microbe_dict.items():
        if val[0] in (0, N - 1) or val[1] in (0, N - 1):
            microbe_dict[key][2] //= 2
            microbe_dict[key][3] = reverse_dir[microbe_dict[key][3]]


def combine() -> None:
    """
    두 개 이상의 군집이 한 셀에 모이는 경우를 처리해주는 함수
    """
    combine_dict = dict()
    for key, val in microbe_dict.items():
        coordinate = (val[0], val[1])
        if combine_dict.get(coordinate):
            combine_dict[coordinate].append(key)
        else:
            combine_dict[coordinate] = [key]
    
    for key_list in combine_dict.values():
        if len(key_list) > 1:
            sum_microbe = sum([microbe_dict[key][2] for key in key_list])
            max_microbe = max([microbe_dict[key][2] for key in key_list])
        
            for key in key_list:
                if microbe_dict[key][2] != max_microbe:
                    del microbe_dict[key]
                else:
                    microbe_dict[key][2] = sum_microbe

    # 3개 중에서 가장 세포가 많은 군집의 방향으로 설정..
    # 순서대로 합병해버리면 안된다.
    # combine_dict = dict()
    # delete_key_list = []
    # for key, val in microbe_dict.items():
    #     coordinate = (val[0], val[1])
    #     if coordinate in combine_dict:
    #         sum_microbe = microbe_dict[combine_dict[coordinate]][2] + val[2]
    #         if microbe_dict[combine_dict[coordinate]][2] < val[2]:
    #             delete_key_list.append(combine_dict[coordinate])
    #             combine_dict[coordinate] = key
    #             microbe_dict[combine_dict[coordinate]][3] = val[3]
    #         else:
    #             delete_key_list.append(key)
    #         microbe_dict[combine_dict[coordinate]][2] = sum_microbe
    #     else:
    #         combine_dict[coordinate] = key

    # for key in delete_key_list:
    #     del microbe_dict[key]

def total_of_microbe() -> int:
    """
    M시간 후 남아 있는 미생물 수의 총합을 구하는 함수
    """
    total = 0
    for val in microbe_dict.values():
        total += val[2]
    
    return total


T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    microbe_dict = {}
    for n in range(1, K + 1):
        microbe_dict[n] = list(map(int, input().split()))
    
    for time in range(M):
        move()
        check_corner()
        combine()
    
    print(f"#{tc} {total_of_microbe()}")