#문자열 my_string과 문자 letter이 매개변수로 주어집니다.
#  my_string에서 letter를 제거한 문자열을 
# return하도록 solution 함수를 완성해주세요.

def solution(my_string, letter):

    result = []
    for word in my_string:
        if word != letter:
            result. append(word)
    return ''.join(result)  

print(solution("abcdef", "f"))  # "abcde"
print(solution("BCBdbe", "B"))  # "Cdbe"



#my_string	letter	result
#"abcdef"	"f"	"abcde"
#"BCBdbe"	"B"	"Cdbe"