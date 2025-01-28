def solution(s):
    a= s.split(" ")
    b=[]
    for i in a:
       b.append(int(i))
    return str(min(b)) + ' ' + str(max(b))