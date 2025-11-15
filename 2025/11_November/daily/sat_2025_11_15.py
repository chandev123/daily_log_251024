# sat_2025_11_15.py
# 주목할만한 코드
# 프로그래머스 코테. 주사위 게임3. 
# https://school.programmers.co.kr/learn/courses/30/lessons/181916?language=python3

def solution(a, b, c, d):
    l = sorted([a, b, c, d]) # sorted() 오름차순 정렬O, 중복제거X

    return (a * 1111 if l[0] == l[-1] # [-1] 인덱싱 주목.
            else (10 * l[0] + l[3]) ** 2 if l[0] == l[-2] 
            else (10 * l[-1] + l[0]) ** 2 if l[1] == l[-1] 
            else (l[0] + l[-1]) * abs(l[0] - l[-1]) if l[0] == l[1] and l[2] == l[3] # if and
            else min(l) if len(set(l)) == 4 
            else a * b * c * d // next(filter(lambda x: [a, b, c, d].count(x) == 2, l)) ** 2) # 하단
# set(). 중복제거, 순서X -> 인덱싱X
# next(). 순서대로 인출
# filter(condtion, iterable)
# count(). 의 메소드 체이닝
