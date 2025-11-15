# sat_2025_11_15_1.py
# 프로그래머스 코테
# https://school.programmers.co.kr/learn/courses/30/lessons/181915

# no3. 압축. 성공
def solution(my_string, index_list):
  return ''.join([my_string[i] for i in index_list])

# no2. 성공
def solution(my_string, index_list):
    answer = []
    for i in index_list:
        answer.append(my_string[i])
        an = ''.join(answer) 
    return an

# no1. 실패
def solution(my_string, index_list):
    answer = ''
    for i in index_list:        
        answer.append(my_string[i]) # list.append(). append는 list를 받아야 한다
    return answer
  
