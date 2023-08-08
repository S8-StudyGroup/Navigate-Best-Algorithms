# [BOJ] 25601. 자바의 형변환
# 소요 시간 : 00분

from sys import stdin

readline = stdin.readline

relation = {}
for _ in range(int(readline()) - 1):
    child, parent = readline().split()
    relation.update({child:parent})
pair = readline().split()
result = False
for i in range(2):
    j = int(not i)
    finding = pair[i]
    while True:
        try:
            if pair[j] == relation[finding]:
                print(1)
                result = True
                break
            else:
                finding = relation[finding]
        except:
            break
    if result:
        break
else:
    print(0)