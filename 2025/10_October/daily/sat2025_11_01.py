# sat2025_11_01.py

# 출처: 프로그래머스
# 수 조작하기

def solution(numLog):
    
    # condition = {
    #     1 :"w",
    #     -1 : "s",
    #     10 : "d",
    #     -10 : "a"
    # }

    # result_list = []

    # 방식 1    
    # for i in range(1, len(numLog)):
    #     num = numLog[i] - numLog[i-1]
    #     result_list.append(condition[num])

    # 방식 2
    # [result_list.append(condition[numLog[i] - numLog[i-1]]) for i in range(1, len(numLog))]
        
    # result = "".join(result_list)
    
    # 방식 3
    result = ''
    joystick=dict(zip([1,-1,10,-10],["w","s","d","a"]))

    for i in range(1, len(numLog)):
        result += joystick[numLog[i]-numLog[i-1]]

    return result

# numLog = [0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]	
# result = "wsdawsdassw"