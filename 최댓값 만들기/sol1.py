def solution(numbers):
    first_max = max(numbers)
    numbers.remove(first_max)
    second_max = max(numbers)
    return first_max * second_max
    #return  list( from math.max(numbers)
print(solution([1,2,3,4,5]))
print(solution([0,31,24,10,1,9]))