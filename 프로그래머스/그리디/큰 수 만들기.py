def solution(number, k):
    l = len(number)
    n = l - k
    answer = ''
    s = 0
    
    while n > 0:
        num1 = number[s:l-n+1]
        if '9' in num1:
            m1 = '9'
            m1_idx = num1.index(m1) + s
        else:
            m1 = max(num1)
            m1_idx = num1.index(m1) + s
        answer += m1
        s = m1_idx + 1
        n -= 1

    return answer

print(solution("1231234",3))