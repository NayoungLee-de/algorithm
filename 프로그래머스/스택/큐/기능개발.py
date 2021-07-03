from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    q = deque(progresses)
    s = deque(speeds)
    
    while q:
        time = math.ceil((100 - q[0]) // s[0])

        for i in range(len(q)):
            q[i] += (s[i] * time)
        
        cnt = 0

        while len(q)>0 and q[0] >= 100:
            cnt += 1
            q.popleft()
            s.popleft()

        if cnt > 0:
            answer.append(cnt)
        
    return answer

print(solution([93, 30, 55],[1,30,5]))