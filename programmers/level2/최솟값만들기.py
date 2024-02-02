def solution(A,B):
    answer = 0
    A.sort(reverse=False)
    B.sort(reverse=True)

    for a,b in zip(A,B):
        answer+= a*b
    return answer