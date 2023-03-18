# [BOJ] 1918. 후위 표기식
# 소요 시간 : 30분

ans = ""
stack = []

# 전체를 괄호로 감싸고 시작
for val in "(" + input() + ")":

    # 여는 괄호라면 스택에 추가
    if val == "(":
        stack.append(val)

    # 닫는 괄호라면 스택에 여는 괄호(짝)까지 ans에 추가
    elif val == ")":
        while stack[-1] != "(":
            ans += stack.pop()
        stack.pop()
    
    # 더하기, 빼기라면
    elif val in ["+", "-"]:
        
        # 스택에서 여는 괄호를 만나기 전까지 stack에서 제거, ans에 추가하는 작업 반복
        while stack and stack[-1] != "(":
            ans += stack.pop()
        
        # 이후 stack에 해당 연산자 추가
        stack.append(val)

    # 곱하기, 나누기라면
    elif val in ["*", "/"]:

        # 스택에서 곱하기, 나누기를 만난다면 stack에서 제거, ans에 추가
        while stack and stack[-1] in ["*", "/"]:
            ans += stack.pop()
        
        # 이후 stack에 해당 연산자 추가
        stack.append(val)
    
    # 알파벳은 바로 ans에 추가
    else:
        ans += val

print(ans)