# [SWEA] 1238. Contact
# 소요 시간 : 100분


for test_count in range(1, 11):
    line_count, starting_person = map(int, input().split())
    input_line_list = list(map(int, input().split()))
    line_list = [[] for _ in range(101)]
    for i in range(len(input_line_list)):
        if i & 1:
            line_list[input_line_list[i - 1]].append(input_line_list[i])
    distance_list = [0] * 101
    distance = 1
    the_queue = [starting_person]
    while the_queue:
        i = the_queue.pop(0)
        for k in line_list[i]:
            if distance_list[k] == 0:
                the_queue.append(k)
                distance_list[k] = distance_list[i] + 1
    max_distance = max(distance_list)
    last_people_list = []
    for p in range(1, 101):
        if distance_list[p] == max_distance:
            last_people_list.append(p)
    print("#%d %d" %(test_count, max(last_people_list)))