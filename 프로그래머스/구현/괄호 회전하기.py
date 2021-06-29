from collections import deque

def solution(s):
    left = ['{','[','(']
    right = ['}',']',')']
    l = len(s)
    if l%2==1:
        return 0
    answer = 0
    
    for a in range(l): # rotate
        q = deque(s)
        q.rotate(-a)
        for b in range(l-1): # 올바른지 확인
            if q[b] in left and not q[b].isalpha():
                idx = left.index(q[b])
                q[b] = 0
                for c in range(b+1, l,2):
                    if q[c] == right[idx]:
                        q[c] = 0
                        break
        if list(q)==[0]*l:
            answer += 1
    return answer

solution("[](){}")