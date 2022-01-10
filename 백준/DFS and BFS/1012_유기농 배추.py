from collections import deque

import sys
input = sys.stdin.readline

t = int(input())

dx = [-1, 1, 0 , 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<m and 0<=ny<n:
                if graph[nx][ny]==1 and visited[nx][ny]==0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
            
for i in range(t):
    m, n, k = map(int, input().split())

    graph = [[0]*n for _ in range(m)]
    visited = [[0]*n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    
    ans = 0

    for a in range(m):
        for b in range(n):
            if visited[a][b] == 0:
                if graph[a][b] == 1:
                    ans += 1
                    bfs(a, b)
    print(ans)