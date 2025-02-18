def solution(my_string):
    answer = 0
    numbers = []

    for char in my_string: # ord는 아스키 코드를 이용한것 a~z까지만 글자 ,숫자임을 물어봄
        if not (ord('A') <= ord(char) <= ord('z')):
            answer += int(char)
            

    return answer

print(solution("aAb1B2cC34oOp"))