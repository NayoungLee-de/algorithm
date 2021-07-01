import heapq
INF = 1e9

def solution(N,road,K):
    graph = [[] for _ in range(N+1)]
    q = []
    distance = [INF] * (N+1) 
    start = 1

    for a,b,c in road:
        graph[a].append((c,b))
        graph[b].append((c,a))

    heapq.heappush(q, (0, start))
    distance[start] = 0

    print(distance)
    while q:
        dist, now = heapq.heappop(q)
        print(dist, now)
        
        for a,b in graph[now]:
            if distance[b] > dist + a:
                distance[b] = dist + a
                heapq.heappush(q,(distance[b],b))
    
    cnt = 0
    for i in distance:
        if i <= K:
            cnt+= 1
    return cnt


print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))