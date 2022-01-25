# 두 개 뽑아서 더하기
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[j])
    return sorted(set(answer))

answer = solution([5,0,2,7])
print(answer)