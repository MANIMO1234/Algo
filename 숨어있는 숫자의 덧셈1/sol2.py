def solution(my_string):
    answer = 0
    numbers = []

    for char in my_string:
        if char.isdigit():
            numbers.append(int(char))

    return sum(numbers)

print(solution("aAb1B2cC34oOp"))


#my_string	result
#"aAb1B2cC34oOp"	10
#"1a2b3c4d123"	16
# 숫자만 골라서 더한다 
# 문자를 제거 한다 > 어려움 