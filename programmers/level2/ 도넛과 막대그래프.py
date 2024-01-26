from collections import defaultdict

def solution(edges):
    answer = [0,0,0,0]
    node_info = defaultdict(lambda :[0,0])
    #정점 별 [나가는 간선 수,들어오는 간선 수]  
    
    for a,b in edges :
        node_info[a][0] += 1
        node_info[b][1] += 1
    
    for node, info in node_info.items() :
        give = info[0]
        take = info[1]
        
        if give >= 2 and take == 0 : 
            answer[0] = node
        elif give ==0 and take >= 1 :
            answer[2] +=1
        elif give >= 2 and take >= 2:
            answer[3] +=1
    answer[1] = node_info[answer[0]][0] - answer[2] - answer[3]
        
    return answer