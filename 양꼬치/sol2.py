def solution(n, k):
    answer = (12000 * n) + (2000 * k)
    # 양꼬치 인분수 :n
    # 음료수 개수 : k
    if n >= 10:
        service = n // 10
        answer = n * 12000 + (k - service) * 2000

    else:
        answer = n * 12000 + k * 2000

    return answer 
   
print(solution(10, 3)) #124000
print(solution(64, 6)) #768000


#