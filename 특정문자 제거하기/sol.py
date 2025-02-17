#문자열 my_string과 문자 letter이 매개변수로 주어집니다.
#  my_string에서 letter를 제거한 문자열을 
# return하도록 solution 함수를 완성해주세요.

def solution(my_string, letter):

    result = []
    for word in my_string:
        if word  not in 'letter':
            result. append(word)

 print(solution('abcdef', 'f'))
 print(solution(''.join('abcdef','f'))



#my_string	letter	result
#"abcdef"	"f"	"abcde"
#"BCBdbe"	"B"	"Cdbe"