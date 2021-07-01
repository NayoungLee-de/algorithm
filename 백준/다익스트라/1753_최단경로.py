import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input()) - 1
INF = 11
graph = [[] for _ in range(V)]
distance = [INF] * (V)

for i in range(E):
    a,b,c = map(int, input().split())
    graph[a-1].append((c,b-1))

def dijkstra():
    q = []
    heapq.heappush(q,(0,start))

    while q:
        dist, now = heapq.heappop(q)
        distance[now] = dist

        for d,n in graph[now]:
            if distance[n] > dist + d:
                distance[n] = dist + d
                heapq.heappush(q, (distance[n], n))

    for i in range(len(distance)-1):
        if distance[i] == INF:
            print("INF")
        else:
            print(distance[i])

    if distance[len(distance)-1] == INF:
        print("INF")
    else:
        print(distance[i])

dijkstra()