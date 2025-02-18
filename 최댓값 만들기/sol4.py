
# 버블정렬


def solution(numbers):
    n = len(numbers) #길이
    for i in range(n): #렌의 마지막 수 만큼 반복
        for j in range(0 , n-i-1) : # 뒤에 있는 숫자가 들어 듬 
            if numbers[j] > numbers [j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    #return numbers[-1] * numbers[-2] # 올림 차순으로 정렬 해도 됩니다링
    return numbers[-1] * numbers[-2]

print(solution([1,2,3,4,5]))
print(solution([0,31,24,10,1,9]))