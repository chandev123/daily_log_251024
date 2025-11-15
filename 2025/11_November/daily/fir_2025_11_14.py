# fri_2025_11_14.py
# 주사위문제3
# https://school.programmers.co.kr/learn/courses/30/lessons/181916

# no2
def solution(a, b, c, d):
    l = [a,b,c,d]
    c = [l.count(x) for x in l]
    if max(c) == 4:
        return 1111*a
    elif max(c) == 3:
        return (10*l[c.index(3)]+l[c.index(1)])**2
    elif max(c) == 2:
        if min(c) == 1:
            return eval('*'.join([str(l[i]) for i, x in enumerate(c) if x == 1]))
        else:
            return (max(l) + min(l)) * abs(max(l) - min(l))
    else:
        return min(l)

# no1
def solution(a, b, c, d):   
    answer = 0
    s = [a,b,c,d]
    o = sorted(s)
    c = set(s)
    
    if len(c) == 1:
        answer = 1111 * a
    elif len(c) == 2:
        if min(c) == o[o]:
            
        if o[1] == o[2]:
            answer = (10 * o[1] * o[2]) ** 2
        else:
            answer = (o[2] + o[3]) * abs(o[2] - o[3])
    else:
        answer = o[0]
    return answer
