
# 숫자 문자열과 영단어

def solution(s):
    answer = s
    a = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
         'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    for key, value in a.items():
        answer = answer.replace(key, value)
    return int(answer)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))
