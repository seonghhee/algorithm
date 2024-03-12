def solution(brown, yellow):
    answer = [0,0]
    size = brown + yellow
    for i in range(int(size**(1/2)),size):
        w,h = i, size/i
        if w == int(i) and h ==int(size/i):
            if brown == 2*w + 2*(h-2) and yellow == size -(2*w + 2*(h-2)):
                answer = [w,h]
    
    return answer