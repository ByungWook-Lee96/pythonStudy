
n = 3
slicer = [1,5,2]
num_list = [1, 2, 3 ,4 ,5, 6, 7 , 8, 9]

def solution(n, slicer, num_list):
    answer = []

    if n == 1:
        answer = num_list[:slicer[1]+1]
    elif n == 2:
        answer = num_list[slicer[0]:]
    elif n == 3:
        answer = num_list[slicer[0]:slicer[1]+1]
    elif n == 4:
        answer = num_list[slicer[0]:slicer[1]+1:slicer[2]]
    else:
        print('잘못입력됨')

    return answer

print(solution(n, slicer, num_list))