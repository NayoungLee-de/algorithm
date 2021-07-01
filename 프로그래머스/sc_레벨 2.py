from collections import deque

s,e = ord('A'), ord('Z')
dic = deque([0])

for i in range(s, e+1):
    dic.append(chr(i))

def solution(msg):
    answer = []
    l = len(msg)
    x = 0
    while x < l:
        cnt = 1
        word = msg[x:x+cnt]
        while word in dic:
            cnt += 1
            word = msg[x:x+cnt]

            if x+cnt==l+1:
                answer.append(dic.index(word))
                return answer
        
        before = msg[x:(x+cnt-1)]
        answer.append(dic.index(before))
        dic.append(word)

        x = x+cnt-1

        if x == l-1:
            answer.append(dic.index(msg[x]))
            break
    return answer

print(solution("ABABABABABABABAB"))