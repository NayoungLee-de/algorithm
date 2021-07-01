def solution(n, words):
    answer = []
    done = []
    who = 0
    
    for i in range(len(words)-1):
        done.append(words[i])
        if words[i][-1] != words[i+1][0] or words[i+1] in done:
            who = (i+1)%n + 1
            n = (i+1)//n + 1
            break
    
    if who==0:
        answer = [0,0]
    else:
        answer = [who,n]
    return answer

solution(3,["hello", "one", "even", "never", "now", "world", "draw"],[3,3])