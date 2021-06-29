# 최단거리 -> bfs
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[]*m for _ in range(n)]
visited = [0] * n

for i in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)

q = deque()
x -= 1 # 인덱스 0번부터 시작 맞추기 위해

def bfs():
    q.append(x)
    visited[x] = 1

    while q:
        a = q.popleft()
        for i in graph[a]:
            if visited[i]==0 or visited[i] > visited[a]+1:
                q.append(i)
                visited[i] = visited[a] + 1
    
    if k+1 not in visited:
        print(-1)
        return
    
    for i in range(len(visited)):
        if visited[i] == (k+1):
            print(i+1)
bfs()


