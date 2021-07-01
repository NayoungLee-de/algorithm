# c언어에서는 2진법 만들 때 항상 직접 구현했어서 
# 이번에도 binary 함수를 만들었는데,,
# 파이썬에는 bin() 함수가 이진법을 만들어준다!
# 다만 0bxx 형식으로 나오니 숫자만 얻기 위해서는 
# [2:] 범위만 가져오면 된다.

def binary(n):
    a = ''
    while n >= 1:
        a = str(n%2) + a
        n = n//2
    return a
    
def solution(s):
    cnt = 0
    z = 0
    answer = s
    
    while len(answer)>1 or answer[0] != '1':
        z += answer.count('0')
        answer = answer.replace('0','')

        n = len(answer)
        answer = bin(n)[2:]
        print(answer)
        cnt += 1
    
    return [cnt,z]

print(solution("110010101001"))