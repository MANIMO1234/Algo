def solution(numbers):
    numbers.sort() #내림 차순의 정렬

    #return numbers[-1] * numbers[-2] # 올림 차순으로 정렬 해도 됩니다링
    return numbers[-1] * numbers[-2]

print(solution([1,2,3,4,5]))
print(solution([0,31,24,10,1,9]))