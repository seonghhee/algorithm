def solution(clothes):
    answer = 1
    type = {b: [] for a,b in clothes}
    
    for a,b in clothes:
        tmp = type[b]
        tmp.append(a)
    
    for a in type.values():
        answer*= (len(a)+1)
            
    print(type)
    
    return answer-1