def solution(n):
    answer = 0
    for i in range(n+1, 1000001):
        print(i)
        if bin(n)[2:].count("1") == bin(i)[2:].count("1"):
            answer = i
            break
    return answer