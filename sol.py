# 머쓱이네 양꼬치 가게는 10인분을 먹으면 음료수 하나를 서비스로 줍니다. 
# 양꼬치는 1인분에 12,000원, 음료수는 2,000원입니다. 정수 n과 k가
# 매개변수로 주어졌을 때, 양꼬치 n인분과 음료수 k개를 먹었다면 총얼마를 지불해야 
# 하는지 return 하도록 solution 함수를 완성해보세요.

    
def solution(n, k):
    # 양꼬치 인분수 :n
    # 음료수 개수 : k
            # 양꼬치 총액    음료 총액    서비스 음료수 가격 
    answer = n * 12000 + k * 2000 - (n//10*2000)
    
    return answer

print(solution(10, 3)) #124000
print(solution(64, 6))
    
    
    
    
    #if n >= 10

    #for h in solution 
        #if h % 10 == 0:
           # return k = 1
    #else:
       
    #return answer    
