def solution(s):
    words = s.split(' ')
    answer=""
    for idx, word in enumerate(words):
        if idx >0:
            answer += " "
        answer += word.capitalize()
    return answer
        
solution("3people unFollowed me")