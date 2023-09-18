k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]


def solution(k, m, score):
    count = m
    minimum = 0
    while k > 0:
        for i in score:
            if i == k:
                count = count - 1
                print(f'i는 {i}, count는 {count}, k는 {k}')
            if count == 0:
                minimum = k
                print(minimum)
                return minimum * m * len(score)
        k = k - 1

    return minimum * m


print(solution(k, m, score))
