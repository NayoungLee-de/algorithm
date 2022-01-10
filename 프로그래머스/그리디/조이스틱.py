def solution(name):
    answer = 0
    c = [min(ord(ch)-ord('A'), ord('Z') - ord(ch) + 1) for ch in name]
    idx = 0
    
    while True:
        answer += c[idx]
        c[idx] = 0

        if sum(c) == 0:
            return answer
    
        le, ri = 1, 1
        
        while c[idx + ri] == 0:
            ri += 1
        while c[idx-le]==0:
            le += 1

        i = min(le, ri)
        answer += i
        idx += -le if le<ri else ri
        
print(solution("JAN"))