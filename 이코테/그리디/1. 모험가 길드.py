n = int(input())
scare = list(map(int,input().split()))

group = [[]*i for i in range(n)]
cnt = 0 

while len(scare) > 0:
    mi = min(scare)
    scare.remove(mi)

    group[cnt].append(mi)
    if len(group[cnt]) >= mi:
        cnt += 1

print(cnt)