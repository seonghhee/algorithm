def solution(s):
    answer = []
    words = s.split(" ")
    for word in words:
        if word:
            word= word.lower()
            word = word[0].upper()+word[1:]
            answer.append(word)
            
        else :
            answer.append(word)
            
    return " ".join(answer)