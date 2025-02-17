# 문자열 my_string이 매개변수로 주어집니다. 
# my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.


def solution(my_string):
    answer = 0
    numbers = list(range(10))
    result = [] 

    for onnum in my_string:
        if onnum  in numbers:
            result.append(sum(onnum))

    return answer

print(solution("aAb1B2cC34oOp"))

#my_string	result
#"aAb1B2cC34oOp"	10
#"1a2b3c4d123"	16
# 숫자만 골라서 더한다 
# 문자를 제거 한다 > 어려움 