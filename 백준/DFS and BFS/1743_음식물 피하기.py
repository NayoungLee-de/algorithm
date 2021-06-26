# bfs. 인접한 음식물만 체크 (1303 전쟁 문제와 비슷)

from collections import deque

n,m,k = map(int, input().split())
graph = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and graph[nx][ny]==1:
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
    
    return cnt

result = 0

for a in range(n):
    for b in range(m):
        if visited[a][b]==0 and graph[a][b] == 1:
            result = max(result,bfs(a, b))

print(result)