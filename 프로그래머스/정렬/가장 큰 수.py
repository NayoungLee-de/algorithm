def solution(numbers):
    answer = ''
    if sum(numbers) == 0:
        return "0"
    
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    answer = ''.join(numbers)
    
    return answer

print(solution([0,0,0,0]))