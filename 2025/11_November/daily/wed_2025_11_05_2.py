# wed_2025_11_05_2.py

# 콜라츠 수열 생성

# no2 성공
def solution(n):
    answer = []

    while n != 1:
        answer.append(n)
        if n % 2 == 0:
            n = n/2
        elif n % 2 != 0:
            n = 3 * n + 1

    answer.append(n)

    return answer


# no1 실패
def solution(n):
    answer = []
    k = 0

    while n != 1:
        answer.append(n)
        if n % 2 == 0:
            k = n/2
            answer.append(k)
        elif n % 2 != 0:
            k = 3 * n + 1
            answer.append(k)

    return answer