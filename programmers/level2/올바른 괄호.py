def solution(s):
    answer = False
    data = []
    for _ in s:
        if _ == '(':
            data.append('(')
        else :
            if data == [] :
                return False
            else :
                data.pop()
            
            
    return data==[]