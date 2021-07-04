def solution(number):
    if number <= 0:
        return 0
    summ = 0
    for i in range(3, number):
        if i % 3 == 0 or i % 5 == 0:
            summ += i
    return summ

print(solution(10))