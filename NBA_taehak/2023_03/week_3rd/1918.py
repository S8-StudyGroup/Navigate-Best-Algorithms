# [BOJ] 1918. 후위 표기식
# 소요 시간 : 00분
string = list(input())
pm = ['+', '-']
md = ['*', '/']
stack=[]
result=''

for char in string:
    if char.isalpha():
        result += char
    elif char == '(':
        stack.append(char)

    elif char in md:
        while stack and (stack[-1] in md):
            result += stack.pop()
        stack.append(char)

    elif char in pm:
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.append(char)
        
    elif char == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()
while stack:
    result += stack.pop()

print(result)

