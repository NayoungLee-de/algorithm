def solution(n):
    answer = []
    direction = [(1,0),(0,1),(-1,-1)]
    
    graph = [[0]*i for i in range(1,n+1)]
    
    
    x,y = 0,0
    d ,cnt = 0, 1

    for a in range(n,0,-1):
        for b in range(a):
            graph[x][y] = cnt
            cnt += 1
            print(b,x, y)
        
            if b == a-1:
                d = (d+1)%3
            n_x, n_y = direction[d]
            x += n_x
            y += n_y

    print(graph)
    return answer

solution(4)