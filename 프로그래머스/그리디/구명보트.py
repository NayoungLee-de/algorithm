def solution(people, limit):
    answer = 0
    people.sort()
    num = len(people)
    right = num-1
    
    for a in range(num):
        if a > right:
            break
        
        if people[a] > limit/2:
            people[a] = 0
            answer += 1
            continue
        
        l = limit - people[a]
        people[a] = 0
        
        for b in range(right, a, -1):
            if people[b] <= l:
                right = b-1
                people[b] = 0
                break
        answer += 1
    
    c = [a for a in people if a != 0]
    answer += len(c)
    return answer

print(solution([70, 80, 50], 100))