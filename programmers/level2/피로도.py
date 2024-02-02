from itertools import permutations
def solution(k, dungeons):
    answer = 0
    
    for p in permutations(dungeons,len(dungeons)):
        tmp = k
        count = 0
        
        for need,spend in p:
            if tmp >= need:
                tmp -= spend
                count += 1
        answer = max(answer,count)
    return answer