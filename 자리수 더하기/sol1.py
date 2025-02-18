# 정수 n이 매개변수로 주어질 때 n의 각 자리
#  숫자의 합을 return하도록 solution 함수를 완성해주세요



def solution(n):
   answer = 0
   #n을 10으로 나눴을 때 , 각각 나머지값이 필요한 것이다
   #몫이 0이 될때 까지 나눠야 한다. 
   #12344/10은 ....4 
   while n > 0:
     a, b = divmod(n ,10)
                                  #n을 10로 나눈 몫과 나머지  몫에 a에 들어가고, 
     answer = answer + b  
     n = a                # 각각을 할당 하는 것 a = n//10 ,divmode(n,10)[0]
   return answer
print(solution(1234))
print(solution(930211))


# 입출력 예
#n	result    # 숫자들을 각각의 튜블로 봐서 구한다
#1234	10
#930211	16


# 1 + 2 + 3 + 4 = 10을 return합니다.


