import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n , m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    ans = 0

    for i in b:
        idx = bisect_right(a, i)
        ans += n - idx

    print(ans)