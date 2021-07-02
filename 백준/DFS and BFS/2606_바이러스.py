# dfs

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = -1

def dfs(v):
    global cnt
    cnt += 1
    visited[v] = 1

    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)
    
    return cnt

print(dfs(1))