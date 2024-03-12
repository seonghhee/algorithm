def solution(s):
    answer = 1

    stack = []
    for i in range(len(s)):
        if not stack :
            stack.append(s[i])
        else : 
            if s[i] == stack[-1]:
                stack.pop()
            else :
                stack.append(s[i])
    if stack :
        answer = 0
    return answer