s = "((()()))"

# stack을 사용해서 '(' 나오면 append ')' 나오면 pop
# 해당 stack이 empty인지 확인 후 empty면 True, empty가 아니면 False 반환
# '('없는 상황에서 ')' 들어가면 바로 False 반환
def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
            # try except문 사용하여 진행 가능
            # try:
            #     stack.pop()
            # except IndexError:
            #     return False
        else:
            return False
    if len(stack) == 0:
        return True
    else:
        return False

    # len(s) 가 0이면 empty 이니까 True 노출, 0이 아니면 False노출
    # return len(s) == 0
print(solution(s))