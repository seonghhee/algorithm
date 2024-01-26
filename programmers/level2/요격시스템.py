#greedy

def solution(targets):
    answer = 0
    targets.sort(key = lambda x : x[1]) #e를 기준으로 정렬
    
    e_check = 0
    for target in targets: 
        if target[0] >= e_check: #s가 e_check보다 큰 경우 
            answer+= 1 #요격
            e_check = target[1] #update
    
    return answer