from itertools import combinations


def cal(line1,line2): #교점 반환
    x1, y1, c1 = line1
    x2, y2, c2 = line2
    
    if x1*y2 == x2*y1 :#기울기가 같을 경우 - 교점이 무수히 많음
        return
    
    x = (y1*c2-c1*y2)/(x1*y2-y1*x2)
    y = (c1*x2-x1*c2)/(x1*y2-y1*x2)
    
    if x == int(x) and y ==int(y): #x와 y가 모두 정수이면 return
        return [int(x),int(y)]

def solution(lines):
    points = []
    for line1, line2 in combinations(lines,2):
        point= cal(line1,line2)
        if point:
            points.append(point)
    
    #별의 시작점과 끝점 찾기
    w1,w2 = min(points, key= lambda x : x[0])[0], max(points, key = lambda x : x[0])[0]+1
    h1,h2 = min(points, key= lambda x : x[1])[1], max(points, key = lambda x : x[1])[1]+1
    
    answer = [['.']*(w2-w1) for _ in range(h2-h1)]
    
    for x, y in points:
        answer[y-h1][x-w1] = '*'
    
    answer.reverse()
    
    return [''.join(a) for a in answer]
