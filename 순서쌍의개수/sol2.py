
from math import sqrt
def solution(n):
    answer = 0

    for num in range(1, int(sqrt(n))+1): # 100 까지 해야 하면 제곱수= 루트를 해서 그 수가 나올 때 
         if n % num == 0:                   #int(n**0.5)랑 같다             # 까지 하면 된다
              answer += 2 

              if num * num == n:
                   answer -= 1

    return answer

print(solution(20))
print(solution(100))

