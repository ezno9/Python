
# 소수 만들기

from itertools import combinations

def prime(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                return False
        return True


def solution(nums):
    answer = 0
    cmb = list(combinations(nums, 3))
    for arr in cmb:
        if prime(sum(arr)):
            answer += 1
    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))
