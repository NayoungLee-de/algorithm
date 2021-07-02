def solution(n):
    answer = []
    direction = [(0,1),(1,0),(-1,-1)]
    graph = [[0]* n for _ in range(n)]
    x, y = 0, 0
    cnt = 1
    d = 0

    for a in range(n,0,-1):
        for b in range(a):
            graph[x][y] = cnt
            cnt += 1

            if b==a-1:
                d = (d+1)%3
            nx, ny = direction[d]
            x, y = x+nx, y+ny
            

    for a in range(n):
        for b in range(n):
            k = graph[a][b]
            if k != 0:
                answer.append(k)
    return answer

print(solution(5))