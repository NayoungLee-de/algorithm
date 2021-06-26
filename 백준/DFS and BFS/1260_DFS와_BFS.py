from collections import deque

n, m, v= map(int, input().split())

graph = [[]*i for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

def dfs(v):
    if visited[v] == True:
        return

    print(v,end = ' ')
    visited[v] = True
    w = sorted(graph[v])
    for i in w:
        if visited[i] == False:
            dfs(i)

q = deque([v])

def bfs(v):
    while q:
        a = q.popleft()
        visited[a] = True
        print(a,end=' ')

        w = sorted(graph[a])
        for i in w:
            if visited[i]==False and i not in q:
                q.append(i)

dfs(v)
print()
visited = [False] * (n+1)
bfs(v)