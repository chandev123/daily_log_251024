# tue_2025_11_04.py

# 프로그래머스 배열 만들기2

# 정답
def solution(l,r):
    answer = []
    
    for i in range(l, r+1):
        if not set(str(i)) - set(['0', '5']):
            answer.append(i)
    
    return answer if answer else [-1]

# 1차 시도
def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if i == 0:
            answer.append(i)
        elif i == 5:
            answer.append(i)

    if not answer:
        answer.append(-1)
        
    return answer

# 2차 시도
def solution(l, r):
    answer = []

    for i in range(l, r+1):
        s = list(str(i))
        s2 = sorted(s)
        
        if s2 == '0':
            if s2 == '5':
                answer.append(-1)
            else:
                answer.append(i)
    return answer