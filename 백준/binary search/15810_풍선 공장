import sys

input = sys.stdin.readline

_, m = map(int, input().split())
a = list(map(int, input().split()))

start, end = 0, min(a)*m

while start<=end:
    mid = (start + end) //2
    cnt = sum(mid//i for i in a) # mid초 일때 만들 수 있는 풍선의 개수

    if cnt<m:
        start = mid + 1
    else:
        end = mid - 1
        ans = mid
        
print(ans)
