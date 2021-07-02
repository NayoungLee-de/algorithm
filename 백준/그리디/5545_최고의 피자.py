import sys
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
C = int(input())

D = []

for _ in range(N):
    a = int(input())
    D.append(a)

D.sort(reverse=True)
s = 0
money = A
cal = 0

for i in range(0,N):
    s = C + sum(D[0:i])
    money = A + B*i
    cal = max(cal,s//money)

print(cal)