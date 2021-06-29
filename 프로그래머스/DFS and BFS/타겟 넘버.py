def solution(numbers, target):
    l = len(numbers)
    answer = 0
    
    def dfs(idx, n):
        nonlocal answer
        if idx < l-1:
            idx+=1
            dfs(idx,n+numbers[idx])
            dfs(idx,n-numbers[idx])
        elif idx == l-1:
            if n == target:
                answer += 1
            return
        
    dfs(0,numbers[0])
    dfs(0,-numbers[0])
    return answer