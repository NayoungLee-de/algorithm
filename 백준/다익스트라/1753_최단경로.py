import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
INF = 1e9

graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
        
def dijkstra():
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
            
        for x in graph[now]:
            if distance[x[0]] > dist + x[1]:
                distance[x[0]] = dist + x[1]
                heapq.heappush(q, (distance[x[0]], x[0]))

    for i in range(1,V+1):
        print(distance[i] if distance[i]!=INF else "INF")
dijkstra()