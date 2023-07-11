# [BOJ] 3678. 카탄의 개척자
# 소요 시간 : 140분

board_list = [
    [1],
    [2, 3, 4, 5, 2, 3]
]

diagonal_idx = [
    [],
    [i for i in range(6)]
]

resource = [[1,1],[2,2],[3,2],[4,1],[5,1]]
resource.sort(key= lambda x:[x[1], x[0]])
total_count = 7

for shellnum in range(2, 1000):
    board_list.append([0 for _ in range(shellnum * 6)])
    diagonal_idx.append([])
    total_count += shellnum * 6
    relate_list = [(shellnum - 1)*6 - 1, 0]
    for idx in range(shellnum*6):
        if idx % shellnum == shellnum - 1:
            diagonal_idx[shellnum].append(idx)
            if idx == shellnum*6 - 1:
                for resource_idx in range(5):
                    if resource[resource_idx][0] not in [board_list[shellnum - 1][diagonal_idx[shellnum - 1][idx // shellnum]], board_list[shellnum][idx - 1], board_list[shellnum][0]]:
                        board_list[shellnum][idx] = resource[resource_idx][0]
                        resource[resource_idx][1] += 1
                        resource.sort(key=lambda x:[x[1], x[0]])
                        break
            else:
                for resource_idx in range(5):
                    if resource[resource_idx][0] not in [board_list[shellnum - 1][diagonal_idx[shellnum - 1][idx // shellnum]], board_list[shellnum][idx - 1]]:
                        board_list[shellnum][idx] = resource[resource_idx][0]
                        resource[resource_idx][1] += 1
                        resource.sort(key=lambda x:[x[1], x[0]])
                        break
        else:
            relate_resource = [board_list[shellnum - 1][relate_num] for relate_num in relate_list]
            if idx == 0:
                for resource_idx in range(5):
                    if resource[resource_idx][0] not in relate_resource:
                        board_list[shellnum][idx] = resource[resource_idx][0]
                        resource[resource_idx][1] += 1
                        resource.sort(key= lambda x:[x[1], x[0]])
                        relate_list.pop(0)
                        relate_list.append(relate_list[0] + 1)
                        break
            else:
                for resource_idx in range(5):
                    if resource[resource_idx][0] not in relate_resource + [board_list[shellnum][idx - 1]]:
                        board_list[shellnum][idx] = resource[resource_idx][0]
                        resource[resource_idx][1] += 1
                        resource.sort(key= lambda x:[x[1], x[0]])
                        relate_list.pop(0)
                        relate_list.append(relate_list[0] + 1)
                        break
    if total_count > 10000:
        break

result_list = []
for i in board_list:
    result_list += i

for test_cnt in range(int(input())):
    print(result_list[int(input()) - 1])