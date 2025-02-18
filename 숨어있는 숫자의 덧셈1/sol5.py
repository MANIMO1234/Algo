def solution(my_string):
    answer = 0
    numbers = []

    for char in my_string:
        try:
            answer += int(char)  #글자는 error가 발생할 경우 except
         
        except:
            continue  #지속하라 이거라
        
    return answer

print(solution("aAb1B2cC34oOp"))