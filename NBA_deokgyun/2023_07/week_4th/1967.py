# [BOJ] 1967. 트리의 지름
# 소요 시간 : 00분

from sys import stdin

readline = stdin.readline

nodes_cnt = int(readline())

tree = [{} for _ in range(nodes_cnt + 1)]

for case in range(nodes_cnt - 1):
    parent, child, length = map(int, readline().split())
    tree[child].update({"parent" : [parent, length]})
    try:
        tree[parent]["child"].append([child, length])
    except:
        tree[parent].update({"child" : [[child, length]]})

layer = set()

for i in range(1, nodes_cnt + 1):
    if not tree[i].get("child"):
        try:
            tree[i].update({"over" : tree[i]["parent"][1]})
        except:
            tree[i].update({"over" : 0})
        if tree[i].get("parent") and tree[i]["parent"][0] not in layer:
            layer.add(tree[i]["parent"][0])

layer2 = set()

under_list = []

while layer:
    for node in layer:
        len_list = sorted(list(map(lambda x: tree[x[0]].get("over") if tree[x[0]].get("over") else 0, tree[node]["child"])), reverse=True)
        try:
            tree[node].update({"over" : len_list[0] + tree[node]["parent"][1]})
        except:
            tree[node].update({"over" : len_list[0]})
        try:
            tree[node].update({"under" : len_list[0] + len_list[1]})
        except:
            tree[node].update({"under" : len_list[0]})
        under_list.append(tree[node]["under"])
        if tree[node].get("parent") and tree[node]["parent"][0] not in layer2:
            layer2.add(tree[node]["parent"][0])
    else:
        layer = layer2
        layer2 = set()
try:
    print(max(under_list))
except:
    print(0)