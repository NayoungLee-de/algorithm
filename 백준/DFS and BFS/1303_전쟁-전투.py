from collections import deque

m, n = map(int, input().split())
graph = [list(input()) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
W, B = 0, 0

    
visited = [[0]*m for _ in range(n)]

q = deque()

def bfs(x,y):
    q.append((x,y))
    visited[x][y] = 1
    cnt = 1

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and graph[x][y] == graph[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = 1
                cnt += 1
    return cnt

for a in range(n):
    for b in range(m):
        if visited[a][b] == 0:
            answer = bfs(a,b)
            if graph[a][b] == 'W': W += answer ** 2
            else: B += answer ** 2

print(W,B)