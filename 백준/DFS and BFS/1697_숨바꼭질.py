from collections import deque

n, k = map(int, input().split())
visited = [0 for _ in range(100001)]

q = deque()

def bfs(a):
    q.append(a)
    visited[a] = 0
    
    while q:
        a = q.popleft()
        if a == k:
            return visited[a]
        
        for e in (a-1, a+1, 2*a):
            if 0<=e<=100000 and visited[e]==0:
                visited[e] = visited[a]+1
                q.append(e)
        
print(bfs(n))