# fri_2025_11_07

# 배열만들기4


# no2
def solution(arr):
    stk = []
    for i in range(len(arr)):
        while stk and stk[-1] >= arr[i]:
            stk.pop()
        stk.append(arr[i])
    return stk

# no1
def solution(arr):
    stk = []
    i = 0

    while i < len(arr):
        if stk:
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
            elif stk[-1] >= arr[i]:
                stk.pop()
        else:
            stk.append(arr[i])
            i += 1

    return stk