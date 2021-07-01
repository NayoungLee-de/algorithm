import sys
import heapq
input = sys.stdin.readline
INF = 1e9

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for i in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c)) 

start, end = map(int, input().split())

def dijkstra():
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for x in graph[now]:
            d, n = x[1], x[0]
            if distance[n] > dist + d:
                distance[n] = dist + d
                heapq.heappush(q,(distance[n],n))

    return distance[end]

print(dijkstra())